def main():
    print(convert(input("Write something: ")))

def convert(input):
    input = input.replace(":)", "\N{slightly smiling face}").replace(":(", "\N{slightly frowning face}")
    return input 

main()