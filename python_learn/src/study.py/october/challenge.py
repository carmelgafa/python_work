"""October Challenge study.py"""
import sys
import csv
import urllib.request
import io

class FileManipulator():
    """class to manipulate commandline commands related to csv files"""

    def __init__(self, args):
        """init method - initializes variables"""
        # maps command to method processing it
        self.command_processor = {'--file' : self.__process_input_file,
                                  '--get-line' : self.__process_getline,
                                  '--output-file' : self.__process_output_file,
                                  '--merge-files' : self.__process_merge_files,
                                  '--remove-line' : self.__process_remove_line,
                                  '--filter' : self.__process_filter,
                                  '--http-get-file' : self.__process_http_get_file}
        # the arguments
        self.arguments = args
        # index of the current argument
        self.current_argument_idx = 1
        # data
        self.csv_data = []

    def process_task(self):
        """entry method"""
        # start with the first arguemnt
        self.current_argument_idx = 1

        # for all arguments
        # pass processing to relevant method
        while self.current_argument_idx < len(self.arguments):
            current_argument = self.arguments[self.current_argument_idx]
            if self.__is_current_arg_command():
                self.command_processor[current_argument]()
            else:
                self.__process_unknown_argument()

    # processing methods

    def __process_input_file(self):
        """processing of reading a csv file file"""
        file_name = self.__get_next_argument()
        print('input file: {}'.format(file_name))
        self.__read_data(file_name)
        print(self.csv_data)
        self.current_argument_idx += 1

    def __process_output_file(self):
        """process of writing a csv file"""
        file_name = self.__get_next_argument()
        print('output file: {}'.format(file_name))
        self.__write_data(file_name)
        print(self.csv_data)
        self.current_argument_idx += 1

    def __process_getline(self):
        """gets a single line from the data: data is set to that line"""
        line_number = int(self.__get_next_argument())
        print('getting line {} containing data: ({})'.format(line_number
                                                             , self.csv_data[line_number]))
        self.csv_data = [self.csv_data[line_number]]

    def __process_merge_files(self):
        """process to merge a number of csv files"""
        args = self.__get_argument_list()
        print(args)
        for arg in args:
            self.__read_data(arg)

    def __process_remove_line(self):
        """process to remove a line from data"""
        line_number = int(self.__get_next_argument())
        del self.csv_data[line_number]

    def __process_filter(self):
        """process that filters data containing some parameter. data is now filtered data"""
        filter_argument = self.__get_next_argument()
        print('filter argument: {}'.format(filter_argument))
        filtered_list = []
        for sublist in self.csv_data:
            for items in sublist:
                if filter_argument in items:
                    filtered_list.append(sublist)
                    break
        self.csv_data = filtered_list
        self.current_argument_idx += 1

    def __process_http_get_file(self):
        """process that gets csv data from url"""
        url_argument = self.__get_next_argument()
        print('reading url {}'.format(url_argument))
        webpage = urllib.request.urlopen(url_argument)
        datareader = csv.reader(io.TextIOWrapper(webpage))
        self.csv_data = list(datareader)
        self.current_argument_idx += 1

    def __process_unknown_argument(self):
        """process that informs user taht an unkown command has been issued"""
        print('Unknown command: {}'.format(self.arguments[self.current_argument_idx]))
        self.current_argument_idx += 1

    # helper methods

    def __get_next_argument(self):
        """gets the next argument in the ragument list"""
        self.current_argument_idx += 1
        return self.__get_current_argument()

    def __get_current_argument(self):
        """Gets the current argument in the argument list"""
        return self.arguments[self.current_argument_idx]

    def __is_current_arg_command(self):
        """true if the current argument is a command"""
        return self.__get_current_argument() in self.command_processor

    def __read_data(self, filename):
        """reads data from a csv file"""
        with open(filename, 'r') as csv_file:
            self.csv_data = self.csv_data + list(csv.reader(csv_file, delimiter=','))

    def __write_data(self, filename):
        """writes data fo a csv file"""
        with open(filename, 'w', newline='') as write_file:
            file_writer = csv.writer(write_file)
            file_writer.writerows(self.csv_data)

    def __is_next_arg_command(self):
        """true if next argument is a command"""
        return self.arguments[self.current_argument_idx + 1] in self.command_processor

    def __get_argument_list(self):
        """ get a list of arguments following current argument that are not commands
            used when a number of parameters follow a command"""
        args = []
        while not self.__is_next_arg_command():
            args.append(self.__get_next_argument())

        self.current_argument_idx += 1
        return args

manipulator = FileManipulator(sys.argv)
manipulator.process_task()
