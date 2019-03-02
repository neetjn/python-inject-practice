import inject
from python_inject_practice.core.database import Database


@inject.params(client=Database)
def set_user(username: str, value: all, client: Database=None):
    return client.save(username, value)


@inject.params(client=Database)
def get_user(username: str, client: Database=None):
    return client.get(username)


@inject.autoparams()
def set_user_auto(username: str, value: all, client: Database=None):
    return client.save(username, value)


@inject.autoparams()
def get_user_auto(username: str, client: Database=None):
    return client.get(username)


# Configuration for database binding
def db_config(binder):
    # define a single instance of the database to use here
    binder.bind(Database, Database())


# configure our injection with the database config
inject.configure(db_config)

# experiment with params inject
set_user('john', 1)
assert get_user('john') == 1
# experiment with autoparams
set_user_auto('doe', 1)
assert get_user_auto('doe') == 1
