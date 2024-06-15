#1
pass_1, pass_2 = input(), input()
if pass_1 == pass_2:
    print("Пароль принят")
else:
    print("Пароль не принят")

#2
num = int(input())
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

#3
num = int(input())
num_1 = num // 1000 % 10
num_2 = num // 100 % 10
num_3 = num // 10 % 10
num_4 = num % 10
if num_1 + num_4 == num_2 - num_3:
    print("ДА")
else:
    print("НЕТ")

#4
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#5
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if (num_2 - num_1) == (num_3 - num_2):
    print("YES")
else:
    print("NO")

#6
num_1 = int(input())
num_2 = int(input())
if num_1 > num_2:
    print(num_2)
else:
    print(num_1)

#7
num_1, num_2, num_3, num_4 = int(input()), int(input()), int(input()), int(input())
print(min(num_1, num_2, num_3, num_4))

#8
age = int(input())
if age <= 13:
    print("детство")
elif age <= 24:
    print("молодость")
elif age <= 59:
    print("зрелость")
elif age > 59:
    print("старость")

#9
sum = 0
num_1, num_2, num_3 = int(input()), int(input()), int(input())
if num_1 > 0:
    sum = sum + num_1
if num_2 > 0:
    sum = sum + num_2
if num_3 > 0:
    sum = sum + num_3
print(sum)

