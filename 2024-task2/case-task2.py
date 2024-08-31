import datetime

def get_birthday():
    day = int(input("Введите день рождения (число): "))
    month = int(input("Введите месяц рождения (число): "))
    year = int(input("Введите год рождения (число): "))
    return datetime.date(year, month, day)

def day_of_week(date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

def is_leap_year(year): # Проверяем вискосный ли год, без модуля calendar
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birthday):
    today = datetime.date.today()
    age = today.year - birthday.year
    if today < datetime.date(today.year, birthday.month, birthday.day):
        age -= 1
    return age

def print_date_in_stars(date):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }

    date_str = date.strftime("%d%m%Y")
    for i in range(5):
        line = ' '.join(digits[digit][i] for digit in date_str)
        print(line)

def main():
    birthday = get_birthday()
    
    print(f"Вы родились в {day_of_week(birthday)}")
    
    if is_leap_year(birthday.year):
        print(f"{birthday.year} високосный год.")
    else:
        print(f"{birthday.year} не високосный год.")
        
    age = calculate_age(birthday)
    print(f"Вам {age} лет.")
    
    print("Дата вашего рождения:")
    print_date_in_stars(birthday)

if __name__ == "__main__":
    main()
