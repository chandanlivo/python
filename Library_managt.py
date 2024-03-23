class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f'The no of books are {self.noBooks} || And the books are: ')
        for books in self.books:
            print(books)

l1 = Library()
l1.addBook('Atomic Habits')
l1.addBook('Bhagavadhgitha')
l1.showInfo()