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

def to_json(obj):
    json = '{ \n'
    cl = str(obj.__class__)
    if isinstance(obj,(int,float)):
        json += get_name(obj) + " :" + str(obj) + ',\n'
    elif isinstance(obj,bool):
        json += get_name(obj) + " :" + str(obj).lower() + ',\n'
    elif isinstance (obj, str):
        json += get_name(obj) +  " :\"" + obj + '\",\n'
    elif isinstance(obj, (list,tuple)):
        json += get_name(obj) + " :[\n"
        for v in obj:
            json += to_json_noname(v)
        json = json [:-2] + '\n]\n'
    elif isinstance(obj, dict):
        json += get_name(obj) + " :{\n"
        for k,v in obj.items():
            json += "\"" + str(k) + "\" :" + to_json_noname(v)
        json = json[:-2] + '\n}\n'
    elif "<class \'__main__." in cl:
        json += get_name(obj) + " :{\n"
        for k, v in obj.__dict__.items():
            json += "\"" + str(k) + "\" :" + to_json_noname(v)
        json = json[:-2] + '\n}\n'
    if json[len(json) - 2]==',':
        json = json[:-2] + '\n}\n'
    else:
        json += "}\n"
    return json

def to_json_noname(obj):
    json = ''
    if isinstance(obj, (int,float)):
        json += str(obj) + ',\n'
    elif isinstance(obj,str):
        json += "\"" + obj + "\",\n "
    elif isinstance(obj, bool):
        json += str(obj).lower() + ",\n"
    elif isinstance(obj, (list, tuple)):
        json += '[\n'
        for v in obj:
            json += to_json_noname(v)
        json =json[:-2] + '\n],\n'
    elif isinstance(obj, dict):
        json += "{\n"
        for k,v in obj.items():
            json += "\"" + str(k) + "\" :" + to_json_noname(v)
        json = json[:-2] +  '\n},\n'
    elif "<class \'__main__." in str(obj.__class__):
        json += '{\n'
        for k, v in obj.__dict__.items():
            json += "\"" + str(k) + "\" :" + to_json_noname(v)
        json = json[:-2] + "\n},\n"
    return json

def get_name(obj):
    for k, v in globals().items():
        idi = id(v)
        idobj = id(obj)
        if idi == idobj:
            if k == None:
                return " "
            else:
                return "\"" + k + "\" "


if __name__ == "__main__":
    book = Book()
    book = Book.get_instance()
    print (to_json(book))
    m = "hi!"
    print(to_json(m))
    k = [1,2,3]
    d = {'dict': 1, 'dictionary': 2}
    print (to_json(k))
    murakami = Book()
    murakami.author = "H.Murakami"
    murakami.name = "Killing comrade"
    murakami.pages = 143
    k = [book, murakami]
    print(to_json(k))
