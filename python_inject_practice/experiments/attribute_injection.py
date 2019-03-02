import inject
from python_inject_practice.core.database import Database


class User:

    client = inject.attr(Database)

    def __init__(self, username: str):
        self.username = username
        self.client.save(username, {
            'username': username
        })

    @property
    def data(self):
        return self.client.get(self.username)

    def update_user(self, data: dict):
        self.client.save(self.username,
                        self.client.get(self.username).update(data))


# Configuration for database binding
def db_config(binder):
    # define a single instance of the database to use here
    binder.bind(Database, Database())


# configure our injection with the database config
inject.configure(db_config)

user = User('john')
assert user.data['username'] == 'john'
