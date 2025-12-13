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
        if sum/len(self.marks) > 50:
            return True
        else:
            return False

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library elements:\nCity: {self.city}\nStreet: {self.street}\nZip code: {self.zip_code}\nOpen-hours: {self.open_hours}\nPhone: {self.phone}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee elements:\nFirst Name: {self.first_name}\nLast name: {self.last_name}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\nCity: {self.city}\nStreet: {self.street}\nZip code: {self.zip_code}\n Phone: {self.phone}'

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library #obiekt
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book elements:\n{self.library.__str__()}\nPublication Date: {self.publication_date}\n Author: {self.author_name} {self.author_surname}\n Number of Pages: {self.number_of_pages}'

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee #obiekt
        self.student = student #obiekt
        self.books = books #obiekt
        self.order_date = order_date

    def __str__(self):
        return f'Order elements:\n{self.employee.__str__()}\n{self.student.__str__()}\n{self.books.__str__()}\nOrder Date: {self.order_date}'

library1 = Library('city1', 'street1', 'zip_code1', 'open_hours1', 'phone1')
library2 = Library('city2', 'street2', 'zip_code2', 'open_hours2', 'phone2')

book1 = Book(library1, 'publication_date1', 'author_name1', 'author_surname1', 'number_of_pages1')
book2 = Book(library2, 'publication_date2', 'author_name2', 'author_surname2', 'number_of_pages2')
book3 = Book(library2, 'publication_date3', 'author_name3', 'author_surname3', 'number_of_pages3')
book4 = Book(library2, 'publication_date4', 'author_name4', 'author_surname4', 'number_of_pages')
book5 = Book(library1, 'publication_date5', 'author_name5', 'author_surname5', 'number_of_pages')

employee1 = Employee('John', 'Smith', '1999', '12-12-22', 'City1', 'street1', 'zip_code1', 'phone1')
employee2 = Employee('Ann', 'Stark', '1998', '12-12-22', 'City2', 'street2', 'zip_code2', 'phone2')
employee3 = Employee('Ben', 'Mark', '1997', '12-12-22', 'City2', 'street2', 'zip_code2', 'phone2')

student1 = Student("No name", [10, 20])
student2 = Student("No name2", [10, 20])

order1 = Order(employee1, student1, book1, '1999-12-22')
order2 = Order(employee2, student2, book3, '1999-12-22')

print(order1.__str__())
print(order2.__str__())

