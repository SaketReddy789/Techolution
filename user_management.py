from storage import Storage
from models import User

class UserManager:
    def __init__(self):
        self.storage = Storage('users.json')
        self.users = self.load_users()

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.save_users()

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.save_users()
                return True
        return False

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                self.save_users()
                return True
        return False

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")

    def search_users(self, attribute, value):
        for user in self.users:
            if getattr(user, attribute, '') == value:
                print(f"Name: {user.name}, User ID: {user.user_id}")
                return True
        return False

    def load_users(self):
        users_data = self.storage.load_data()
        return [User(**user) for user in users_data]

    def save_users(self):
        users_data = [{'name': user.name, 'user_id': user.user_id} for user in self.users]
        self.storage.save_data(users_data)
