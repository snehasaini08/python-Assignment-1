def reverse(k):
    rev = 0
    while k > 0 :
        dig= k%10
        rev=rev*10+dig
        k=k//10
        return rev
    num=int(input("Enter a number to reverse: "))

    for i in range(num):
        a=int(input("first number: "))
        b=int(input("second number: "))
        arev=reverse(a)
        brev=reverse(b)
        sum=arev+brev
        sumrev=reverse(sum)
        print("Sum of reversed number is: ",sumrev)