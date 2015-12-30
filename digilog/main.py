import digilog, math, re

def main():
	expr = raw_input("Enter an expression: ")
	base = input("Enter the base of the numbers: ")
	print evaluate_expression(expr, base)

def decimal_separate(expr):
	"Returns the separated whole number and decimal number"
			# Decimal number			Whole number
	return str(math.modf(float(expr))[0]), str(math.modf(float(expr))[1])

def evaluate_expression(expr, base):
	"Returns the evaluated expression"
	answer = "" # String to contain the answer
	regexpr = r'\d+[.]\d+|\d+|[-+/*]' # Regex determining operators and operands
	regexpr_eval = re.findall(regexpr, expr) # Regex method finding all match
	for x in range(len(regexpr_eval)):
		if regexpr_eval[x] == "+" or regexpr_eval[x] == "-" or regexpr_eval[x] == "*" or regexpr_eval[x] == "/":
			# Concatenate the string as it is if it is an operand
			answer += regexpr_eval[x]
		else:
			# Convert the number first before concatenating
			answer += str(digilog.decimal_evaluate(decimal_separate(regexpr_eval[x])[0], base) + digilog.whole_evaluate(decimal_separate(regexpr_eval[x])[1], base))
	return eval(answer)

main()