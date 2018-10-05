#-*-coding:utf8 -*-

def repeat_msg(msg,repeat=3):
    for i in range(repeat):
        print(msg)

if __name__=='__main__':
    repeat_msg('Hello')
    print("---------------")
    repeat_msg('Hello',2)
    print("---------------")
    repeat_msg('Hi',repeat=5)# repeat_msg('Hi',5)
                             #키워드 문자

def circle_area(radius, pi):
    area = pi*(radius**2)
    return area
if __name__ == "__main__":
    print("반지름:",3,"면적:",circle_area(3,3.14))
    print("반지름:",3, "면적:",circle_area(3,pi=3.14))
    print("반지름:",3,"면적:",circle_area(pi=3.14,radius=3))
