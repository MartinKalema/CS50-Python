text = input("Input: ")

result = []

def isVowel(letter):
    list = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    if letter in list:
        return True
    else: 
        return False


for letter in text:
    if isVowel(letter) is not True:
        result.append(letter)

print("Output: ", ''.join(result))
        