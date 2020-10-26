#!/usr/bin/python

print ("Hello World")

dic2 = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight",
        '9': "nine", '0': "zero"}
a, b, c, d, e, f, g, h, i, j = dic2
print(f"{a},{j}")
phone_number = input("Phone: ")
for number in phone_number:
    print(dic2.get(number))
    print(dic2[number])
