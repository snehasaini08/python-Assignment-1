# Given three numbers find the maximum of three numbers using the ternary operater.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
maximum = a if (a>b and a>c) else (b if b>c else c)
print("maximun number is: ",maximum)