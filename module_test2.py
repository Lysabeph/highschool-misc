import base_converter

GRIDSIZE = 144000
ROW = []
COLUMN = []
for integer in range(GRIDSIZE):
	if GRIDSIZE < 27:
		COLUMN.append(chr(integer + 65))
	else:
		gridchar = base_converter.denary_to_base(36, GRIDSIZE)
		intchar = base_converter.denary_to_base(36, integer + 1)
		COLUMN.append('#' * (len(gridchar) - len(intchar)) + intchar)
