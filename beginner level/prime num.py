n=int(input(""))
f=0
i=1
for i in range(2,n//2):
   if((n%i)==0):
      f=f+1
      break
if(f==0):
   print("yes")
else:
   print("no")
