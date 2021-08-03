dict = {
        1 : "Kelly's Eye",
        2 : "One little duck",
        3 : "Cup of tea",
        4 : "Knock at the door",
        5 : "Man alive",
        6 : "Half a dozen",
        7 : "Lucky",
        8 : "Garden gate",
        9 : "Doctor's orders",
        10: "David's den"
    }

bingoNumberIsValid = False

while not bingoNumberIsValid:
    bingoNumber = input("Please enter a number.\n~~> ")

    if bingoNumber.isdigit() and int(bingoNumber) > 0 and int(bingoNumber) < 91:
        bingoNumberIsValid = True
    else:
        print("Invalid number, please enter again.\n")

bingoCall = dict[int(bingoNumber)]
print(str(bingoNumber) + ": " + bingoCall)
