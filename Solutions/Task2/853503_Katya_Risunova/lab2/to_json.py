class Book(object):
    __instance = None

    @staticmethod
    def get_instance():
        if Book.__instance is None:
            Book()
        return Book.__instance

    def __init__(self):
        if Book.__instance is None:
            self.author = "J.K. Rowling"
            self.name = "Harry Potter"
            self.pages = 346
        Book.__instance = self


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def to_json(obj):
    json = "{"
    for key, value in obj.__dict__.items():
        json += "\"" + str(key) + "\": " + ((str(value)) if is_float(value) else ("\"" + str(value) + "\"")) + ", "
    json = json[:-2]
    json += "}"
    return json


if __name__ == "__main__":
    book = Book()

    book = Book.get_instance()
    print(book)
    print(to_json(book))

    murakami = Book()
    murakami.name = "Killing comrade"
    murakami.pages = "143"
    print(to_json(murakami))
