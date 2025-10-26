# ques1: A wire is in the form of arc ..........area of square.
angle = int(input("Enter angle: "))
radius = int(input("Radius: "))
pi=3.14
low = (angle/360)*2*pi*radius #low=lengthofwire
side = low/4
area=side**2
print("area of square is :  ",area)