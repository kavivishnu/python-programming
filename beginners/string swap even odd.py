a = input("Enter the String:")
f=''.join([c[1] + c[0] for c in zip(a[::2], a[1::2])])
print(f)
