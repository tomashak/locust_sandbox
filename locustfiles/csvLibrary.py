import csv


class csvLibrary(object):
    '''Documentation for csvLibrary.

        It is used for reading from CSV (comma-separated values) files
        which is used for storing tabular data (numbers and text) in plain text
    '''

    def read_csv_file(self, filename, selector):
        '''This creates a keyword named "Read CSV File"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        '''
        data = []
        with open(filename, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if selector in str(row):
                    data.append(row)
        return data

    def read_csv_file_two_select(self, filename, selector1, selector2):
        '''This creates a keyword named "Read CSV File"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        '''
        data = []
        with open(filename, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                if selector1 in str(row) and selector2 in str(row):
                    data.append(row)
        return data


    def read_csv_file_all_rows(self, filename):
        '''This creates a keyword named "Read CSV File All Rows"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        '''
        data = []
        i = 0
        with open(filename, 'rt') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if i != 0:
                    data.append(row)
                i = i + 1
        return data;
