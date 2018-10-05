L=[1,2,3]
def func1():
    try:
        num=L[0]
    except IndexError:
        print('IndexError')
    else:
        print('Keep calm and go ahead')

if __name__=='__main__':
    func1()


