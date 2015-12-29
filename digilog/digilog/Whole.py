def whole_evaluate(expr, base):
	"Returns the base-10 equivalent of the whole number"
	whole = 0; x = len(expr) - 1; y = 0
	while x >= 0 and y < len(expr):
		whole += int(expr[x]) * (base ** y)
		x -= 1
		y += 1
	return whole