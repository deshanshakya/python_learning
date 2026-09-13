class Student:


    # adding the __init__() method
    def __init__(self, name, score):
       self.name = name
       self.score = score


    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student('Harry', 85)

# calling this method using student1
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)