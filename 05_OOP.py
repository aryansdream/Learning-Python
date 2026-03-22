# =========================================
# 🧠 OBJECT ORIENTED PROGRAMMING (OOP)
# =========================================


# =========================================
# 1. CLASS & OBJECT
# =========================================
class Student:
    name = "Aryan"
    age = 20

s1 = Student()
print(s1.name)


# =========================================
# 2. CONSTRUCTOR (__init__)
# =========================================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Aryan", 20)
s2 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)


# =========================================
# 3. INSTANCE METHODS
# =========================================
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Aryan", [80, 90, 85])
s1.display()
print("Average:", s1.average())


# =========================================
# 4. CLASS VARIABLES
# =========================================
class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Aryan")
print(s1.school)


# =========================================
# 5. INHERITANCE
# =========================================
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

s1 = Student("Aryan", 90)
s1.show()


# =========================================
# 6. MULTILEVEL INHERITANCE
# =========================================
class A:
    def method_a(self):
        print("A")

class B(A):
    def method_b(self):
        print("B")

class C(B):
    def method_c(self):
        print("C")

obj = C()
obj.method_a()
obj.method_b()
obj.method_c()


# =========================================
# 7. POLYMORPHISM
# =========================================
class Bird:
    def speak(self):
        print("Some sound")

class Dog:
    def speak(self):
        print("Bark")

def make_sound(animal):
    animal.speak()

make_sound(Bird())
make_sound(Dog())


# =========================================
# 8. ENCAPSULATION
# =========================================
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())


# =========================================
# 9. ABSTRACTION
# =========================================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print("Area:", c.area())


# =========================================
# 10. MAGIC METHODS (BONUS)
# =========================================
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(5)
n2 = Number(10)

print(n1 + n2)


# =========================================
# 🎯 END OF OOP
# =========================================