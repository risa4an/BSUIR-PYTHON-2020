import math

class Vector(object):
    def __init__(self, array):
        self.n = len(array)
        self.arr = array

    def __add__(self, other):
        if self.n != other.n:
            print ("error")
            return
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] + other.arr[i]
        return vector

    def __sub__(self, other):
        if self.n != other.n:
            print ("error")
            return
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] - other.arr[i]
        return vector

    def __mul__(self, other):
        if type(other) is int:
            arr = [0] * self.n
            vector = Vector(arr)
            for i in range(0, self.n):
                vector.arr[i] = self.arr[i] * other

        else:
            if self.n != other.n:
                print ("error")
                return
            arr = [0] * self.n
            vector = Vector(arr)
            for i in range (0, self.n):
                vector.arr[i] = self.arr[i] * other.arr[i]

        return vector



    def __eq__(self, other):
        if self.n != other.n:
            return False
        for i in range(0, self.n):
            if self.arr[i] != other.arr[i]:
                return False
        return True

    def len(self):
        a = 0
        for i in self.arr:
            a += i**2
        return math.sqrt(a)

    def __str__(self):
        line = ''
        for i in range(0, self.n):
            line += str(self.arr[i]) + ' '
        return line

    def __getitem__(self, item):
        return self.arr[item]




if __name__ == "__main__":
    vector1 = Vector([1,2,3])
    vector2 = Vector([4,5,6])
    print ("First vector: ", str(vector1))
    print("Second vector: ", str(vector2))
    print("Addition: ", vector1  + vector2)
    print("Substraction: ", vector1 - vector2)
    print("Multiply 3: ", vector1 * 3)
    print ("Length of vector1: ", vector1.len())
    if vector1 == vector2:
        print("vector1 is equal vector2")
    else:
        print("vector1 is not equal vector2")
    print("Multiply vector1 and vector2: ", vector1 * vector2)



