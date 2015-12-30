def whole_evaluate(expr, base):
	"Returns the base-10 equivalent of the whole number"
	expr = expr.replace(".0", "") # Remove the string ".0"
	whole = 0; x = len(expr) - 1; y = 0
	while x >= 0 and y < len(expr):
		whole += int(expr[x]) * (base ** y) # Positional notation
		x -= 1
		y += 1
	return whole