#!/usr/bin/python
no1,no2=input("enter num1 and num2")
#no2=input("enter num2")
#print("%d-%d is %d"%(no1,no2,no1-no2))

if no1 > no2:
    print("%d"%(no1-no2))
elif no2 > no1:
    print("%d"%(no2-no1))
else:
    print("number equal or invalid input")
