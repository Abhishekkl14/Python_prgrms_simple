class Animal:
 def __init__(self, name, age):
     self.__name = name # private variable
     self.__age = age # private variable
 def get_name(self):
     return self.__name
 def set_name(self, name):
     self.__name = name
 def get_age(self):
     return self.__age
 def set_age(self, age):
     self.__age = age
 def sound(self): # To be overridden by subclasses
     pass
# Derived class demonstrating inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
     super().__init__(name, age)
     self.breed = breed # public variable
 # Overriding the sound method
    def sound(self):
     return "Bark"
# Demonstrating method overloading using default arguments
class Calculator:
 def add(self, a, b, c=0):
     return a + b + c
# Creating objects and demonstrating the concepts
def main():
 # Encapsulation
 animal = Animal("Elephant", 10)
 print(f"Animal Name: {animal.get_name()}, Age: {animal.get_age()}")
 animal.set_name("Lion")
 animal.set_age(5)
 print(f"Updated Animal Name: {animal.get_name()}, Age: {animal.get_age()}")

 # Inheritance
 dog = Dog("Tony", 3, "Golden Retriever")
 print(f"Dog Name: {dog.get_name()}, Age: {dog.get_age()}, Breed: {dog.breed}")
 print(f"Dog Sound: {dog.sound()}")
 # Overloading
 calc = Calculator()
 print(f"Addition (2 args): {calc.add(5, 10)}")
 print(f"Addition (3 args): {calc.add(5, 10, 15)}")
if __name__ == "__main__":
 main()
