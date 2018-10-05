import os, time

file = 'C:\BigDeep\python36\python.exe'

print(os.path.getctime(file))   #파일 생성시간 - 초 단위로 나옴
print(time.ctime(os.path.getctime(file)))
print()
print( time.ctime(os.path.getatime(file)))  #액세스 시간
print(time.ctime(os.path.getmtime(file)))   #변경 시간
print(os.path.getsize(file))    #파일의 사이즈
print(os.path.splitext(file)) #파일명과 확장자 분리