class Person:
    def __init__(self, name, age):
        Person.name =name
        Person.age = age
    def aboutPerson(self):
        print("name :"+self.name+",age: " + str(Person.age))
    def __del__(self):
        print("call del")

if __name__ == "__main__":
    objectPerson = Person("Dominica", 20)
    objectPerson.aboutPerson()
