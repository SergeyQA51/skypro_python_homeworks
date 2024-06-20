def is_year_leap(year):
    if (year % 4) == 0:
        return True
    else:
        return False

year_to_check = 2020
leap_year = is_year_leap(year_to_check)

print(f"год {year_to_check}: {leap_year}")