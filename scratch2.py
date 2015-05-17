path_list = ['C:\Users\III\Desktop\Coding Lessons']
file_type = ['.py']
file_size_in_MB = 50

marked_files = []
files_to_delete = []
files_to_move = []

move_files_to_destination = 'C:\Users\III\Desktop\Python move'

def find_file_types(filename):
    if filename.lower().endswith(f_type):
        print(filename)

import os
import shutil

for path in path_list:
    for root, dirs, files in os.walk(path):
        for filename in files:
            for f_type in file_type:
                f_type.find_file_types()
