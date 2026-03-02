from datetime import date


def get_century() -> int:
    while True:
        try:
            raw_value = input("Please enter a century between 1 and 99: ").strip()
            if not raw_value:
                print("Input cannot be empty. Please enter a whole number between 1 and 99.")
                continue

            century_value = int(raw_value)
            if 1 <= century_value <= 99:
                print("Thank you for your input.")
                return century_value

            print("Invalid input. Please enter a value between 1 and 99.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 99.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput canceled.")
            raise SystemExit(1)


century = get_century()

start_year = (century - 1) * 100 + 1
end_year = start_year + 99

print("The following years have three Friday the 13ths:")
for year in range(start_year, end_year):
    friday_13_count = 0
    
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            friday_13_count += 1

    if friday_13_count == 3:
        print(year)
            
