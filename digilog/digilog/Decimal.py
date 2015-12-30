def decimal_evaluate(expr, base):
	"Returns the base-10 equivalent of decimal digits"
	expr = expr.replace("0.", "") # Remove the string "0."
	decimal = 0; x = 0; y = -1
	while x < len(expr) and (abs(y) - 1) < len(expr):
		decimal += float(expr[x]) * (float(base) ** y) # Positional notation
		x += 1
		y -= 1
	return decimal