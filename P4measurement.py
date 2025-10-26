#P4.Measurement Conversion
# #Write a program that converts and prints user given measurement in inches into
#1. foot(12 inches)
#2. yard(36 inches)
#3. centimetres(2.54 inches)
#4. meter(39.37 inches)
# Program: Measurement Conversion (without f-strings)

inches = float(input(" Measurement in inches: "))
foot = inches / 12
yards = inches / 36
centimetres = inches * 2.54
metres = inches / 39.37

print("Foot: ", foot)
print("Yards: ", yards)
print("Centimetres:  ", centimetres)
print("Metres: ", metres)
