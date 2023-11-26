## Simple Python Keystroke Logger
<hr>

Keystroke loggers or Keyloggers are software or hardware tools that record every keystroke made on a device. They can be used for a variety of purposes, both legitimate and malicious.

The provided code defines a class named `Keylogger` that implements a keylogging functionality. It captures keystrokes, records the active window name, and periodically logs the captured data to a file.

**NOTE**: This project should be used for authorized testing or educational purposes only. You are free to copy, modify and reuse the source code at your own risk.
<hr>

### Uses
- **Parental monitoring**: Parents can use keyloggers to monitor their children's online activity and protect them from cyberbullying, online predators, and inappropriate content.
- **Employee monitoring**: Employers can use keyloggers to monitor employee productivity and ensure that they are using company computers for work purposes.
- **Investigating cybercrime**: Law enforcement can use keyloggers to investigate cybercrime and gather evidence.
- **User input analysis**: Software developers can use keyloggers to analyze user input and improve the usability of their software.
- **Self-analysis and assessment**.
<hr>

### Features
- **Keystroke Capture**: The `_on_key_press` method captures every keystroke made on the keyboard and stores it in the line buffer.
- **Window Name Tracking**: The `_on_key_press` method also detects changes in the active window and records the current window name before logging the line buffer.
- **Time-Based Logging**: The `_report_loop` method periodically logs the line buffer to a file based on the _MINUTES_TO_LOG_TIME interval.
- **File Management**: The `_log` method creates timestamped log files and appends the captured data to the appropriate file.
- **Special Key Handling**: The code handles special keys like `Ctrl`, `Shift`, `Alt`, and `Space` appropriately.
- **Caps Lock Awareness**: The `_get_capslock_state` method determines the Caps Lock state and applies it to the captured keystrokes.
- **Character Limit Control**: The `_log` method checks the line buffer length and triggers a log event when it reaches the `_CHAR_LIMIT`.
- **Exception Handling**: The `_log` method handles exceptions that might occur during file writing.
- **Multithreading**: The `_report_loop` method utilizes threading to enable continuous keystroke capture and logging while the program is running.
<hr>

### Getting started
#### System requirements
- MS Windows (tested on 11). `Linux or MacOS not tested`
- [Python 3](https://www.python.org/downloads/) (tested on v3.10).
#### Usage
##### Quick Setup
- `git clone https://github.com/yashanksingh/keylogger`
- `cd keylogger`
- `python -m pip install -r requirements.txt` (alternatively `pip ...`)
###### Run as a standalone Python script
```py
# Stores logs in the main directory
from keylogger import Keylogger
Keylogger().run()
``` 
```py
# Stores logs in logs folder inside root directory
from keylogger import Keylogger
Keylogger("logs").run()
``` 
```py
# Another way to run the keylogger. 
# You can also use absolute path in `stroke_logger.dir`. ex. "C:\logs"
from keylogger import Keylogger
stroke_logger = Keylogger()
stroke_logger.dir = "keystroke-logs"
stroke_logger.run()
```
###### Run in a separate thread in another Python script
```py
# Executes the logger in a new thread without blocking the main flow of the program
import threading
from keylogger import Keylogger
threading.Thread(target=Keylogger("logs").run).start()
```
<hr>

### Notes
Feel free to contribute to fix any problems, or to submit an issue!

The program makes no attempt to hide itself.

Please note that this repository is for educational purposes only. No contributors, major or minor, are responsible for any actions made by the software.