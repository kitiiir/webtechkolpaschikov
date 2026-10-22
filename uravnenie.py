def discr(a,b,c):
    d = (b*b)-4*a*c
    if d<0:
        print("Дискриминант <0, корней нет.")
        return
    else:
        if d==0:
            x = (-b)/(2*a)
            print("Корень уравнения x =", x)
            return
        else:
            x1 = ((-b)+(d**0.5))/(2*a)
            x2 = ((-b)-(d**0.5))/(2*a)
            print("Корни уравнения x1 = ", x1," x2 = ", x2)
            return 

while(True):
    print("Вычисление квадратного уравнения: введите коэффиценты a, b, c: ")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    command = int(input("Метод решения: 1 - через дискрименант, 2 - через теорему Виета"))
    if command == 1:
        discr(a,b,c)
    else:
        if command == 2:
            viet(a,b,c)
        else: print("Неверная команда")
    input()