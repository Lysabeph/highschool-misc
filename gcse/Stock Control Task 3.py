#Stock Control Task 3
#Aug 27th 2015
#Made by Elisabeth Morgan

#Imports the 're' and 'time' modules.
import re, time

#Creates the lists and variables needed for the program.
Amount = []
Code = []
Continue = 'Y'
Current = []
Order = []
Reorder = []
Target = []

#Opens and reads the Stock file.
f = open("Stock.txt", 'r')
Stock = f.readlines()
f.close()

#Creates the Re-stocking file.
f = open("Re-stocking Orders.txt", 'w')
f.writelines("The following items have been sent off to be re-ordered (this is to maintain stock levels):\n")
f.close()

#Adds all the necessary info to the lists of codes and current, reorder and target levels.
for i in range(1, len(Stock)):

    Code.append(re.split("\,", Stock[i])[0])
    Current.append(re.split("\,", Stock[i])[1])
    Reorder.append(re.split("\,", Stock[i])[2])
    Target.append(re.split("\,", Stock[i])[3])

#Loops until the user has entered the full order.
while Continue == 'Y':

    Continue = 'N'

    #Loops until the user enters a valid code.
    while True:

        #Asks the user to enter a code.
        Item = input("What item was ordered?\n>>> ")

        #Loops through all the items in the file.
        for i in range(len(Stock)):

            #Checks if the user entered a code that matches a code in the file.
            if Item in Stock[i][0:]:

                Continue = 'Y'

        #If a valid code was entered then the loop breaks.
        if Continue == 'Y':

            break

        #Else, the user has to enter another code.
        else:

            print("\nInvalid item! Please choose again.\n")

    #Loops until the user enters a valid amount.
    while True:

        #Asks how much of the previously entered item was ordered.
        Quantity = input("\nHow much of " + Item + " was ordered?\n>>> ")

        #Checks that a valid amount was entered.
        if (Quantity.isdigit() == False) or (int(Quantity) > 20) or (int(Quantity) < 1):

            print("\nInvalid amount! Please choose again.\n")

        else:

            #Adds the item code and quantity to their relevent lists.
            Order.append(Item)
            Amount.append(Quantity)

            #Breaks the loop.
            break

    #Asks the user if there was any other items ordered.
    Continue = input("\nWere there any other items ordered? [Y/N]\n>>> ").upper()

    #If so, the user can enter another item code and quantity in the same manner.
    if Continue == 'Y':

        print("\nPlease enter another item.\n")

    #If the user ends the order there, then the stock of each item ordered is updated.

#Loops through each item that was ordered.
for ii in range(len(Order)):

    #Loops through all the codes in the file.
    for i in range(len(Code)):

        #If the order code matches a code in the file, the stock of that item is updated.
        if Order[ii] in Code[i]:

            #Adds a delay to give the appearance of work and allows time for the user to read each item as it is updated.
            time.sleep(1.5)

            #Updates the amount of each item that is in stock.
            Current[i] = int(Current[i]) - int(Amount[ii])

            #Updates the main Stock list when changes are made.
            Stock[i + 1] = Stock[i + 1].replace(re.split("\,", Stock[i + 1])[1], " " + str(Current[i]))

            #If the stock of the ordered item(s) is bellow the re-order amount, more of that item is ordered and the stock updated again.
            if int(Current[i]) < int(Reorder[i]):

                #Tells the user that the item is running low on stock.
                print("\nThe stock of item " + str(Code[i]) + " is running low!")

                #Adds this item to the text file of items that need to be re-ordered and re-stocked.
                f = open("Re-stocking Orders.txt", 'a')
                f.writelines(str(int(Target[i]) - int(Current[i])) + " items of " +
                             str(Code[i]) + " needs to be ordered.\n")

                #Updates the main Stock list to show that more of the item has been ordered and that the stock of this item is now at the target level.
                Stock[i + 1] = Stock[i + 1].replace(re.split("\,", Stock[i + 1])[1], " " + Target[i])

                #Tells the user that more of this item has been ordered and the new stock of that item.
                print("More of item " + str(Code[i]) + " has been ordered and the stock is now at" +
                      str(Target[i]) + " items.")

            #If the stock of the ordered item(s) is not bellow the re-order amount, the user is informed of the stock changes for that item.
            else:

                #Tells the user that the stock of the item has been updated.
                print("\nThe stock has been updated for item " + Code[i] + ".")

#Writes the new stock info to the Stock file.
f = open("Stock.txt", 'w')

for i in range(len(Stock)):

    f.writelines(Stock[i])

f.close()

#Tells the user again that the stock has been fully updated.
print("\nAll the stock of the ordered item(s) has been fully updated.")
