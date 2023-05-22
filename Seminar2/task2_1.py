# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
i = int(input("Введите число: "))
count = 1
pow = 1
while i:
    pow *= count
    count += 1
    i -= 1
print(pow)    
#num = int(input("Введите число: "))+1
	#flag = 1
	#if num<0:
	    #print("Введите положительное число")
	#else:
	    #while num != 1:
	     #   flag *= num - 1
	      #  num-=1
	#print(flag)