# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b//2) * power(a, b//2)
    else:
        return a * power(a, b//2) * power(a, b//2)

a = int(input("Ведите первое число: "))
b = int(input("Введите второе число: "))

print(power(a, b))