

#Function to take input values.
def input_function():
    check = False
    
    while check == False:
        try:
            num = int(input("Enter a number: "))
            
            #To check if the number is less than 0 or greater than 255.
            if (num < 0 or num > 255):
                print(" --- LIMIT ERROR!!! --- \nPlease enter a number from 0 but less than 256! \n")
            else:
                check = True
                return num
            
        except:
            #Error if invalid value is entered
            print(" --- INPUT ERROR!!! --- \nPlease input a valid number! \n")
