from datetime import date


century = int(input("Please enter a century between 1 and 100: "))

start_year = century * 100
end_year = start_year + 99

for year in range(start_year, end_year + 1):
    friday_13_count = 0

    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            friday_13_count += 1

    if friday_13_count == 3:
        print(year)
            
