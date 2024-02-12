def main():
    time  = input("What time is it? ").strip()
    time_in_decimal = convert(time)

    if time_in_decimal >= 7.0 and time_in_decimal <= 8.0:
        print("breakfast time")
    elif time_in_decimal >= 12.0 and time_in_decimal <= 13.0:
        print("lunch time")
    elif time_in_decimal >= 18.0 and time_in_decimal <= 19.0:
        print("dinner time")


def convert(time):
    time = time.split(":")
    hour = float(time[0])
    minute = float(time[1])
    minute_as_decimal = minute/60
    return hour + minute_as_decimal

    

if __name__ == "__main__":
    main()
