#Stock Control Task 2
#Aug 26th 2015
#Made by Elisabeth Morgan

#Imports the 're' module.
import re

#Creates all the lists and variables needed.
Amount = []
CodePattern = '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
Continue = 'Y'
Order = []
Price = []
Receipt = []
Total = 0.00

#Open the file of products and reads the contents.
f = open("Products.txt", 'r')
print("Welcome to our shop!\nPlease choose an item from our catalogue:\n")
print(f.read()); f.seek(0)
Items = f.readlines()
f.close()

#Loops until the user has ordered all their items.
while Continue.upper() == 'Y':

    #Resets the value of 'Quantity' after each order.
    Quantity = ''

    #Just a minor thing that prints a different message after the user's first order.
    if Continue == 'y':

        Code = input("\nPlease choose another code from the list.\n>>> ")

    else:

        Code = input("Please choose a code from the list.\n>>> ")

    #Checks the entered code to make sure it's valid.
    if re.match(CodePattern, Code) and len(Code) == 8:

        #Loops until a valid quantity is entered.
        while True:

            #Asks for a quantity.
            Quantity = input("\nPlease enter the quantity of " + str(Code) + " that you would like to order.\n" +
                           "Please note, you can order, at maximum, 20 of the same item.\n>>> ")

            #Validates the quantity to make sure it fits the range.
            if (Quantity.isdigit() == False) or (int(Quantity) > 20) or (int(Quantity) < 1):

                print("\nInvalid amount entered.\n")

            else:

                #Adds the quantity to the list of amounts and the code to the list of orders.
                Amount.append(Quantity + "   ")
                Order.append(Code)

                #Improves the appearance of the quantity.
                if len(str(Quantity)) != 2:

                    Amount[-1] = Amount[-1] + " "

                #Ends the loop.
                break

        #Asks the user if they would like to choose another item from the list.
        Continue = input("\nWould you like to order another item? [Y/N]\n>>> ").lower()

    else:

        print("\nThat wasn't an eight digit code!\n")
        Continue = 'y'

#Starts the receipt.
print("\nHere is your receipt:\n")

#Loops through all the items the user has ordered.
for ii in range(len(Order)):

    #Loops through each item in the file.
    for i in range(len(Items)):

        #Checks each ordered item to see if it is in the file.
        if Order[ii] in re.split("\,", Items[i])[0]:

            #Calculates the total price of each item (Price * Quantity).
            Price.append(int(Amount[ii]) * float(re.split(",", Items[i])[2]))

            #Improves the appearance of the price.
            if len(re.split('\.', str(Price[-1]))[1]) < 2:

                Price[-1] = str(Price[-1]) + "0"

            #Adds each order to the receipt.
            Receipt.append(Order[ii] + re.split(",", Items[i])[1] + Amount[ii] +
                           re.split(",", Items[i])[2] + "  " + str(Price[-1]))

    #Adds the items ordered that aren't in the file to the receipt as 'Not Found' items.
    if len(Receipt) != ii + 1:

        Receipt.append(Order[ii] + " Not Found  N/A  N/A   N/A")

#Calculates the total cost of the order.
for i in range(len(Price)):

    Total += float(Price[i])

#Improves the appearance of the total.
if len(re.split('\.', str(Total))[1]) < 2:

    Total =  str(Total) + "0"

#Adds the total cost to the end of the receipt.
Receipt.extend(["-" * 37, "Total cost of order"+ " " * 12 + str(Total)])

#Prints the receipt for the user to see.
for i in range(len(Receipt)):

    print(Receipt[i])
