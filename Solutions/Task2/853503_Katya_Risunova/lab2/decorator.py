def cached(func):
    fibonachi = {}

    def hash_table(a):
        if fibonachi.get(to_key(a)):
            print(a, "fibonachi: ", end=" ")
            return fibonachi[to_key(a)]
        else:
            print("Now calculated: ", end=" ")
            fibonachi[to_key(a)] = func(a)

            return func(a)
    return hash_table


@cached
def fibonachi(a):
    k = 1
    m = 1
    toreturn = 0
    for _ in range(a):
        toreturn = k
        k , m = m, k + m
    return toreturn

def to_key(a):
    return str(a)


if __name__ == "__main__":
    print(fibonachi(6))
    print(fibonachi(13))
    print(fibonachi(6))

