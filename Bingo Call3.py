import random, sys, time
calls = {
    1 : "Kelly's Eye",
    2 : "One Little Duck",
    3 : "Cup of Tea",
    4 : "Knock at the Door",
    5 : "Man Alive",
    6 : "Half a Dozen",
    7 : "Lucky",
    8 : "Garden Gate",
    9 : "Doctor's Orders",
    10: "David's Den",
    11: "Legs Eleven",
    12: "One Dozen",
    13: "Unlucky for Some",
    14: "Valentines Day",
    15: "Young and Keen",
    16: "Sweet Sixteen",
    17: "Dancing Queen",
    18: "Coming of Age",
    19: "Goodbye-Teens",
    20: "Two and Zero",
    21: "Key of the Door",
    22: "Two Little Ducks",
    23: "Two and Three",
    24: "Two Dozen",
    25: "Jump and Jive",
    26: "Pick and Mix",
    27: "Gateway to Heaven",
    28: "Two and Eight",
    29: "Rise and Shine",
    30: "Dirty Gertie",
    31: "Get Up and Run",
    32: "Buckle My Shoe",
    33: "All the Three's",
    34: "Ask for More",
    35: "Jump and Jive",
    36: "Three Dozen",
    37: "More than Eleven",
    38: "Three and Eight",
    39: "Steps",
    40: "Four and Zero",
    41: "Four and One",
    42: "Winnie the Pooh",
    43: "Four and Three",
    44: "Droopy Drawers",
    45: "Halfway There",
    46: "Up to Tricks",
    47: "Four and Seven",
    48: "Four Dozen",
    49: "Four and Nine",
    50: "Half a Century",
    51: "Five and One",
    52: "Danny La Rue",
    53: "Here comes Herbie",
    54: "Five and Four",
    55: "Snakes Alive",
    56: "Five and Six",
    57: "Heinz Beanz",
    58: "Five and Eight",
    59: "The Brighton Line",
    60: "Five Dozen",
    61: "Bakers Bun",
    62: "Tickety-boo",
    63: "Six and Three",
    64: "Six and Four",
    65: "Old Age Pension",
    66: "Clickety Click",
    67: "Made in Heaven",
    68: "Saving Grace",
    69: "Either Way Up",
    70: "Seven and Zero",
    71: "Bang on the Drum",
    72: "Six Dozen",
    73: "Queen Bee",
    74: "Seven and Four",
    75: "Seven and Five",
    76: "Trombones",
    77: "Sunset Strip",
    78: "Seven and Eight",
    79: "One More Time",
    80: "Gandhi's Breakfast",
    81: "Stop and Run",
    82: "Eight and Two",
    83: "Time for Tea",
    84: "Seven Dozen",
    85: "Staying Alive",
    86: "Between the Sticks",
    87: "Torquay in Devon",
    88: "Two Fat Ladies",
    89: "Almost There",
    90: "Top of the Shop"
    }
called = []
bingo = False
bingo_total_num = 15
line = False
line_total_num = 5
while bingo == False:
    input("Hit return to draw a number.")
    while True:
        bingo_num = random.randint(1,90) 
        if (len(called) != 90) and (bingo_num not in called):
            called.append(bingo_num)
            bingo_call = calls[bingo_num]
            print(bingo_call + ",",str(bingo_num) + "!\n")
        if len(called) == 90:
            print("BINGO!")
            bingo = True
            break
        if line == False:
            line = input("Line? [y/N]\n~~> ").upper()
        elif line == True and bingo == False:
            bingo = input("Bingo? [y/N]\n~~> ").upper()
        if line == "Y" or bingo == "Y":
            while True:
                numbers = input("Please enter the numbers crossed off \
(E.G. \"1, 34, 49, 61, 88\")\nor enter \"N\" to cancel.\n~~> ").upper()
                if numbers == "N":
                    break
                numbers = numbers.split(", ")
                if (line == "Y" and len(numbers) != line_total_num) or\
                (bingo == "Y" and len(numbers) != bingo_total_num):
                    print(
                    "Invalid amount of numbers, please enter all the numbers.")
                else:
                    valid = True
                    not_called = []
                    for i in numbers:
                        if int(i) not in called:
                            not_called.append(i)
                            valid = False
                    if valid == True:
                        if line == "Y":
                            print("LINE!!!")
                            time.sleep(0.5)
                            print("\nNow play for a full house!")
                            line = True
                        else:
                            print("BINGO!!!")
                            bingo = True
                    else:
                        valid = input(
"The number(s): " + str(not_called) + " haven't been called.\nIf a mistake \
hasn't been made, this player has crossed off the wrong number(s).\nHas a \
mistake been made? [y/N]\n~~> ").upper()
                        if valid != "Y":
                            print("False alarm! The numbers were incorrect.")
                        else:
                            print("Please enter the numbers again.")
        else:
            if line != True:
                line = False
            else:
                bingo = False
            break
