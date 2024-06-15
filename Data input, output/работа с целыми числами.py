#1
n = int(input())
print(n, n+1, n+2, sep="\n")
#2
print(int(input())+int(input())+int(input()))
#3
a = int(input())
print("Объем =", a*a*a)
print("Площадь полной поверхности =", 6*a*a)
#4
a = int(input())
b = int(input())
print(3*pow((a+b),3)+275*pow(b,2)-127*a-41)
#5
n = int(input())
print("Следующее за числом", n, "число:", n+1)
print("Для числа", n, "предыдущее число:", n-1)
#6
print((int(input())+int(input())+int(input())+int(input()))*3)
#7
a = int(input())
b = int(input())
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
#8
print(int(input())+int(input())*(int(input())-1))
#9
x = int(input())
print(x, x*2, x*3, x*4, x*5, sep="---")
#10
print(int(input())*int(input())**(int(input())-1))
#11
print(int(input())//100)
#12
sm = int(input())
oranges = int(input())
print(oranges // sm, oranges % sm, sep="\n")
#13
n = int(input())
print((n + 1) // 2)
#14
t = int(input())
print(t, "мин - это", t // 60, "час", t % 60, "минут.")
#15
n = int(input())
print(((n - 1) // 4) + 1)
#16
n = int(input())
print("Сумма цифр =", n // 100 % 10 + n // 10 % 10 + n // 1 % 10)
print("Произведение цифр =",(n // 100 % 10) * (n // 10 % 10) * (n // 1 % 10))
#17
n = int(input())
print(n // 100 % 10, n // 10 % 10, n // 1 % 10, sep="")
print(n // 100 % 10, n // 1 % 10, n // 10 % 10, sep="")
print(n // 10 % 10, n // 100 % 10, n // 1 % 10, sep="")
print(n // 10 % 10, n // 1 % 10, n // 100 % 10, sep="")
print(n // 1 % 10, n // 100 % 10, n // 10 % 10, sep="")
print(n // 1 % 10, n // 10 % 10, n // 100 % 10, sep="")
#18
n = int(input())
print("Цифра в позиции тысяч равна", n // 1000 % 10)
print("Цифра в позиции сотен равна", n // 100 % 10)
print("Цифра в позиции десятков равна", n // 10 % 10)
print("Цифра в позиции единиц равна", n % 10)