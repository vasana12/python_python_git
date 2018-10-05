pi= 3.141592

def circle_area_with_pi(r): #r은 지역변수
    #circle_area_wiht_pi의 local 영역
    global pi
    pi=3.14
    result =pi*(r**2)   #local 변수 pi,r 사용
    return result

def circle_area_without_pi(r):
    #circle_area_without_pi의 local 영역
    result =pi * (r**2)
    return result
def sum_area():
    result =[circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(result)     #bulit-in 의 sum 함수를 호출

if __name__=="__main__":
    print("PI:", pi)
    print("반지름:", 3, "면적:", circle_area_with_pi(3))
    print("반지름:",3,"면적:",circle_area_without_pi(3))
    print(sum_area())
    print(pi)