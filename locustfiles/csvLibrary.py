from csv import reader
import os


class CsvLibrary:

    def __init__(self, mysql_csv, variables_csv):
        self.path_to_mysql_csv = mysql_csv
        self.path_to_variables_csv = variables_csv

    def _check_if_path_exist(self, path):
        if os.path.exists(path):
            self.path_exists = True
        else:
            self.path_exists = False

    def read_mysql_csv(self):
        data = []
        self._check_if_path_exist(self.path_to_mysql_csv)
        if self.path_exists:
            with open(self.path_to_mysql_csv, 'r') as csv_file:
                csv_reader = reader(csv_file)
                for row in csv_reader:
                    data.append(row)
                return data[1]
        else:
            print('Cesta neexistuje')

    def read_test_variable(self, number_row: int):
        data = []
        self._check_if_path_exist(self.path_to_variables_csv)
        if self.path_exists:
            with open(self.path_to_variables_csv, 'r') as csv_file:
                csv_reader = reader(csv_file)
                for row in csv_reader:
                    data.append(row)
                return data[number_row]
        else:
            print('Cesta neexistuje')

'''
csv = CsvLibrary('../csv_example/mysql.csv', '../csv_example/test_variables.csv')
csv.read_mysql_csv()
print(csv.read_test_variable(1))
'''
