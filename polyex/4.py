from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}.'

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")

class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"

dog = Dog("Buddy", 3, "Male")
cat = Cat("Misty", 2, "Female")
kitten = Kitten("Lily", 1)
tomcat = Tomcat("Tom", 4)

print(dog)
print(dog.make_sound())
print(cat)
print(cat.make_sound())
print(kitten)
print(kitten.make_sound())
print(tomcat)
print(tomcat.make_sound())