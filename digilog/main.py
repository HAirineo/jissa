import digilog, math, re

def main():
	expr = raw_input("Enter an expression: ")
	base = input("Enter the base of the numbers: ")
	target = input("Enter the target base for the result: ")
	print evaluate_expression(expr, base)
	print convert_result(evaluate_expression(expr, base), target)

def convert_hexa(expr):
	if expr == "a" or expr == "A":
		return "10"
	elif expr == "b" or expr == "B":
		return "11"
	elif expr == "c" or expr == "C":
		return "12"
	elif expr == "d" or expr == "D":
		return "13"
	elif expr == "e" or expr == "E":
		return "14"
	elif expr == "f" or expr == "F":
		return "15"
	else:
		return expr

def convert_result(result, target):
	"Returns the converted result to its target-base equivalent"
	if result / target == 0:
		return result
	else:
		answer = ""
		while not int(result / target) == 0:
			quotient = result / target
			answer = hexa_convert(str(int(result % target))) + answer
			result = quotient
		else:
			result = hexa_convert(str(int(result))) + answer
	return result;

def decimal_separate(expr):
	"Returns the separated whole number and decimal number"
			# Decimal number			Whole number
	return str(math.modf(float(expr))[0]), str(math.modf(float(expr))[1])

def evaluate_expression(expr, base):
	"Returns the evaluated expression"
	answer = "" # String to contain the answer
	regexpr = r'\d+[.]\d+|\d+|[-+/*()]' # Regex determining operators and operands
	regexpr_eval = re.findall(regexpr, expr) # Regex method finding all match
	for x in range(len(regexpr_eval)):
		if regexpr_eval[x] == "+" or regexpr_eval[x] == "-" or regexpr_eval[x] == "*" or regexpr_eval[x] == "/" or regexpr_eval[x] == "(" or regexpr_eval[x] == ")":
			# Concatenate the string as it is if it is an operand
			answer += regexpr_eval[x]
		else:
			# Convert the number first before concatenating
			answer += str(digilog.decimal_evaluate(decimal_separate(regexpr_eval[x])[0], base) + digilog.whole_evaluate(decimal_separate(regexpr_eval[x])[1], base))
	try:
		return eval(answer)
	except SyntaxError:
		return "Syntax Error!"

def hexa_convert(expr):
	if expr == "10":
		return "A"
	elif expr == "11":
		return "B"
	elif expr == "12":
		return "C"
	elif expr == "13":
		return "D"
	elif expr == "14":
		return "E"
	elif expr == "15":
		return "F"
	else:
		return expr

main()