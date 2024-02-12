def main():
    calculate()


def calculate():
    try :
        fraction = input("Fraction:").split("/")

        numerator = 0
        denominator = 0

        # Check whether the characters are digits and not alphabetical
        if fraction[0].isdigit() and fraction[1].isdigit():
            numerator = int(fraction[0])
            denominator = int(fraction[1])
        else:
            print("The numerator and denominator must not be a decimal")
            calculate()

        if (numerator <= denominator):
            percentage = int(round((numerator/denominator) * 100, 0))
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
        else:
            calculate()

    except ZeroDivisionError or ValueError:
        print("You either divided by zero or inserted a non-fraction.")


main()