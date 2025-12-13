import People.Employee as Employee
import People.Student as Student
import Items.Book as Book


class Order:
    def __init__(self, employee: Employee, student: Student, book: Book, order_date):
        self.employee = employee  # object
        self.student = student  # object
        self.book = book  # object
        self.order_date = order_date

    def __str__(self):
        return (f'Order elements:'
                f'\n{self.employee.__str__()}'
                f'\n{self.student.__str__()}'
                f'\n{self.book.__str__()}'
                f'\nOrder Date: {self.order_date}')
