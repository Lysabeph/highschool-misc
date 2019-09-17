#Declares list of all possible values of coins/notes(pence), declares separate
#list for all note-type currency and requests item price and amount paid.
changelist=[2000,1000,500,200,100,50,20,10,5,2,1]
notes=(2000,1000,500)
amount_due=input("What is the total amount of the item(s) [GBP]?: ")
amount_paid=input("How much money has been paid? [GBP]: ")
#A try selection that ensures the entered values are numbers.
try:
    #Converts entered GBP values into pence and calculates change required.
    amount_due=float(amount_due)*100
    amount_paid=float(amount_paid)*100
    change=amount_paid-amount_due
    #Checks paid amount is greater than item price.
    if change<0:
        total_change="Not enough money has been paid"
    #Checks if the paid amount is correct for item price.
    elif change==0:
        total_change="Exact amount paid. No change needed."
    #Otherwise, precise coin/note amounts are calculated.
    else:
        total_change="£"+format(change/100,',.2f')+" change required as:\n"
        #Loops through all coin/note types.
        for amount in changelist:
            #Checks if currently selected coin/note can be used for
            #change - if so, the maximum quantity suitable.
            quantity=int(change//amount)
            if quantity!=0:
                #Sorts coins from notes and GBP from pence.
                if amount in notes:
                    total_change+=str(quantity)+" £"+str(int(amount/100))+" Note(s)\n"
                elif amount>=100:
                    total_change+=str(quantity)+ " £"+str(int(amount/100))+" Coin(s)\n"
                else:
                    total_change+=str(quantity)+" "+str(int(amount))+"p Coin(s)\n"
                #Reduces needed change after calculations.
                change-=amount*quantity
    #Displays result to user.
    print(total_change)
#Except selection that catches invalid user inputs.
except ValueError:
    print("Invalid amount(s) entered. Ensure all numbers are entered as digits.")

