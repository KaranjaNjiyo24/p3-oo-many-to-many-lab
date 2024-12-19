class Author:
    pass


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)


class Contract:
    pass