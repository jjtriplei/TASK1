paths = ['C:\\Users\\III\\Desktop\\Coding Lessons\\']
garbage_folder = []

import os

def find_files_to_remove(path):
    for path in paths:
        for item in os.listdir(path):
            if os.path.isdir(path + item) is False:
                check_file(item)
            else:
                search_subfolders(path + item + "\\")

def search_subfolders(folder):
    for item in os.listdir(folder):
        if os.path.isdir(folder + item) is False:
            check_file(item)
        else:
            search_subfolders(folder + item + "\\")

def check_file(file):
    if file.lower().endswith('.py'):
        print(file)

def find_files_to_remove2(path):
    for path in paths:
        for root, dirs, files in os.walk(path):
	    for file in files:
	        if file.lower().endswith('.py'):
	            print(file)
