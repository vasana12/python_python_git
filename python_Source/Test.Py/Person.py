class Person:
    def __init__(self, name,age):
        self.name =name
        self.age = age

    def PersonInfo(self):
        return self.name + " : (age::"+str(self.age)+")"

class Student(Person):
    def __init__(self, name,age,grade):
        Person.__init__(self, name, age)
        self.grade =grade
    def GetStudent(self):
        return self.PersonInfo()+", grade:"+str(self.grade)

'''class Student(Person):
    def__init__(self, name, age, grade):
        super().__init__(name,age) #Person.__init__(self.name, age)
        self.grade = grade
    def GetStudent(self):
        return super().PersonInfo() +", grade:" +str(self.grade)'''
if __name__=='__main__':

    x= Person("Dominica", 12)
    y= Student("Ruri", 7, 3)
    y.name = '이기자'
    y.age = '10'
    print(x.PersonInfo())
    print(y.PersonInfo())
    print(y.GetStudent())