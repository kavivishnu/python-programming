a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
if((a>b) and  (a>c)):
    largest=a
elif((b>c) and (b>a)):
     largest=b
else:
     largest=c
print( "largest numeber between",a,",",b,"and",c,"is",largest)
