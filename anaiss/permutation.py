# Anaiss module
# Factorial
def factorial(number):
	return (number * factorial(number - 1)) if (number > 0) else 1

# Permutation
def permutation(number, positions):
	return (factorial(number) / (factorial(number - positions)))

print(permutation(int(input("Enter number of distinct objects: ")), int(input("Enter number of positions: "))))