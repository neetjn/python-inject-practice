import inject


class Database:
    """Some theoretical database provider."""
    cached = {}

    def get(self, key):
        return self.cached.get(key)

    def save(self, key, value):
        self.cached.setdefault(key, value)


def save_user_age(name, age):
    """Saves some user's age in our theoretical database"""
    db = inject.instance(Database)
    db.save(name, age)


def get_user_age(name):
    """Fetch a user's age in our theoretical database"""
    db = inject.instance(Database)
    return db.get(name)


# Configuration for database binding
def db_config(binder):
    # define a single instance of the database to use here
    binder.bind(Database, Database())


# configure our injection with the database config
inject.configure(db_config)

save_user_age('john', 10)
print(get_user_age('john'))
