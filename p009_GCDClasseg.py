#!/usr/bin/python

def GCD(no1, no2):
    while no1 != no2:
        if no1 > no2:
            no1=no1-no2
        else:
            no2=no2-no1
    return no1

def main():
    n1,n2=input("Enter 2 numbers")
    gcd=GCD(n1,n2)
    print(gcd)

if __name__ == '__main__':
    main()


