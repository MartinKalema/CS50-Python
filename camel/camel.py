variableName = input("camelCase: ")

result = []

for letter in variableName:
    if letter.isupper():
        result.append("_")
        result.append(letter.lower())
    else:
        result.append(letter)

# join the elements inside the iterable into one string
print(''.join(result))




