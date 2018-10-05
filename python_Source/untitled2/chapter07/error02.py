try:
    print('try-시작')
    #예외발생
    a=int('string')
    print('try-종료')
except ZeroDivisionError :
    print('0으로 나누려 했거나')
except IOError:
    print('파일이 존재하지 않습니다')
except:
    print("AAAAAA")
else:
    print('else 왔어요' )
finally:
    print('finally 왔어요')
