import calendar


# calendar application
# view calendar dates of any month in any year

def print_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    print(f"\n{month_name} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")

    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "    "
            else:
                week_str += f"{day:2d}  "
        print(week_str)


print("Welcome to Calendar App!")

while True:
    year = int(input("\nEnter the year (YYYY): "))
    month = int(input("Enter the month (MM): "))

    if year < 1 or month < 1 or month > 12:
        print("Invalid input. Please try again.")
        continue

    print_calendar(year, month)

    choice = input("\nDo you want to view another calendar? (y/n): ")
    if choice.lower() != 'y':
        print("Goodbye!")
        break
