cost=input("Please enter the cost of the carpet per square metre: ")
width=input("Please enter the width of the carpet(metres): ")
length=input("Please enter the length of the carpet(metres): ")
discount=input("Would you like a discount? [y/N]: ").upper()
delivery=input("Would you like your carpet to be delivered? [y/N]: ").upper()
fitting=input("Would you like your carpet to be fitted for you? [y/N]: ").upper()
subtotal = ((int(width)*int(length))//1+1)*int(cost)
if discount=="Y":
    subtotal*=0.9
if delivery=="Y":
    subtotal+=20
if fitting=="Y":
    subtotal+=((int(width)*int(length))//1+1)*5
vat=subtotal*0.2
total=subtotal*1.2
print("\nSubtotal: "+str(subtotal)+"\nV.A.T.(20%): "+str(vat)+"\nTotal: "+str(total))