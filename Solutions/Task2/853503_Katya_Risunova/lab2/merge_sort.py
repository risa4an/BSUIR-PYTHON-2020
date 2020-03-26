import tempfile


def merge_sort(filename,outname):
    lengthOfFile = 0

    with open(filename) as file:
        for line in file:
            lengthOfFile += 1
    files = []
    k = 0
    with open(filename) as file:
        while k < lengthOfFile / 128:
            array = []
            i = 0
            while i < 128:
                temp = file.readline()
                if len(temp) != 0:
                    array.append(int(temp))
                else:
                    break
                i += 1
            array.sort()
            with tempfile.NamedTemporaryFile('w', delete=False) as t:
                for i in array:
                    t.write(str(i) + '\n')
                t.write('\n')
                files.append(t.name)
            k += 1
    kolvonew = len(files)


    while kolvonew != 1:
        k = knew = 0
        while k < kolvonew:
            if k + 1 == kolvonew:
                files[knew] = files[k]
                knew += 1
                k += 1
            else:
                k1 = k
                k2 = k + 1
                with open(files[k1]) as file1:
                    with open(files[k2]) as file2:
                        with tempfile.NamedTemporaryFile('w', delete=False) as t:
                            a1 = file1.readline()
                            a2 = file2.readline()
                            while a2 != '\n'  and (a1) != '\n':
                                if int(a1) < int(a2):
                                    t.write(a1)
                                    a1 = file1.readline()
                                else:
                                    t.write(a2)
                                    a2 = file2.readline()
                            while a1 != '\n':
                                t.write(a1)
                                a1 = file1.readline()
                            while a2 != '\n':
                                t.write(a2)
                                a2 = file2.readline()
                            t.write('\n')
                            files[knew] = t.name
                knew += 1
                k += 2
        kolvonew = knew

    with open(outname, 'w') as file:
        with open(files[0]) as t:
            for line in t:
                file.write(line)

if __name__ == "__main__":
    merge_sort('numbers.txt','numbers2.txt')