import Items.Library as Library


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library  # object
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Book elements:'
                f'\n{self.library.__str__()}'
                f'\nPublication Date: {self.publication_date}'
                f'\n Author: {self.author_name} {self.author_surname}'
                f'\n Number of Pages: {self.number_of_pages}')
