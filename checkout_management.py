from storage import Storage

class CheckoutManager:
    def __init__(self, book_manager, user_manager):
        self.storage = Storage('checkouts.json')
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = self.load_checkouts()

    def checkout_book(self, user_id, isbn):
        for book in self.book_manager.books:
            if book.isbn == isbn and not book.is_checked_out:
                book.is_checked_out = True
                self.checkouts.append({"user_id": user_id, "isbn": isbn})
                self.book_manager.save_books()
                self.save_checkouts()
                return True
        return False

    def checkin_book(self, isbn):
        for book in self.book_manager.books:
            if book.isbn == isbn and book.is_checked_out:
                book.is_checked_out = False
                self.checkouts = [checkout for checkout in self.checkouts if checkout['isbn'] != isbn]
                self.book_manager.save_books()
                self.save_checkouts()
                return True
        return False

    def load_checkouts(self):
        return self.storage.load_data()

    def save_checkouts(self):
        self.storage.save_data(self.checkouts)
