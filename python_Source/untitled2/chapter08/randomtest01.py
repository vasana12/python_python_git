from random import*

seed(3)         #동일한 값의 난수가 나오게 함, seed 가 없는 경우 seed 는 시스템 시간 값을 사용하기 때문에 계속 바뀜
print(random()) #0.0~1.0 사이의 float 값을 리턴
print(uniform(1,100)) #1~100 사이의 임의의 float 값 리턴
print(randint(1,100)) #1~100 사이의 int 값을 리턴
print(choice("12345678900abcdefghij")) #요소중 하나의 요소만 리턴
sample_list =["python", "java", "c++", "random", "spring"]
print(sample_list)
shuffle(sample_list)
print(sample_list)
