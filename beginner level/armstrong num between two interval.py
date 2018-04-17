l,u=input().split(" ")
for num in range(int(l)+1,int(u)):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if num == sum:
         print(num,end=(' '))
