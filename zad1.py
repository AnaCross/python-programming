class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        if sum / len(self.marks) > 50:
            return True
        else:
            return False


student1 = Student("John", [89, 78, 45, 67])
print(student1.is_passed())

student2 = Student("Ann", [12, 20, 45, 67])
print(student2.is_passed())
