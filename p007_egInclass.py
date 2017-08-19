#!/usr/bin/python

for x in range(1,10):
    print x
    if x % 7 == 0:
        break
else:
    print "success"
x=1
while x!=8:
    if x % 7 == 0:
        break;
    print x
    x+=1
else:
    print "else of while"

def add(a,b=10):
    return a-b
res = add(1,2)
print "result is",res,"of type",type(res)
res = add(12)
print "result is",res,"of type",type(res)
res = add(b=10,a=20)
print "result is",res,"of type",type(res)
res = add(10,20)
print "result is",res,"of type",type(res)



def mul(a=1,b=1,c=1,d=1,e=1):
    return(a*b*c*d*e)

res = mul()
print "result is",res,"of type",type(res)

res = mul(1,2)
print "result is",res,"of type",type(res)

res = mul(1,2,3)
print "result is",res,"of type",type(res)

res = mul(1,2,3,4)
print "result is",res,"of type",type(res)

res = mul(1,2,3,4,5)
print "result is",res,"of type",type(res)

def sub(a,b,c=10):
    return a+b+c

res=sub(10,10)
print res
res=sub(10,b=30)
print res
res=sub(b=10,a=20)
print res
res=sub(1,c=200,b=100)
print res
res=sub(b=30,c=20,a=1)
print res
res=sub(b=20,c=20,a=0)
print res


def varadd(*args):
    print(type(args))
    sum=0
    for x in args:
        print x
        sum+=x
        print sum
varadd(1,2,3)
varadd(1,2,3,4,5,6)
varadd()
#varadd("ro","sh","an")
