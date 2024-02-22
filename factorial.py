num = int(input("Ədədi daxil edin:"))

factorial = 1


if num < 0:
   print("Factorial mənfi ola bilməz!")
elif num == 0:
   print("0 factorial 1-ə bərabərdir.")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("Factorialın nəticəsi",factorial,"edir.")