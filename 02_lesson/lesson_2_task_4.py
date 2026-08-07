def fizz_buzz(n):
    """
    Печатает числа от 1 до n.
    Вместо чисел, кратных 3, печатает Fizz.
    Вместо чисел, кратных 5, печатает Buzz.
    Вместо чисел, кратных 3 и 5, печатает FizzBuzz.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Пример вызова

num = int (input ("Введите число: "))
fizz_buzz(num)
