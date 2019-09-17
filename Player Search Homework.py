#Python lists start with the first value as 0.
#None type used as a buffer so value 1 is the first name in the list.
Names = [None, "Ben", "Thor", "Zoe", "Kate"]
Max = 4
Current = 1
Found = False

PlayerName = input("What player are you looking for?\n>>> ")

while (Found == False) and (Current <= Max):
    if Names[Current] == PlayerName:
        Found = True

    else:
        Current += 1

if Found == True:
    print("Yes, they have a top score.")

else:
    print("No, they do not have a top score.")
