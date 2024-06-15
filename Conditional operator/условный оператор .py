#1
n = int(input())
k = int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
else:
    print("Don't know")

#2
side1=int(input())
side2=int(input())
side3=int(input())
if side1==side2==side3:
    print("Равносторонний")
elif side1==side2 or side1==side3 or side2==side3:
    print("Равнобедренный")
else:
    print("Разносторонний")

#3
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2>n3 or n1<n2<n3:
    print(n2)
elif n2<n1<n3 or n2>n1>n3:
    print(n1)
else:
    print(n3)

#4
n = int(input())
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("31")
elif n==4 or n==6 or n==9 or n==11:
    print("30")
else:
    print("28")

#5
w = int(input())
if w < 60:
    print("Легкий вес")
elif 60 <= w < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

#6
a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')

#7
a, b = input(), input()

if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
    print('зеленый')
elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
    print(a)
else:
    print('ошибка цвета')

#8
n = int(input())
if 1 <= n <= 10 or 19 <= n <= 28:
    if n%2==0:
        print("черный")
    elif n%2==1:
        print("красный")
    else:
        print("ошибка ввода")
elif 11 <= n <= 18 or 29 <= n <= 36:
    if n%2==0:
        print("красный")
    elif n%2==1:
        print("черный")
    else:
        print("ошибка ввода")
elif n==0:
    print("зеленый")
else:
    print("ошибка ввода")

#9
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 > b1 or a1 > b2:  
    print('пустое множество')
elif a1 == b2:  
    print(a1)
elif a2 == b1: 
    print(a2)
else: 
    if a1 > a2:  
        a2 = a1
    if b1 < b2:  
        b2 = b1
    print(a2, b2)