# This module converts the given expression to its decimal equivalent
# However, this module is currently designed for whole number only
def whole_evaluate(expr, base):
	whole = 0
	x = len(expr) - 1
	y = 0
	while x >= 0 and y < len(expr):
		whole += int(expr[x]) * (base ** y)
		x -= 1
		y += 1
	return whole