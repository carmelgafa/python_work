import sys
import csv
import urllib3

class csv_file_manipulator():

    def __init__(self, args):
        self.command_processor = {'--file' : self.process_input_file,
                                  '--get-line' : self.process_getline,
                                  '--output-file' : self.process_output_file,
                                  '--merge-files' : self.process_merge_files,
                                  '--remove-line' : self.process_remove_line,
                                  '--filter' : self.process_filter,
                                  '--http-get-file' : self.process_http_get_file}
        self.arguments = args
        self.current_argument_idx = 1
        self.csv_data = []

    def process_task(self):
        self.current_argument_idx = 1

        while self.current_argument_idx < len(self.arguments):
            current_argument = self.arguments[self.current_argument_idx]

            if self.__is_current_arg_command():
                self.command_processor[current_argument]()
            else:
                self.process_unknown_argument()

    def process_input_file(self):
        print('entering proc...')
        file_name = self.__get_next_argument()

        print('input file: {}'.format(file_name))

        self.__read_data(file_name)

        print(self.csv_data)
        self.current_argument_idx += 1

    def process_output_file(self):
        print('outputting file...')

        file_name = self.__get_next_argument()

        print('output file: {}'.format(file_name))

        self.__write_data(file_name)

        print(self.csv_data)
        self.current_argument_idx += 1

    def process_getline(self):

        line_number = int(self.__get_next_argument())
        print('getting line {} containing data: ({})'.format(line_number
                                                             , self.csv_data[line_number]))
        self.csv_data = [self.csv_data[line_number]]

    def process_merge_files(self):
        print('merging...')
        args = self.__get_argument_list()
        print(args)

        for arg in args:
            self.__read_data(arg)

    def process_remove_line(self):
        line_number = int(self.__get_next_argument())
        del self.csv_data[line_number]

    def process_filter(self):
        filter_argument = self.__get_next_argument()

        print('filter argument: {}'.format(filter_argument))

        filtered_list = []
        for sublist in self.csv_data:
            for items in sublist:
                if filter_argument in items:
                    filtered_list.append(sublist)
                    break
        
        self.csv_data = filtered_list

        print(filtered_list)
        self.current_argument_idx += 1

    def process_http_get_file(self):
        url_argument = self.__get_next_argument()

        data = urllib3.request.ur urlopen(url_argument)

        urllib3.connection.ur
        for line in data: # files are iterable
            print(line)
        self.current_argument_idx += 1

    def process_unknown_argument(self):
        print('Unknown command: {}'.format(self.arguments[self.current_argument_idx]))
        self.current_argument_idx += 1

    def __get_next_argument(self):
        self.current_argument_idx += 1
        return self.__get_current_argument()

    def __get_current_argument(self):
        return self.arguments[self.current_argument_idx]

    def __is_current_arg_command(self):
        return self.__get_current_argument() in self.command_processor

    def __read_data(self, filename):
        with open(filename, 'r') as csv_file:
            self.csv_data = self.csv_data + list(csv.reader(csv_file, delimiter=','))

    def __write_data(self, filename):
        with open(filename, 'w', newline='') as write_file:
            file_writer = csv.writer(write_file)
            file_writer.writerows(self.csv_data)

    def __is_next_arg_command(self):
        return self.arguments[self.current_argument_idx + 1] in self.command_processor

    def __get_argument_list(self):
        args = []
        while not self.__is_next_arg_command():
            args.append(self.__get_next_argument())

        self.current_argument_idx += 1
        return args

manipulator = csv_file_manipulator(sys.argv)
manipulator.process_task()
