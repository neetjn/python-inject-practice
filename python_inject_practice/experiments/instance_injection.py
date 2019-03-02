import inject
from python_inject_practice.core.database import Database


def save_user_age(name: str, age: int):
    """Saves some user's age in our theoretical database"""
    db = inject.instance(Database)
    db.save(name, age)


def get_user_age(name: str):
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
assert get_user_age('john') == 10
