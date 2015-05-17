paths = []
garbage_folder = []

import os

# Because I assumed you were going to put multiple paths in the paths variable, 
# I had to define two seperate functions for looking through folders. When I tried
# doing this with just the one function, the program lost it's mind.

def find_files_to_remove(path):
	for path in paths:
		for item in os.listdir(path):
			if os.path.isdir(path + item) is False:
				check_file()
			else:
				search_subfolders(path + item + "\\")

def search_subfolders(folder):
	for item in os.listdir(folder):
			if os.path.isdir(folder + item) is False:
				check_file()
			else:
				search_subfolders(folder + item + "\\")

def check_file(file):
	if item.lower().endswith('.nfo'):
		# MARK THAT BITCH FOR REMOVAL
		pass
	elif "sample" in i
	
# ---------------------------------------------
# SIIIIIIIIIIGH!! practice with os.walk()
# ---------------------------------------------
# import os
# for root, dirs, files in os.walk("/mydir"):
#     for file in files:
#         if file.endswith(".txt"):
#              print(os.path.join(root, file))
# ---------------------------------------------
def find_files_to_remove(path)
	for root, dirs, files in os.walk(path):
	    for file in files:
	        if file.lower().endswith('.py'):
	            print(file)