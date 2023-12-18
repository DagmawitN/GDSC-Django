class Book :
    def __init__ (self , title,author,ISBN , availability_status ):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = availability_status
        def display_book_detail(self):
            return (f'Title : {self.title} \nAuthor : {self.author} \nISBN : {self.ISBN} ')
        def update_availability(self):
            pass
class User:
    def __init__(self,user_id , name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []
    def user_details (self):
        return (f'User Data \nName : {self.name} \nID : {self.user_id} \nBorrowed book : {self.books_borrowed}')
    def borrowing(self,book):
        if book.availability_status:
            self.books_borrowed.append(book.title)
            book.update_availability(False)
            print("Book borrowed successfully")
        else :
            print("Book not available")
    def returning(self,book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_availability(True)
            print ("Book returned successfully")
        else:
            print("Book not borrowed")
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transaction = []
    def add_books(self,book):
        self.books.append(book)
    def register(self,user):
        self.users.append(user)
    def borrow_book(self, user_id, book_title):
        user = self.find_user(user_id)
        book = self.find_book(book_title)
        if user and book:
            user.borrow_book(book)
            transaction = Transaction(user, book, "Borrowed")
            self.transactions.append(transaction)

    def return_book(self, user_id, book_title):
        user = self.find_user(user_id)
        book = self.find_book(book_title)
        if user and book:
            user.return_book(book)
            transaction = Transaction(user, book, "Returned")
            self.transactions.append(transaction)

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print("User with ID '{user_id}' not found.".format(user_id))
        return None

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
        print("Book with title '{book_title}' not found.".format(book_title))
        return None

class Transaction:
    def __init__ (self, user, book, action):
        self.user = user
        self.book = book
        self.action = action
    def display_details(self):
        print("User ID:", self.user.user_id)
        print("User Name:", self.user.name)
        print("Book Title:", self.book.title)
        print("Action:", self.action)
