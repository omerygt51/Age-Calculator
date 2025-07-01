import datetime

first_name = input("Your first name: ")
last_name = input("Your last name: ")
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

today = datetime.date.today()
birth_date = datetime.date(birth_year, birth_month, birth_day)

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"\nHello {first_name} {last_name}, your age is: {age}")

# Birthday check
if (today.month, today.day) == (birth_month, birth_day):
    print("🎉 Happy Birthday!")
else:
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    remaining_days = (next_birthday - today).days
    print(f"🎂 {remaining_days} day(s) left until your next birthday.")

# Made by Ömer Yiğit Üzümcü