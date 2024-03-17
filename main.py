import book_management
import user_management
import checkout_management

def print_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout Book")
    print("4. Check-in Book")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def manage_books(book_manager):
    while True:
        print("\nManage Books")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            # Check if the book with the given ISBN already exists
            if book_manager.is_isbn_unique(isbn):
                book_manager.add_book(title, author, isbn)
                print("Book added successfully.")
            else:
                print("A book with this ISBN already exists.")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep unchanged): ")
            author = input("Enter new author (leave blank to keep unchanged): ")
            # Proceed with update if the book exists
            if book_manager.does_book_exist(isbn):
                updated = book_manager.update_book(isbn, title if title else None, author if author else None)
                if updated:
                    print("Book updated successfully.")
                else:
                    print("Another book with the same title or author already exists.")
            else:
                print("Book not found.")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            if book_manager.delete_book(isbn):
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        elif choice == '4':
            book_manager.list_books()
        elif choice == '5':
            attribute = input("Search by (title/author/isbn): ")
            value = input(f"Enter {attribute}: ")
            if not book_manager.search_books(attribute, value):
                print("No books found.")
        elif choice == '6':
            break

def manage_users(user_manager):
    while True:
        print("\n Manage Users")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Search Users")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            print("User added successfully.")
        elif choice == '2':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name: ")
            updated = user_manager.update_user(user_id, name)
            if updated:
                print("User updated successfully.")
            else:
                print("User not found.")
        elif choice == '3':
            user_id = input("Enter user ID of the user to delete: ")
            if user_manager.delete_user(user_id):
                print("User deleted successfully.")
            else:
                print("User not found.")
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            attribute = input("Search by (name/user_id): ")
            value = input(f"Enter {attribute}: ")
            if not user_manager.search_users(attribute, value):
                print("No users found.")
        elif choice == '6':
            break

def log_operation(operation):
    with open("library_log.txt", "a") as log_file:
        log_file.write(f"{operation}\n")

def main():
    bm = book_management.BookManagement()
    um = user_management.UserManager()
    cm = checkout_management.CheckoutManager(bm, um)

    while True:
        choice = print_menu()

        if choice == '1':
            manage_books(bm)
        elif choice == '2':
            manage_users(um)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            if cm.checkout_book(user_id, isbn):
                print("Book checked out successfully.")
            else:
                print("Failed to checkout book. It might be already checked out or does not exist.")
        elif choice == '4':
            isbn = input("Enter ISBN of the book to check-in: ")
            if cm.checkin_book(isbn):
                print("Book checked in successfully.")
            else:
                print("Failed to check in book. It might not be checked out or does not exist.")

        elif choice == '5':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")
        

if __name__ == "__main__":
    main()
