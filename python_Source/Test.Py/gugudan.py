num1=int(input("첫번째 숫자를 입력하세요=>"))
num2=int(input("두번째 숫자를 입력하세요=>"))

if num1>num2:
    max_num=num1
    min_num=num2
else:
    max_num=num2
    min_num=num1

print()
for dan in range(min_num, max_num+1):
    print(" ** %d단 ** " % dan, end="")
print()
for i in range(1,10):
    for dan in range(min_num,max_num+1):
        print("%d * %d = %2d "  %(dan, i, dan*i),end="")
    print()

