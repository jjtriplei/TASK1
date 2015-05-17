import os

# for i in os.listdir('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids'):
#     print(i)
#     print(os.path.isdir('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\' + i))

paths = ['C:\\Users\\III\\Desktop\\Coding Lessons\\']

def print_bitch():
    print("TODAY, You're MY BITCH!")

#for p in paths:
#    for i in os.listdir(p):
#        print(i)
#        if os.path.isdir(p + i) is True:
#            print("I AM A FILE!!!! HEAR ME DO NOTHING")
#        else:
#            print("NOOOOOOOOOOOOOOOOOOOOOOOOOO!")

#for p in paths:
#    for i in os.listdir(p):
#        if os.path.isdir(p + i) is False:
#            print_bitch()
#        else:
#            print("I'm not your BITCH TODAY BEYOTCH!")

def find_files(path):
    for p in paths:
        for i in os.listdir(p):
            if os.path.isdir(p + i) is False:
                print(p + "\\" + i)
#                print_bitch()
            else:
                files(p + i + "\\")

def files(folder):
#    print(folder)
    for i in os.listdir(folder):
        if os.path.isdir(folder + i) is False:
#            if i.lower().endswith('.py'):
#                print(folder + i)
            if ".py" in i:
                print(folder + i)
        else:
            files(folder + i + "\\")
