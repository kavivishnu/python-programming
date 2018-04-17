a,b=input().split(" ")
for num in range(int(a)+1,int(b)):
   if num > 0:
     for i in range(2,num):
       if (num % i) == 0:
          break
     else:
         print(num,end=(' '))
