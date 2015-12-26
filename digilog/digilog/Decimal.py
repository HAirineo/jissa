# Module to convert decimal digits to their base-10 equivalent
def decimal_evaluate(expr, base):
	decimal = 0
	x = 0
	y = -1
	while x < len(expr) and (abs(y) - 1) < len(expr):
		decimal += float(expr[x]) * (float(base) ** y)
		x += 1
		y -= 1
	return decimal