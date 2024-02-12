# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return starts_with_two_letters(plate) and check_character_count(plate) and check_punctuation(plate) and does_not_start_with_zero(plate)

# Checks condition 1
def starts_with_two_letters(plate):
    return plate[0:2].isalpha()


# Checks condition 2
def check_character_count(plate):
    character_count = 0
    for character in plate:
        if character.isdigit() or character.isalpha():
            character_count += 1
    return character_count >= 2 and character_count < 7


# Checks condition 3
def does_not_start_with_zero(plate):
    middle_index = int(len(plate)/2)
    return plate[middle_index] != "0"


# Checks condition 4
def check_punctuation(plate):
    return plate.isalnum()


main()
