# Вы пользетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получати билет с номером. Счастливым билетом
# называют билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 
# счастливый, т.к. 3+8+5 = 9 +1 +6. Напишите программу, которая проверяе счастливость билета.
n = input("введите число : ")
n = int(n)
c = n%1000
d = c %10
c= c//10
e = c %10
f = c//10
# print(d+e+f)
n2= n//1000
c1 = n2%10
n2 = n2 //10
b = n2%10
a = n2//10
# print(c1+a+b)
if d+e+f==c1+a+b:
 print("УРА !!!Счастливый билет")
else:
 print("Увы..") 