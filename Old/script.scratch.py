path_list = 'D:\\'
file_type = ['.exe','.bk2']

import os

#def find_files_to_remove(path_list):
#    for paths in path:
for root, dirs, files in os.walk(path_list):
    for filename in files:
        for f_type in file_type:
            if filename.lower().endswith(f_type):
                #print(root + " \ " + filename)
                #print(filename)
                #print(os.path.getsize(os.path.join(root,filename)))
                if os.path.getsize(os.path.join(root,filename)) > 50000000:
                    print(filename)
            #elif "sample" in filename:
                #print(root + " \ " + filename)
                #print(filename)
