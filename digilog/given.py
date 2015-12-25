# This module separates the whole number and decimal number portion of a given number
def separate(expr):
	whole_number = ""; decimal_number = ""
	for x in range(len(expr)):
		if expr[x] == ".":
			break
		else:
			whole_number += expr[x]
			decimal_number = expr.replace(expr[x], "")
			decimal_number = decimal_number.replace(".", "")
	return "whole number: " + whole_number, "decimal number: " + decimal_number;

print separate(str(1.25))