import datetime
import os
import csv

class Logger:
    def __init__(self, wanna_log=True, wanna_csv=True, path_to_csv='../csv_example/log.csv'):
        self.wanna_log = wanna_log
        self.wanna_csv_log = wanna_csv
        self.path_to_csv = path_to_csv

    def log_value(self, text):
        if self.wanna_log:
            print(text)
        if self.wanna_csv_log:
            date = datetime.datetime.now()
            a = [str(date), text]
            with open(self.path_to_csv, 'a', newline='') as file:
                wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                wr.writerow(a)


logger = Logger()
logger.log_value('ahoj')