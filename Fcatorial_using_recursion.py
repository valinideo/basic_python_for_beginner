def fact(n):
    if n==1 or n==0:
        return 1
    else: 
        return fact(n-1)*n
a = int (input ("enter a number "))
print(f"the factorial of {a} is = ",fact(a)) 