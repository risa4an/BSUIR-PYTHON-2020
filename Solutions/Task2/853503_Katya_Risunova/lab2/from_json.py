class Book(object):
    def __init__(self):
        self.author = "J.K. Rowling"
        self.name = "Harry Potter"
        self.pages = 346

def from_json(text, obj):
    working_word = ""
    write_symbol = False
    is_digit = False
    key_value = []
    for symbol in text:
        if symbol.isdigit():
            working_word += symbol
            is_digit = True
        elif symbol.isdigit() is False and is_digit is True:
            key_value.append(working_word)
            is_digit = False
            working_word = ""

        if write_symbol and symbol != '"':
            working_word += symbol
        elif write_symbol and symbol != " " and symbol != '"':
            working_word += symbol

        if symbol == '"' and write_symbol is False:
            write_symbol = True
        elif symbol == '"' and write_symbol:
            key_value.append(working_word)
            write_symbol = False
            working_word = ""

    i = 0
    for key, value in obj.__dict__.items():
        if str(key) == key_value[i]:
            if type(value) is int:
                setattr(obj, key, int(key_value[i + 1]))
            elif type(value) is float:
                setattr(obj, key, float(key_value[i + 1]))
            elif type(value) is complex:
                setattr(obj, key, complex(key_value[i + 1]))
            elif type(value) is str:
                setattr(obj, key, key_value[i + 1])
            elif type(value) is bool:
                setattr(obj, key, bool(key_value[i + 1]))
        i += 2
    return obj


if __name__ == "__main__":
    book = Book()
    print("Old: ", book.__dict__)
    person = from_json('{"author": "J.K. Rowling", "name": "Harry Potter", "greeting": 346}', book)
    print("New: ", book.__dict__)