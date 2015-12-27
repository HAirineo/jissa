import digilog, math
# Use the math.eval() method to evaluate the expression to be given by the user

def main():
	number = str(input("Enter a number to convert: "))
	base = input("Enter the base of the number: ")
	print digilog.whole_evaluate(str(decimal_separate(number)[0]), base) + digilog.decimal_evaluate(str(decimal_separate(number)[1]), base)	

# decimal_separate(expr) separates the whole number and decimal number of an expression
def decimal_separate(expr):
	whole_number = ""; decimal_number = ""
	for x in range(len(expr)):
		if expr[x] == ".":
			break
		else:
			whole_number += expr[x]
			decimal_number = expr.replace(expr[x], "")
			decimal_number = decimal_number.replace(".", "")
	return int(whole_number), int(decimal_number);

main()