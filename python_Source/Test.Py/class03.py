class Emp:
    empno=0
    result=0

if __name__=='__main__':
    a1=Emp()
    a1.empno = "a111"
    a1.result = 850

    a2 =Emp()
    a2.empno ="b111"
    a2.result =750

    a3=Emp()
    a3.empno ="c111"
    a3.result =650

    print("a1.result=",a1.result,end="\t")
    print("a2.result=",a2.result,end="\t")
    print("a3.result=",a3.result,end="")

    print(a2.__class__.result) #0을 출력
    print(a3.__class__.result) #0을 출력
    print(Emp.result) #0을 출력
    print("="*50)

    a1.__class__.result=100;
    print(a2.__class__.result) #1000을 출력
    print(a3.__class__.result) #1000을 출력
    print(Emp.result) # 1000을 출력
    a4=Emp()
    print(a4.result) #1000을 출력

    print("=" * 50)
    print(Emp.__class__)
    print(Emp.__class__.__name__)
    print(a1.__class__)
    print(a1.__class__.__name__)
