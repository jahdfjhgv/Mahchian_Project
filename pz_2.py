# Вариант 18. Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести полученное число.

try:
    number = int(input("Введите трехзначное число: "))

    if not (100 <= abs(number) <= 999):
        print("Ошибка: Введенное число не является трехзначным!")
    else:
        sign = -1 if number < 0 else 1
        abs_number = abs(number)

        first_digit = abs_number // 100
        remaining_digits = abs_number % 100

        result = (remaining_digits * 10 + first_digit) * sign

        print(result)

except ValueError:
    print("Ошибка: Необходимо ввести целое число!")
