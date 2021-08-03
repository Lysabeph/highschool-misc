import random
import re

with open("bingo-calls.txt", "r") as bingoCallsFile:
    lines = bingoCallsFile.readlines()

bingoCalls = {}

for lineIndex, callText in enumerate(lines):
    bingoCalls[lineIndex + 1] = callText[:-1]

BINGO_CALLS = bingoCalls

bingoSize = 15
lineSize  = 5

hasBingo        = False
hasLine         = False
playingForBingo = False

numbersCalled = []

inputPrompt = ">>> "

# Get starting values.
print("Are players able to play for a line? [y/N]")

playingForALine = input(inputPrompt).lower()

if playingForALine != "y":
    playingForBingo = True
    lineSize = 0
else:
    # Enter line size.
    enteredLineSizeIsValid = False

    while not enteredLineSizeIsValid:
        print()
        print("How many numbers make up a line?")
        print("Leave blank for default (" + str(lineSize) + ").")

        enteredLineSize = input(inputPrompt)

        if len(enteredLineSize) == 0:
            enteredLineSizeIsValid = True
        elif enteredLineSize.isdigit() and int(enteredLineSize) >= 1:
            lineSize = int(enteredLineSize)
            enteredLineSizeIsValid = True
        else:
            print()
            print("Invalid line size. Please enter again.")

# Enter bingo size.
enteredBingoSizeIsValid = False

while not enteredBingoSizeIsValid:
    print()
    print("How many numbers make up bingo?")
    print("Leave blank for default (" + str(bingoSize) + ").")

    enteredBingoSize = input(inputPrompt)

    if len(enteredBingoSize) == 0:
        enteredBingoSizeIsValid = True
    elif enteredBingoSize.isdigit() and int(enteredBingoSize) > lineSize:
        bingoSize = int(enteredBingoSize)
        enteredBingoSizeIsValid = True
    else:
        print()

        if (enteredBingoSize.isdigit() and int(enteredBingoSize) >= 1
                and int(enteredBingoSize) <= lineSize):
            print("Bingo size cannot be smaller or the same as the line size ("
                    + str(lineSize) + ").")

        print("Invalid bingo size. Please enter again.")


def validateNumbers():
    print()
    print("Please enter the numbers that you have crossed off.")
    print("Please use commas (,) to separate your numbers.")
    print("Alternatively, enter 'c' to cancel")

    numbers = input(inputPrompt).lower()
    print()

    if numbers == "c":
        return False
    else:
        separatedNumbers = numbers.replace(" ", "").split(",")

        stringsToRemove = []
        numbersOneToNinety = re.compile("[1-9]|[1-8][0-9]|90")

        # Adds invalid strings to array.
        for string in separatedNumbers:
            if not numbersOneToNinety.fullmatch(string):
                stringsToRemove.append(string)

        # Removes invalid strings.
        for string in stringsToRemove:
            separatedNumbers.remove(string)

        # Remove duplicates.
        separatedNumbers = list(set(separatedNumbers))

        separatedNumbers.sort(key=int)

        if not playingForBingo and len(separatedNumbers) != lineSize:
            print("Incorrect amount of numbers entered.")
            print(str(lineSize) + " numbers need to be entered.")

            return False

        elif playingForBingo and len(separatedNumbers) != bingoSize:
            print("Incorrect amount of numbers entered.")
            print(str(bingoSize) + " numbers need to be entered.")

            return False

        notCalledNumbers = []
        calledNumberString = ""

        for number in separatedNumbers:
            if not number.isdigit() or int(number) not in numbersCalled:
                notCalledNumbers.append(number)
            else:
                calledNumberString += number + ", "

        calledNumberString = calledNumberString[:-2]

        if len(notCalledNumbers) == 0:
            print("Congratulations!")

            if lineSize == 1:
                print(calledNumberString + " has been called.")
            else:
                lastCommaIndex = calledNumberString.rfind(",")

                calledNumberString = (calledNumberString[:lastCommaIndex]
                                        + " and" + calledNumberString[
                                                        lastCommaIndex+1:])

                print(calledNumberString + " have all been called.")

            return True
        else:
            notCalledNumberString = ""

            for number in notCalledNumbers:
                notCalledNumberString += str(number) + ", "

            notCalledNumberString = notCalledNumberString[:-2]

            print("The following numbers have not been called: "
                    + notCalledNumberString + ".")

            return False


def checkNumbers():
    print("Let's check some numbers.")

    if validateNumbers():
        return True
    else:
        doneChecking = False

        while not doneChecking:
            print()
            print("Those numbers could not be verified.")
            print("Are there any more numbers that need to be checked? [y/N]")

            moreNumbers = input(inputPrompt).lower()

            if moreNumbers == "y" and validateNumbers():
                return True
            elif moreNumbers != "y":
                doneChecking = True
            else:
                doneChecking = False

        return False


# Print line and bingo sizes needed.
print()

if not playingForBingo:
    print("Players need " + str(lineSize) + " numbers for a line.")

print("Players need " + str(bingoSize) + " numbers for bingo.")

# Start.
while not hasBingo:
    print()

    playingFor = "BINGO"

    if not playingForBingo:
        playingFor = "a LINE"

    print("We are currently playing for " + playingFor + ".")
    input("Hit return to draw a number.")
    print()

    newBingoNumberCalled = False

    while not newBingoNumberCalled:
        bingoNumber = random.randint(1, 90)

        if len(numbersCalled) != 90 and bingoNumber not in numbersCalled:
            numbersCalled.append(bingoNumber)
            bingoCall = BINGO_CALLS[bingoNumber]
            newBingoNumberCalled = True

    numberCall = bingoCall + ", number " + str(bingoNumber) + "!"

    paddingLength    = (len(numberCall) + 2)
    paddingChar = "*"

    print(paddingChar*3 + paddingChar*paddingLength + paddingChar*3)
    print(paddingChar*3 + " " + numberCall + " " + paddingChar*3)
    print(paddingChar*3 + paddingChar*paddingLength + paddingChar*3)

    if len(numbersCalled) == 90:
        print()
        print("All the numbers have been called.")
        print("BINGO!")
        hasBingo = True
    elif ((not playingForBingo and len(numbersCalled) < lineSize)
            or (playingForBingo and len(numbersCalled) < bingoSize)):
        print()
        print("There haven't been enough number calls for a player to have "
                + playingFor + " yet.")
    else:
        print()
        print("Does anyone have " + playingFor + "? [y/N]")
        checkNeeded = input(inputPrompt).lower()

        if checkNeeded == "y":
            numbersAreValid = checkNumbers()

            if numbersAreValid and not hasLine:
                hasLine = True
                playingForBingo = True
                print("We are no longer playing for " + playingFor + ".")
            elif numbersAreValid and hasLine and not hasBingo:
                hasBingo = True
            else:
                print()
                print("False alarm!")
                print("We are still playing for " + playingFor + ".")

print("BINGO!")
print("That's all folks!")
