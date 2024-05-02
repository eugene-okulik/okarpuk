class Book:
    pages_material = 'paper'
    has_text = True

    def __init__(self, book_name, book_author, book_pages_qty, book_isbn, is_reserved):
        self.book_name = book_name
        self.book_author = book_author
        self.book_pages_qty = book_pages_qty
        self.book_isbn = book_isbn
        self.is_reserved = is_reserved


class SchoolBook(Book):
    def __init__(self, book_name, book_author, book_pages_qty, book_isbn, is_reserved, subject, study_year, has_tasks):
        super().__init__(book_name, book_author, book_pages_qty, book_isbn, is_reserved)
        self.subject = subject
        self.study_year = study_year
        self.has_tasks = has_tasks


first_book = Book('1984', 'George Orwell', 311, 111111, True)
second_book = Book('The Complete Robot', 'Isaac Asimov', 226, 222222, False)
third_book = Book('Childhoods End', 'Arthur Clarke', 351, 333333, False)
fourth_book = Book('The Time Machine', 'Herbert Wells', 127, 444444, False)
fifth_book = Book('Dune', 'Frank Herbert', 433, 555555, False)

books = [first_book, second_book, third_book, fourth_book, fifth_book]

for book in books:
    if book.is_reserved:
        print(f'Book name: {book.book_name}, Book author: {book.book_author}, '
              f'Pages quantity: {book.book_pages_qty}, Pages material: {Book.pages_material}, RESERVED')
    else:
        print(f'Book name: {book.book_name}, Book author: {book.book_author}, '
              f'Pages quantity: {book.book_pages_qty}, Pages material: {Book.pages_material}')


first_school_book = SchoolBook('Organic chemistry', 'Ivanov', 222, 666666,
                               True, 'Chemistry', 10, True)

second_school_book = SchoolBook('Geometry', 'Petrov', 500, 777777, False,
                                'Math', 7, False)

third_school_book = SchoolBook('Botanica', 'Sidiriv', 400, 888888,
                               False, 'Biology', 8, False)

school_books = [first_school_book, second_school_book, third_school_book]

for book in school_books:
    if book.is_reserved:
        print(f'Book name: {book.book_name}, Book author: {book.book_author}, '
              f'Pages quantity: {book.book_pages_qty}, Subject: {book.subject}, Study year: {book.study_year}, '
              f'RESERVED')
    else:
        print(f'Book name: {book.book_name}, Book author: {book.book_author}, '
              f'Pages quantity: {book.book_pages_qty}, Subject: {book.subject}, Study year: {book.study_year}')
