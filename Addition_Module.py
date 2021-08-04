

from Conversion_Module import *
from Gates_Module import *

# Converting the given input numbers to binary and then adding them.
def addition_function (list1, list2):
    CIn = 0
    add = []
    
    for i in range (7, -1, -1):
        A = list1 [i]
        B = list2 [i]
        O1 = XOR(A, B)
        O2 = NAND(O1, CIn)
        O3 = OR(O1, CIn)
        Sum_1 = AND(O2, O3)
        O4 = AND(A, B)
        O5 = AND(O1, CIn)
        O6 = NOR(O4, O5)
        COut = NOT(O6)
        CIn = COut
        add.append (Sum_1)
        
    add.append (CIn)
    
    #If the addition is 9 bits.
    if CIn == 1:
        add = "--- STACK ERROR!!! --- \nThe addition has exceeded the maximum 8 bits limit!"
    else:
        add = list_Digits (reverse(add)) # Changing the added number to digit and reversing it if it is 8 bits.
    return add

