#Task 1 Stock Control
#Mr Miller
#11/07/15

#Import of re and time modules
import re
import time

#rule for the productcode (barcode) needing to be 7 digits

validproductcode ="[0-9][0-9][0-9][0-9][0-9][0-9][0-9]"

while True:

    #An empty list to store the users input
    productcode = []

    #Input of the 7 digit code
    print ("Please enter the 7 digit code ")
    sevendigit=input("Product Code: ")

    #Looking to see if the users input matches the rule of numbers applied
    if re.match(validproductcode,sevendigit) and len(sevendigit) == 7:

        #This is printed if the users imput matches the rule applied
        print ("Your choice of product code has been accepted")
        time.sleep(2)

        #This reminds the user what they entered
        print ("The product code you entered is ",sevendigit)

        #A for loop to split the number entry into a string and then added to a list
        for i in sevendigit:
            productcode.append(i.split('\t')[0])

        #Use of index numbers to apply the calculations

        D1=(int(productcode[0]))*(int(3))
        D2=(int(productcode[1]))
        D3=(int(productcode[2]))*(int(3))
        D4=(int(productcode[3]))
        D5=(int(productcode[4]))*(int(3))
        D6=(int(productcode[5]))
        D7=(int(productcode[6]))*(int(3))


        #Sum of the calculations
        totalproductcode = (D1+D2+D3+D4+D5+D6+D7)

        n =(totalproductcode)

        #Working out the rounding up or down to the nearest multiple of 10

        if (n % 10):
            n = n + (10 - n % 10)

        #Working out the check digit
            
        checkdigit=(n-totalproductcode)
        productcode.append(str(checkdigit))

        y=""

        for x in productcode:
            y=y+str(x)
        
        print ("The GTIN-8 is",y)

        if int(checkdigit%10):
            print ("The GTIN-8 is valid")
        else:
            print ("The GTIN-8 is invalid")

        #The user is asked if they want to try another barcode

        again = input("Do you want to add another barcode?")

        if again !='y':
            print ("Thank you for using the Stock Control Program ")
            time.sleep(1)

            x=input("Press enter to close the window")
            
            break
#This code will run if the user presses 'y' and the code will loop back to the beginning        
        else:
            print ("Ok, lets try another barcode")

    else:

        print("Sorry the code is not suitable")

        
    

