#stones
stones=int(input("Enter number of stones: "))
i=1
total=0
while True:
    total=total+i
    if total >= stones:
        print("Ramesh won")
        break
    total=total+i*2
    if total >= stones:
        print("Suresh won")
        break
    i=i+1