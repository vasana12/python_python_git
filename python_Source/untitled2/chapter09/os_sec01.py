import os, time

print("os.listdir()=",os.listdir())             #현재 작업공간 파일 목록 반환
print("os.listdirr('c:/')=",os.listdir('c:/'))  #c루트 하위의 작업공간 파일 반환

path = 'C:\BigDeep\python36'
file_list = os.listdir(path)
for file in file_list:
    print("file="+file)
    file = os.path.join(path, file)
    print("file_path="+file,"\t",
          "file_size="+str(os.stat(file).st_size),"\t",
          "file_time="+time.ctime(os.stat(file).st_mtime))
