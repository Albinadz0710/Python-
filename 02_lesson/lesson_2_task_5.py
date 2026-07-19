def month_to_season(month):
    """
    Принимает номер месяца (1-12) и возвращает название сезона.
    """
    if month in [12, 1, 2]:
        print("Зима")
    elif month in [3, 4, 5]:
        print("Весна")
    elif month in [6, 7, 8]:
        print("Лето")
    elif month in [9, 10, 11]:
        print("Осень")
    else:
        print("Неверный номер месяца")
    

# Примеры использования
month = int (input ("Введите номер месяца: "))
month_to_season(month)
