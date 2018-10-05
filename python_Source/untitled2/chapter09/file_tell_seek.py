f= open('text.txt', 'r', encoding='utf-8')
print('파일 현재 위치:', f.tell()) #tell() : 현재 위치 구함
print(f.read())
print('파일 현재 위치:', f.tell())
print()
f.seek(0) #처음으로. seek() : 파라메터로 주어진 값의 위치로 이동
print('파일의 현재 위치:', f.tell())
print(f.readline(), end="")
print('파일 현재 위치:', f.tell())
f.close()