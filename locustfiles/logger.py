import datetime


class Logger():
    log = True

    def __init__(self, wanna_log = log):
        self.wanna_log = wanna_log

    def log_value(self, text):
        if self.wanna_log:
            print(text)