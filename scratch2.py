import os

paths = 'C:\\Users\\III\\Desktop\\Coding Lessons\\'

for root, dirs, files in os.walk(paths):
    for file in files:
        if file.lower().endswith('.py'):
            print(file)
