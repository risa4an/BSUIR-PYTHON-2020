class Book(object):
    def __init__(self):
        self.author = "J.K. Rowling"
        self.name = "Harry Potter"
        self.pages = 346


def get_dict(text, i):
    d = dict()
    name = ''
    while text[i] != '}':
        if text[i] == '"':
            i += 1
            while (text[i] != '"'):
                name += text[i]
                i+=1
        elif text[i] ==':':
            i += 1
            value, i = get_value(text,i)
            d[name] = value
            name = ''
            while (text[i] != '\n'):
                i += 1
        i+= 1
    return d,i



def get_value(text, i):
    value = ''
    if text[i] == '"':
        i += 1
        while text[i] != '"':
            value += text[i]
            i += 1
    elif text[i] == 'F':
        value = False
    elif text[i] == 'T':
        value = True
    else:
        while text[i] != ',' and text[i] != '\n':
            value += text[i]
            i += 1
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
    return value, i


def get_arr(text,i):
    arr = []
    while(text[i] != ']'):
        if text[i] == '{':
            value, i = get_dict(text,i)

        else:
            value, i = get_value(text, i)
        while (text[i] != '\n'):
            i += 1
        i += 1
        arr.append(value)
        value = ''
    return arr, i




def from_json(text, i):
    openbrackets = 0
    closebrackets = 0
    name = ''
    obj = ''
    if text[i] == '{':
        openbrackets += 1
        i+=1
    while (openbrackets != closebrackets):
        if text[i] == '{':
            openbrackets += 1
        elif text[i] == '"':
            i += 1
            name = ''
            while (text[i] != '"'):
                name += text[i]
                i += 1
        elif text[i] == ':':
            i += 1

            if text[i] == '[':
                i+=2
                globals()[name], i = get_arr(text, i)
            elif text[i] == '{':
                i += 2
                globals()[name], i = get_dict(text, i)
            else:
                value, i = get_value(text,i)
                globals()[name] = value



        elif text[i] == '}':
            closebrackets += 1
        i += 1
    return obj




if __name__ == "__main__":
    s = '{ \n"k"  :[\n{\n"author" :"J.K. Rowling",\n"name" :"Harry Potter",\n"pages" :346\n},\n{\n"author" :"H.Murakami",\n"name" :"Killing comrade",\n"pages" :143\n}\n]\n}'

    from_json(s, 0)
    print(k)
