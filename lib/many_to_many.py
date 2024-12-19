class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)


class Contract:
    all =[]

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        