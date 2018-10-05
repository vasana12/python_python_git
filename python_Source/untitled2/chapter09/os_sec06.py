import os

print(os.getcwd())  #경로 나옴
os.chdir("C:\BigDeep\python36")     #경로 변경
print(os.getcwd())
print(os.path.join(os.getcwd(),"test"))

os.chdir("C:/BigDeep")
os.mkdir(os.path.join(os.getcwd(),"test"))
print(os.listdir())

os.remove(os.path.join(os.getcwd(),"test.py"))
print(os.listdir())