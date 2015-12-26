# Module to separate whole number and decimal number portion of a given number
import digilog

def separate(expr):
	whole_number = ""; decimal_number = ""
	for x in range(len(expr)):
		if expr[x] == ".":
			break
		else:
			whole_number += expr[x]
			decimal_number = expr.replace(expr[x], "")
			decimal_number = decimal_number.replace(".", "")
	return int(whole_number), int(decimal_number);

expr = separate(str(1.25))
print digilog.Whole.whole_evaluate(str(input("Enter a number to convert: ")), input("Enter the base of the number: ")) + digilog.Decimal.decimal_evaluate(str(input("Enter a number to convert: ")), input("Enter the base of the number: "))