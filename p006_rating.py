#!/usr/bin/python

print "enter ratings (out of 5) for different skills"
s1,s2,s3,s4,s5 = input("Python, C, C++, Ruby, Bash").split()
print s1,s2,s3,s4,s5
rat = (int(s1) + int(s2) + int(s3) + int(s4) + int(s5)) / 5
print rat
if rat == 5:
    print "Exceptional!!"
elif rat >= 4 and rat < 5:
    print "Excellent!!"
elif rat >= 3 and rat < 4:
    print "Good"
elif rat >= 2 and rat < 3:
    print "Average"
elif rat >=1 and rat <2:
    print "Below Average"
else:
    print "Poor"
