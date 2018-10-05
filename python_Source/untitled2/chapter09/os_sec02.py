import os, time

file = 'C:\BigDeep\python36\python.exe'

if __name__ =='__main__':
    if os.path.isfile(file):
        a = os.path.basename(file)
        b = os.path.split(file)
        c = os.path.normpath(file)
        print(a)
        print(b)
        print(c)