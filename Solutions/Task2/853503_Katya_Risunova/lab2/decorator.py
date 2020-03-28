def cached(func):
    cache = dict()
    def memorize(*args):
        if args in cache:
            return str(cache[args]) + " cached"
        result = func(*args)
        cache[args] = result
        return str(result) + " now"
    return memorize

@cached
def fibonachi(a):
    k = 1
    m = 1
    toreturn = 0
    for _ in range(a):
        toreturn = k
        k , m = m, k + m
    return toreturn

@cached
def sumFibonachi(a):
    sum = 0
    k = 1
    m = 1
    for _ in range(a):
        sum += k
        k, m = m, k + m
    return sum





if __name__ == "__main__":
    print(fibonachi(6))
    print(fibonachi(13))
    print(fibonachi(6))
    print (sumFibonachi(6))
