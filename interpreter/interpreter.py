expression = input("Expression: ").lower().strip()

# split 
expression = expression.split(" ")

# get the first and second argument.
first_argument = float(expression[0])
second_argument = float(expression[2])

# conditionals
if expression[1] == "+":
    print(first_argument + second_argument)
elif expression[1] == "-":
    print(first_argument - second_argument)
elif expression[1] == "/":
    print(first_argument / second_argument)
elif expression[1] == "*":
    print(first_argument * second_argument)