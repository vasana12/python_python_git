def circle_area(r):
    result = 3.14*(r**2) #result= 3.14*(radius**2) 해도 됨 왜냐하면 radius 가 함수 밖에서 선언되어 전역변수 이기 때문임.
    return result

if __name__=='__main__':
    radius=3
    area=circle_area(radius)
    print("반지름 : %d, 면적: %.2f"%(radius,area))
