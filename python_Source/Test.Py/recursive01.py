def sum_n(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return sum_n(n-1)+sum_n(n-2)

if __name__=='__main__':
    for i in range(0,10):
        print(sum_n(i),end=" ")
