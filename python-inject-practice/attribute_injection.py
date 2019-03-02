import inject


class DatabaseClient:
    """Theoretical client for database."""
    data = {}

    def get(self, key: str):
        return self.data.get(key)

    def save(self, key: str, value: all):
        self.data.setdefault(key, value)


class User:

    client = inject.attr(DatabaseClient)

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
    binder.bind(DatabaseClient, DatabaseClient())


# configure our injection with the database config
inject.configure(db_config)

user = User('john')
assert user.data['username'] == 'john'
