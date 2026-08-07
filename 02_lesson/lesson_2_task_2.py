def is_year_leap(num: int) -> bool:
    return True if num % 4 == 0 else False

year = int (input ("Введите год: "))

result = is_year_leap(year)
print(f"{year}: {result}")
