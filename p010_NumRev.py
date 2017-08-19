#!/usr/bin/python

def reverse(num):
    rev = 0
    num2=num
    while num!=0:
        rem = num%10
        rev = rev*10+rem
        num=num/10
    print(rev)
    palin(num2,rev)

def palin(num2,rev):
    if num2==rev:
        print("Number is Palindrome")
    else:
        print("Not palindrome")

def main():
    num=input("Enter a number for reversing : ")
    reverse(num)

if __name__ == '__main__':
    main()

