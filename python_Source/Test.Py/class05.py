class Num:
    def __init__(self,num):
        self.num =num
    def __add__(self, num):
        self.num +=num
    def __sub__(self, num):
        self.num -=num

if __name__=='__main__':
    n=Num(100)
    print(n.num)
    n+100
    print(n.num)
    n-100
    print(n.num)