import random

def my_sum(arr: list[float|int]) -> float|int:
    print(arr)
    sum = 0
    for number in arr:
        sum = sum + number
    print("Сумма элементов = ", sum)
    input()

def my_avg(arr: list[float|int]) -> float|int:
    print(arr)
    sum = 0
    for number in arr:
        sum = sum + number
    cnt = 0
    for number in arr:
        cnt = cnt + 1
    avg = sum / cnt
    print("Среднее арифметическое = ", avg)
    input()

def my_min(arr: list[float|int]) -> float|int:
    print(arr)
    min = arr[0]
    for number in arr:
        if number < min:
            min = number
    print("Минимальный элемент = ", min)
    input() 

def my_max(arr: list[float|int]) -> float|int:
    print(arr)
    max = arr[0]
    for number in arr:
        if number > max:
            max = number
    print("Максимальный элемент = ", max)
    input() 

def my_max_filter(arr: list[float|int], num: float|int) -> list[float|int]:
    print(arr)
    filterlist = []
    for number in arr:
        if  number > num:
            filterlist.append(number)
    print("Новый список: ", filterlist)
    input()

def my_len(arr: list[float|int]) -> int:
    print(arr)
    cnt = 0
    for number in arr:
        cnt = cnt + 1
    print("Длина списка = ", cnt)
    input()

mylist = [random.randint(1, 100) for _ in range(10)]
print(mylist)
my_sum(mylist)
my_avg(mylist)
my_min(mylist)
my_max(mylist)
num = int(input("Введите число для фильтра: "))
my_max_filter(mylist, num)
my_len(mylist)
input()