#!/usr/bin/python

def pattern1():
    max=input("Enter the max number for star prints : ")
    i=0
    while max!=0:
        while i!=max:
            print'*\t',
	    i+=1
	    print '\n',
        max-=1

def patternabc():
    max_rows=input("Enter number of rows : ")
    i=0
    while i>max_rows:
        a=65
        while i!=row:
            print'%c'%a,
            a+=1
            i+=1
        print '\n'
        row+=1

def main():
    print"What pattern would you like to print?"
    print"\n1.\n*\n**\n***"
    print"\n2.\n  *\n **\n***"
    print"\n3.\n  *\n ***\n*****"
    print"\n4.\n***\n**\n*"
    choice=input("Enter your choice: ")
    if choice == 1 :
        pattern1()
    patternabc()

if __name__ == '__main__':
    main()
