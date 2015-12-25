# This module separates the whole number and decimal number
# portion of a given number. However, this is limited yet 
# for the whole number portion as the return value
def separate(expr):
	whole_number = ""
	decimal_number = ""
	for x in range(len(str(expr))):
		if str(expr[x]) == ".":
			break
		else:
			whole_number += str(expr[x])
	# Might be able to use ternary operator instead
	# of the conventional if-else statement
	return whole_number;

print separate(str(01.25))