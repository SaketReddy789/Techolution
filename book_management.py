from storage import Storage
from models import Book
import json

class BookManagement:
    def __init__(self):
        self.storage = Storage('books.json')
        self.books = self.load_books()

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()

    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                return True
        return False

    def delete_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self.save_books()
                return True
        return False

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Yes' if not book.is_checked_out else 'No'}")

    def search_books(self, attribute, value):
        for book in self.books:
            if getattr(book, attribute, '') == value:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                return True
        return False

    def load_books(self):
        books_data = self.storage.load_data()
        return [Book(**book) for book in books_data]

    def save_books(self):
        books_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'is_checked_out': book.is_checked_out} for book in self.books]
        self.storage.save_data(books_data)
        
    def is_isbn_unique(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return False
        return True

    def does_book_exist(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return True
        return False

    def add_book(self, title, author, isbn):
        # Assume uniqueness check is done prior
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()

    def update_book(self, isbn, title=None, author=None):
        # Additional logic to ensure updated title or author is unique
        for book in self.books:
            if book.isbn == isbn:
                if title and not self.is_title_unique(title, isbn):
                    return False
                if author and not self.is_author_unique(author, isbn):
                    return False
                book.title = title if title else book.title
                book.author = author if author else book.author
                self.save_books()
                return True
        return False

    def is_title_unique(self, title, isbn):
        for book in self.books:
            if book.title == title and book.isbn != isbn:
                return False
        return True

    def is_author_unique(self, author, isbn):
        for book in self.books:
            if book.author == author and book.isbn != isbn:
                return False
        return True
