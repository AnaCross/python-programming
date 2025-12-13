class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name} has {self.marks} marks'

    def is_passed(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        if sum / len(self.marks) > 50:
            return True
        else:
            return False
