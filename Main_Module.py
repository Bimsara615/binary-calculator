

from Conversion_Module import *
from Addition_Module import addition_function
from Input_Module import input_function 
from Output_Module import output_function
from Gates_Module import *


again = "y"

#Creating a loop to run the program until said so.
while ((again.lower()) == "y"):
    num1 = input_function()
    num2 = input_function()
    
    bin1 = Deci_Bina (num1)
    bin2 = Deci_Bina (num2)
    
    rev1 = reverse (bin1)
    rev2 = reverse (bin2)
    
    digit1 = list_Digits (rev1)
    digit2 = list_Digits (rev2)

    binary_sum = addition_function (rev1, rev2)
    
    output_function (digit1, digit2, binary_sum)
    
    again = input ("Do you wish to continue? (y/n).\n")
    print("")

exit()
