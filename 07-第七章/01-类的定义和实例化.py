class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("张三",18)

print(person1.name)
print(person1.age)

person1.age = 20
print(person1.age)

print(person1.__dict__)
person1.gender = "man"
print(person1.__dict__)

print(type(person1))