#!/usr/bin/python

def count():
    list1=input("Enter the list : ")
    print(list1)
    key=input("enter key : ")
    num=0
#    num=input("Number count to find : ")
    for x in list1:
        if key == x:
            num+=1
    print("Count is",num)

def maxmin():
    list1=input("Enter the list : ")
    print(list1)
    maxn=list1[1]
    minn=list1[1]
    for x in list1:
        if x > maxn:
            maxn = x
        if x < minn:
            minn = x
    print"max",maxn, "min",minn

def main():
#    count()
    maxmin()

if __name__ == '__main__':
    main()

