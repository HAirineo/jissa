import digilog, math, re

def main():
	expr = raw_input("Enter an expression: ")
	base = input("Enter the base of the numbers: ")
	# target = input("Enter the target base for the solution: ")
	print evaluate_expression(expr, base)

def decimal_separate(expr):
	"Returns the separated whole number and decimal number"
	whole_number = ""; decimal_number = ""
	for x in range(len(expr)):
		if expr[x] == ".":
			break
		else:
			whole_number += expr[x]
			decimal_number = expr.replace(expr[x], "")
			decimal_number = decimal_number.replace(".", "")
	return int(whole_number), int(decimal_number);

def evaluate_expression(expr, base):
	"Returns the evaluated expression"
	answer = ""
	regexpr = r'\d+|[-+/*]'
	regexpr_eval = re.findall(regexpr, expr)
	for x in range(len(regexpr_eval)):
		if regexpr_eval[x] == "+" or regexpr_eval[x] == "-" or regexpr_eval[x] == "\*" or regexpr_eval[x] == "\/":
			answer += regexpr_eval[x]
		else:
			answer += str(digilog.whole_evaluate(str(decimal_separate(regexpr_eval[x])[0]), base) + digilog.decimal_evaluate(str(decimal_separate(regexpr_eval[x])[1]), base))
	return eval(answer)

main()