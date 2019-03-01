import inject


class Database:
    """Some theoretical database provider."""
    cached = {}

    def get(self, key):
        return self.cached.get(key)

    def save(self, key, value):
        self.cached.setdefault(key, value)


def save_user_age(name, age):
    db = inject.instance(Database)
    db.save(name, age)


def get_user_age(name):
    db = inject.instance(Database)
    return db.get(name)


# Configuration for database binding
def db_config(binder):
    binder.bind(Database, Database())


inject.configure()

save_user_age('john', 10)
print(get_user_age('john'))
