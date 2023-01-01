b = input("Enter Your Roman Number: ")
def RL(x):
    if (x == 'I' or x == 'i'):
        return 1
    if (x == 'V' or x == 'v'):
        return 5
    if (x == 'X' or x == 'x'):
        return 10
    if (x == 'L' or x == 'l'):
        return 50
    if (x == 'C' or x == 'c'):
        return 100
    if (x == 'D' or x == 'd'):
        return 500
    if (x == 'M' or x == 'm'):
        return 1000
    return -1
def RomtoInt(str):
    a = 0
    i = 0
    while (i < len(str)):
        x1 = RL(str[i])
        if (i + 1 < len(str)):
            x2 = RL(str[i + 1])
            if (x1 >= x2):
                a = a + x1
                i = i + 1
            else:
                a = a + x2 - x1
                i = i + 2
        else:
            a = a + x1
            i = i + 1
    return a
print(RomtoInt(b))