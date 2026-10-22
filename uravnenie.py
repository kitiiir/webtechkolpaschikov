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

def viet(b,c, limit=1000):
  for x1 in range(-limit, limit + 1):
    for x2 in range(-limit, limit + 1):
      if x1 + x2 == -b and x1 * x2 == c:
        print("Корни уравнения x1 = ", x1, " x2 = ", x2)
        return x1, x2
  return None

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
            viet(b,c)
        else: print("Неверная команда")
    input()