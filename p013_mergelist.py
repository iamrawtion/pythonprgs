#!/usr/bin/python

def compare():
    list1,list2=input("Enter 2 lists")
    if type(list1) != list or type(list2) != list:
        print "lists not enetered"
        return 0
    list1.sort()
    list2.sort()
    if len(list1)!=len(list2):
        print "Lists are not same"
        return 0
    print list1, list2
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            continue
        break
    else:
        print "They are same"
        return 1
    print "They are not same"
    return 0

def merge():
    list1,list2=input("Enter 2 lists")
    if type(list1) != list or type(list2) != list:
        print "lists not enetered"
        return 0
    list1.sort()
    list2.sort()
    list3=[]
    i=0
    j=0
#    for k in range(len(list1+list2)) and i in range(len(list1)) and j in range(len(list2)):
    while i < len(list1) and j < len(list2):
        if list1[i]<list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    print list3

def main():
#    compare()
    merge()

if __name__ == '__main__':
    main()
