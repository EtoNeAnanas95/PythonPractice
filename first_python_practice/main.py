import math
from re import match

print("Для прекращение работы калькулятора, напишите слово (да)")
Cheker = "ответ убил"
print("1. сложение ")
print("2. вычитание ")
print("3. умножение ")
print("4. деление ")
print("5. возведение в степень ")
print("6. корень числа ")
print("7. факториал числа ")
print("8. синус числа ")
print("9. косинус числа ")
print("10. тангенс числа ")
# В Нигерии никогда не доставляют пиццу на дом, потому что, часто вместе с пиццей съедают курьера)))
try:
    c = int(input("выберите дейсвтие: "))
    while Cheker != "yes" and Cheker != "да" and Cheker != "yea" and Cheker != "lf":
        match c:
            case 1:
                try:
                    print("Введите первое число")
                    a = float(input())
                    print("Введите второе число")
                    b = float(input())
                    Q = a + b
                    print("Ответ: ", a, ' + ', b, ' = ', Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 2:
                try:
                    print("Введите первое число")
                    a = float(input())
                    print("Введите второе число")
                    b = float(input())
                    Q = a - b
                    print("Ответ: ", a, ' - ', b, ' = ', Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные знечения))))")
            case 3:
                try:
                    print("Введите первое число")
                    a = float(input())
                    print("Введите второе число")
                    b = float(input())
                    Q = a * b
                    print("Ответ: ", a, ' * ', b, ' = ', Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 4:
                try:
                    print("Введите первое число")
                    a = float(input())
                    print("Введите второе число")
                    b = float(input())
                    if b == 0:
                        print("Ах маленький пернатый проказник, на ноль делить нельзя))))")
                        print("Введи пожалуйста другой делитель")
                        break
                    Q = a / b
                    print("Ответ: ", a, ' / ', b, ' = ', Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 5:
                try:
                    print("Введите первое число")
                    a = float(input())
                    print("стпень числа")
                    b = int(input())
                    Q = a ** b
                    print("Ответ ", Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 6:
                try:
                    print("Введите первое число")
                    a = float(input())
                    Q = a ** 0.5
                    print("Ответ ", Q)
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные знаяения))))")
            case 7:
                try:
                    print("Введите первое число")
                    a = int(input())
                    from math import factorial
                    print("Ответ ", factorial(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 8:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import sin
                    print("Ответ ", sin(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 9:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import cos
                    print("Ответ ", cos(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
            case 10:
                try:
                    print("Введите число")
                    a = int(input())
                    from math import tan
                    print("Ответ ", tan(a))
                    print("Завершить работу?")
                    Cheker = str(input())
                except ValueError:
                    print("Ах маленький пернатый проказник, введи нормальные значения))))")
except ValueError:
    print("Ах ты пернатый проказник, введи нормальное значение")
    print("Штирлиц всю ночь топил камин")
    print("на утро камин утонул")