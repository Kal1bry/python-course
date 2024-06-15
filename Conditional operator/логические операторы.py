#1
a = int(input())

if -1 < a < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

#2
n = int(input())

if n <= -3 or n >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

#3
n = int(input())

if -30<n<=-2 or 7<n<=25:
    print('Принадлежит')
else:
    print('Не принадлежит')

#4
n = int(input())

if 1000<=n<=9999 and (n%7==0 or n%17==0):
    print('YES')
else:
    print('NO')

#5
s_1 = int(input())
s_2 = int(input())
s_3 = int(input())

if (s_1 + s_2 > s_3) and (s_1 + s_3 > s_2) and (s_2 + s_3 > s_1):
    print("YES")
else:
    print("NO")

#6
year = int(input())

if (year%4==0 and year%100!=0) or year%400==0:
    print("YES")
else:
    print("NO")

#7
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if x1==x2 or y1==y2:
    print("YES")
else:
    print("NO")

#8
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

x = x2 - x1
y = y2 - y1
if (-1 <= x <= 1) and (-1 <= y <= 1):
    print("YES")
else:
    print("NO")
