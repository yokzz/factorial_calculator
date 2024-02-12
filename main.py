def factorial(num):
    if num == 0:
        return 1
    else: 
        return num * factorial(num-1)
num = int(input("Введіть число, факторіал якого потрібно знайти: "))
print(f"Факторіал числа {num} дорівнює {factorial(num)}")