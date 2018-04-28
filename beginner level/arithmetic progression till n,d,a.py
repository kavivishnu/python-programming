n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
s=0
for i in range(1,n+1):
   z=a+(i-1)*d
   s=s+z
print (s)
