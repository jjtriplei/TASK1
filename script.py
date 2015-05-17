path_list = []
file_types = []
file_size_in_MB =
mbs_in_bytes = 1024 * 1024

marked_files = []
files_to_delete = []
files_to_move = []

move_files_to_destination = []

import os
import shutil

def find_files_to_remove(path_list):
    for paths in path_list:
        for root, dirs, files in os.walk(paths):
		    for filename in files:
		       	for f_type in file_types:
					if filename.lower().endswith(f_type):
				    	marked_files.append(os.path.join(root,filename))
				if "sample" in filename:
			        if os.path.getsize(os.path.join(root,filename)) > file_size_in_MB * mbs_in_bytes
			       	marked_files.append(os.path.join(root,filename))

# Copy files:

for marked_file in marked_files:
	shutil.copy2(marked_file, move_files_to_destination)

# Move files:
def function(self):
	pass