import BaseConverter

GRIDSIZE = 144000
ROW = []
COLUMN = []

for integer in range(GRIDSIZE):
	if GRIDSIZE < 27:
		COLUMN.append(chr(integer + 65))
	else:
		gridChar = BaseConverter.denaryToBase(36, GRIDSIZE)
		intChar = BaseConverter.denaryToBase(36, integer + 1)
		COLUMN.append('#' * (len(gridChar) - len(intChar)) + intChar)
