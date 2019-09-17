# Base converter.
def denary_to_base(base, number):
    assert(base < 37 and base > 1), "Chosen base is out of range [2-36]."
    number = int(number)
    if number < 0:
        negative = True
    else:
         negative = False
    mod = abs(number)
    values = [mod%base]
    while mod >= base:
        mod = mod//base
        values.append(mod%base)
    values = values[::-1]
    for index, integer in enumerate(values):
        if integer >= 10:
            values[index] = chr(integer + 55)
    result = ''.join(str(x) for x in values)
    if negative:
        result = "-" + result
    return result

# Base de-converter.
def base_to_denary(base, number):
    assert(base < 37 and base > 1), "Chosen base is out of range [2-36]."
    number = str(number).upper()
    if number.startswith("-"):
        negative = True
        number = number[1:]
    else:
         negative = False
    values = []
    for digit in number:
        if digit.isalpha():
            digit = ord(digit) - 55
        assert(base > int(digit)), "Number not of base " + str(base) + "."
        values.append(int(digit))
    values = values[::-1]
    result = 0
    for index, integer in enumerate(values):
        result += (base**index) * integer
    if negative:
        result = "-" + result
    return int(result)


def base_convert(init_base, res_base, number):
    assert(init_base < 37 and init_base > 1), "Initial base is out of range [2-36]."
    assert(res_base < 37 and res_base > 1), "Resultant base is out of range [2-36]."
    number = str(number).upper()
    if number.startswith("-"):
        negative = True
        number = number[1:]
    else:
        negative = False
    values = []
    for digit in number:
        if digit.isalpha():
            digit = ord(digit) - 55
        assert(init_base > int(digit)), "Number not of base " + str(init_base) + "."
        values.append(int(digit))
    values = values[::-1]
    denary = 0
    for index, integer in enumerate(values):
        denary += (init_base**index) * integer
    mod = denary
    values = [mod%res_base]
    while mod >= res_base:
        mod = mod//res_base
        values.append(mod%res_base)
    values = values[::-1]
    for index, integer in enumerate(values):
        if integer >= 10:
            values[index] = chr(integer + 55)
    result = ''.join(str(x) for x in values)
    if negative:
        result = "-" + result
    return result
