class Test:
    def empty(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)

if __name__ == '__main__':
    my01=Test()
    my02=my01
    my03=Test()
    my01.empty()
    my03.empty()
    for i in range(1,6):
        my01.add(i)
    print(my01.data)
    print(my02.data)