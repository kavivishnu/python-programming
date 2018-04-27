n=int(input("enter the num : "))
e=list(map(int,str(n)))
s=list(map(lambda x:x**3,e))
if(sum(s)==n):
  print("yes")
else:
  print("no")
