import sys
import csv

class csv_file_manipulator():

    def __init__(self, args):
        self.command_processor = {'-ifile' : self.process_input_file,
                                  '-getline' : self.process_getline,
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

        file_name = self.__get_next_argument__()
        print('input file: {}'.format(file_name))
        
        self.__read_data__(file_name)
        print(self.csv_data)

        self.current_argument_idx += 1   
 
    def process_output_file(self):
        print('outputting file...')
        
        file_name = self.__get_next_argument__()
        print('output file: {}'.format(file_name))

        self.__write_data(file_name)
        print(self.csv_data)

        self.current_argument_idx += 1   


    def process_getline(self):
        print('Hello')
        self.current_argument_idx += 1

    def process_unknown_argument(self):
        print('Unknown command: {}'.format(self.arguments[self.current_argument_idx]))
        self.current_argument_idx += 1
    



manipulator = csv_file_manipulator(sys.argv)
manipulator.process_task()