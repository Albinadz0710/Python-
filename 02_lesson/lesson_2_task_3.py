import math

def square(side):
    """
    Вычисляет площадь квадрата.
    Если сторона не целая, округляет результат вверх.
    """
    area = side * side
    return math.ceil(area)

# Примеры использования
side1 = 4
result1 = square(side1)
print(f"Сторона: {side1}, Площадь: {result1}")

side2 = 4.5
result2 = square(side2)
print(f"Сторона: {side2}, Площадь: {result2}")

side3 = 3.2
result3 = square(side3)
print(f"Сторона: {side3}, Площадь: {result3}")
