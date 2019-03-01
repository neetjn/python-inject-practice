import inject


def Foobar():
    return 'hello world'


@inject.params(foobar=Foobar)
def foobar(something, foobar):
    print(something)
    print(foobar)

inject.configure()

foobar('bro')
