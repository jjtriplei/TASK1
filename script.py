paths = []
garbage_folder

import os

# Because I assumed you were going to put multiple paths in the paths variable, 
# I had to define two seperate functions for looking through folders. When I tried
# doing this with just the one function, the program lost it's mind.

def find_files_to_remove(path):
	for p in paths:
		for i in os.listdir(p):
			if os.path.isdir(p + i) is False:
				check_file()
			else:
				search_subfolders(p + i + "\\")

def search_subfolders(folder):
	for i in os.listdir(folder):
			if os.path.isdir(folder + i) is False:
				check_file()
			else:
				search_subfolders(folder + i + "\\")

# ---------------------------------------------
# SIIIIIIIIIIGH!! practice with os.walk()
# ---------------------------------------------
# import os
# for root, dirs, files in os.walk("/mydir"):
#     for file in files:
#         if file.endswith(".txt"):
#              print(os.path.join(root, file))
# ---------------------------------------------

def check_file(file):
	if i.lower().endswith('.nfo'):
		# MARK THAT BITCH FOR REMOVAL
		pass
	elif "sample" in i
	
