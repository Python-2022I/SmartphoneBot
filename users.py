from tinydb import TinyDB, Query

db = TinyDB('users.json', indent=4)

class UserDB:
    def __init__(self):
        self.table = db.table('users')

    def add_user(self, user_id: int, first_name: str, last_name='', username=''):
        self.table.insert({
            'user_id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username
        })

    def get_user(self, user_id: int):
        User = Query()
        return self.table.search(User.user_id == user_id)

    def check_user(self, user_id: int):
        User = Query()
        return self.table.contains(User.user_id == user_id)

