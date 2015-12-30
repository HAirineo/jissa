import digilog, math, re

def main():
	expr = raw_input("Enter an expression: ")
	# base = input("Enter the base of the numbers: ")
	# print evaluate_expression(expr, base)
	
	regexpr = r'\d+[\.]\d+|\d+|[-+/*]'
	regexpr_eval = re.findall(regexpr, expr)
	print decimal_separate(regexpr_eval[0])

def decimal_separate(expr):
	"Returns the separated whole number and decimal number"
	return math.modf(float(expr))[0], math.modf(float(expr))[1]

def evaluate_expression(expr, base):
	"Returns the evaluated expression"
	answer = ""
	regexpr = r'\d+|[-+/*]'
	regexpr_eval = re.findall(regexpr, expr)
	for x in range(len(regexpr_eval)):
		if regexpr_eval[x] == "+" or regexpr_eval[x] == "-":
			answer += regexpr_eval[x]
		else:
			answer += str(digilog.whole_evaluate(str(decimal_separate(regexpr_eval[x])[0]), base) + digilog.decimal_evaluate(str(decimal_separate(regexpr_eval[x])[1]), base))
	return eval(answer)

main()