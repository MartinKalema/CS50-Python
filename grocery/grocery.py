list = []
unique = []
def main():
    try:
        capture()
    except EOFError:
        for item in list:
            if item not in unique:
                unique.append(item)
        unique.sort()
        for item in unique:
            occurrences = list.count(item)
            print(f"{occurrences} {item.upper()}")

def capture():
    global list
    item = input(" ").strip().lower()
    list.append(item)
    capture()


main()