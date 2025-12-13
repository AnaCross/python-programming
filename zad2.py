import People.Student as Student
import People.Employee as Employee
import Items.Library as Library
import Items.Book as Book
import Event.Order as Order


library1 = Library.Library('city1', 'street1', 'zip_code1', 'open_hours1', 'phone1')
library2 = Library.Library('city2', 'street2', 'zip_code2', 'open_hours2', 'phone2')

book1 = Book.Book(library1, 'publication_date1', 'author_name1', 'author_surname1', 'number_of_pages1')
book2 = Book.Book(library2, 'publication_date2', 'author_name2', 'author_surname2', 'number_of_pages2')
book3 = Book.Book(library2, 'publication_date3', 'author_name3', 'author_surname3', 'number_of_pages3')
book4 = Book.Book(library2, 'publication_date4', 'author_name4', 'author_surname4', 'number_of_pages')
book5 = Book.Book(library1, 'publication_date5', 'author_name5', 'author_surname5', 'number_of_pages')

employee1 = Employee.Employee('John', 'Smith', '1999', '12-12-22', 'City1', 'street1', 'zip_code1', 'phone1')
employee2 = Employee.Employee('Ann', 'Stark', '1998', '12-12-22', 'City2', 'street2', 'zip_code2', 'phone2')
employee3 = Employee.Employee('Ben', 'Mark', '1997', '12-12-22', 'City2', 'street2', 'zip_code2', 'phone2')

student1 = Student.Student("No name", [10, 20])
student2 = Student.Student("No name2", [10, 20])

order1 = Order.Order(employee1, student1, book1, '1999-12-22')
order2 = Order.Order(employee2, student2, book3, '1999-12-22')

print(order1.__str__())
print(order2.__str__())
