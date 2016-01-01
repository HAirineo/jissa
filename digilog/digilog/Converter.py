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