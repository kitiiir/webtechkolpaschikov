import random
sum = 0
numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)
delitel = int(input("Введите число для деления: "))
for number in numbers:
    if number % delitel == 0:
        sum = sum + number
print("Сумма чисел, делящихся на ", delitel," = ", sum)
input()