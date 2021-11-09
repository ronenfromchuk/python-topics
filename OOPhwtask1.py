# Object Oriented Programming
# task1

class Book():
    pass

def create_book(title, author, genre, year_of_publish, no_of_pages):
    book = Book()
    book.title = title
    book.author = author
    book.genre = genre
    book.year_of_publish = year_of_publish
    book.no_of_pages = no_of_pages
    return book

_book = create_book('rich dad, poor dad', 'Robert Kiyosaki', 'Finance Education', 2000, 336)
print(_book)

_book_one = Book()
_book_one.__dict__['title'] = 'rich dad, poor dad'
_book_one.__dict__['author'] = 'Robert Kiyosaki'
_book_one.__dict__[' genre'] = 'Finance Education'
_book_one.__dict__['year_of_publish'] = 2000
_book_one.__dict__['no_of_pages'] = 336
print(_book_one.__dict__)

_book_two = Book()
_book_two.title = 'rich dad, poor dad'
_book_two.author = 'Robert Kiyosaki'
_book_two.genre = 'Finance Education'
_book_two.year_of_publish = 2000
_book_two.no_of_pages = 336
print(_book_two.title)
print(_book_two.author)
print(_book_two.genre)
print(_book_two.year_of_publish)
print(_book_two.no_of_pages)
