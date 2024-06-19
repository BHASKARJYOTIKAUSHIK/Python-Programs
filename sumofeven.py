n=int(input("Enter number:"))
# b=0
# for i in range(0,n+1):
#     if i%2==0:
#         b+=i
#     else:
#         pass
a=0
for i in range(0,n+1):
    if i%2==0:
        pass
    else:
        a+=i
c=n*(n+2)//4
print(f"Sum of all even numbers till {n} is ",c)
print(f"Sum of all odd numbers till {n} is ",a)