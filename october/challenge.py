import sys
import csv

class csv_file_manipulator():

    def __init__(self, args):
        self.command_processor = {'--file' : self.process_input_file,
                                  '--getline' : self.process_getline,
                                  '--output-file' : self.process_output_file}
        self.arguments = args
        self.current_argument_idx = 1
        self.csv_data = []

    def process_task(self):
        
        self.current_argument_idx = 1
    
        while self.current_argument_idx < len(self.arguments):
            current_argument = self.arguments[self.current_argument_idx]

            if current_argument in self.command_processor:
                self.command_processor[current_argument]()
            else:
                self.process_unknown_argument()

    def process_input_file(self):
        print('entering proc...')
        self.current_argument_idx += 1
        file_name = self.arguments[self.current_argument_idx]
        print('input file: {}'.format(file_name))
        with open(file_name, 'r') as csv_file:
            self.csv_data = list(csv.reader(csv_file, delimiter=','))

        print(self.csv_data)
        self.current_argument_idx += 1

    def process_output_file(self):
        print('outputting file...')
        self.current_argument_idx += 1
        file_name = self.arguments[self.current_argument_idx]
        print('output file: {}'.format(file_name))
        with open(file_name, 'w', newline='') as write_file:
            file_writer = csv.writer(write_file)
            file_writer.writerows(self.csv_data)

        print(self.csv_data)
        self.current_argument_idx += 1

    def process_getline(self):
        self.current_argument_idx += 1
        line_number = int(self.arguments[self.current_argument_idx])
        print('getting line {} containing data: ({})'.format(line_number
                                                             , self.csv_data[line_number]))
        self.csv_data = [self.csv_data[line_number]]

    def process_unknown_argument(self):
        print('Unknown command: {}'.format(self.arguments[self.current_argument_idx]))
        self.current_argument_idx += 1

manipulator = csv_file_manipulator(sys.argv)
manipulator.process_task()
