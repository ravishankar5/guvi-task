n=int(input("Enter the range"))
a=0
b=1
sum=0
print(a)
print(b)
for i in range(n):
    sum=a+b
    a=b
    b=sum
    print(sum)
