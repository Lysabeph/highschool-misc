Dict = {
    "1" : "Kelly's Eye",
    "2" : "One little duck",
    "3" : "Cup of tea",
    "4" : "Knock at the door",
    "5" : "Man alive",
    "6" : "Half a dozen",
    "7" : "Lucky",
    "8" : "Garden gate",
    "9" : "Doctor's orders",
    "10": "David's den"
    }
while True:
    bingo_num = input("Please enter a number.\n~~> ")
    if bingo_num.isdigit() and int(bingo_num) > 0 and int(bingo_num) < 91:
        break
    else:
        print("Invalid number, please enter again.\n")

bingo_call = Dict[bingo_num]
print(str(bingo_num) + ": " + bingo_call)
