class Student:
    # adding a method to check pass or fail
    def check_pass_fail(self):
        if self.score>=40:
            return True
        else:
            return False
#create object
student1 = Student()
#adding attributes to the object created
student1.name = "Tommy"
student1.score = 60
#calling the check_pass_fail() method using student1 object
did_pass = student1.check_pass_fail()

print(f'Did {student1.name} pass?', did_pass)

#create object
student2 = Student()
student2.name = "haland"
student2.score = 30

#calling this method using student2 object
did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)
