#John is trying to solve the arithmetic series(AP). He wants to find two things in the series
# 1. He wants to find nth terms in the series
# 2. He wants to find the sum up to the nth term.
AP=[5, 10, 15, 20, 25, 30] 
sum=0  
n = int(input("Enter number of term: "))
if n <= len(AP):
    nth = AP[n - 1] 
print("nth term is: ",nth)
     
for i in range(n):
    sum=sum+AP[i]
print("The sum of the first terms is: ",sum)




