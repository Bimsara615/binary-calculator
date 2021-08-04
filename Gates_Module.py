

# Logic gates used for the bit adder

# AND Gate
def AND (a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


# OR Gate
def OR(a, b):
    c = 0
    if a == 1 or b == 1:
        return 1
    else:
        return 0


# NOT Gate
def NOT(a):
    if(a == 0):
        return 1
    elif(a == 1):
        return 0


# NAND Gate
def NAND (a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1


# NOR Gate
def NOR (a, b):
    if(a == 0) and (b == 0):
        return 1
    else:
        return 0


# XOR Gate
def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0
