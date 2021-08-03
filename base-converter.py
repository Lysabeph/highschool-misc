import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="runs a test", action="store_true")
args = parser.parse_args()

def baseConvert(startBase, resultBase, numberToConvert, printResult=True):
    assert(startBase < 37
            and startBase > 1), "Starting base out of range [2-36]."
    assert(resultBase < 37
            and resultBase > 1), "Resulting base out of range [2-36]."

    numberToConvert  = str(numberToConvert).upper()
    numberIsNegative = False

    # Stores whether the number is negative.
    # This is stripped during the convertion and added back at the end.
    if numberToConvert.startswith("-"):
        numberIsNegative = True
        numberToConvert = numberToConvert[1:]

    resultDigits = []

    for digit in numberToConvert:
        if digit.isalpha():
            digit = ord(digit) - 55

        assert(startBase > int(digit)), (str(numberToConvert) + " not of base "
                                            + str(startBase) + ".")
        resultDigits.append(int(digit))

    resultDigits = resultDigits[::-1]

    mod = 0

    for index, digit in enumerate(resultDigits):
        mod += (startBase**index) * digit

    resultDigits = [mod%resultBase]

    while mod >= resultBase:
        mod = mod//resultBase
        resultDigits.append(mod%resultBase)

    resultDigits = resultDigits[::-1]

    for index, digit in enumerate(resultDigits):
        if digit >= 10:
            resultDigits[index] = chr(digit + 55)

    result = ''.join(str(digit) for digit in resultDigits)

    if numberIsNegative:
        result = "-" + result

    if printResult:
        print(str(numberToConvert) + " from base " + str(startBase) + " to "
                    + str(resultBase) + " is " + str(result))

    return result


# Base converter.
def denaryToBase(base, numberToConvert):
    return baseConvert(10, base, numberToConvert)


# Base de-converter.
def baseToDenary(base, numberToConvert):
    return baseConvert(base, 10, numberToConvert)


def test():
    baseConvert(10, 23, 111)
    baseConvert(23, 10, 111)
    denaryToBase(23, 111)
    baseToDenary(23, 111)

if args.test:
    test()
