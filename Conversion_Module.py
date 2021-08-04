

# Defining a function to convert decimal numbers into binary.
def Deci_Bina (n):
        bit = []
        count = 0
        while count != 8:
                remainder = n%2
                bit.append(remainder)
                n = n//2
                count += 1
        return bit


# Defining a function to reverse the list numbers.

def reverse (revNum):
        rev = []
        for i in range (len(revNum)-1, -1, -1):
                rev.append (revNum [i])
        return rev


# Defining a function to change the list into digits.
def list_Digits (bitList):
        temp = ""
        for i in range (0, len(bitList), 1):
                temp = temp + str(bitList [i])
                digit = int (temp)
        return digit
