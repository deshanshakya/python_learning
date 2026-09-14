# Animal is a parent class
class Animal:
    def eat(self):
        print("I can eat")

# making a Dog class that is derived from Animal class
class Dog(Animal):
    def bark(self):
        print("I can bark")

#making a Cat class that is derived from Animal Class
class Cat(Animal):
    def get__grumpy(self):
        print("i am getting grumpy")

#creating a object from Dog class
dog1 = Dog()

#calling the bark() method from Dog class
dog1.bark()

#calling the eat() function from the Animal parent class
dog1.eat()

#creating a objecy from Cat class
cat1 = Cat()
 #calling the function from Animal class again
cat1.eat()
cat1.get__grumpy()