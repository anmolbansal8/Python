""" #even odd number
n=int(input("please input a nmuber:"))
if n%2==0:
    print("even number")
else:
    print("odd number")
 
    #biggest number
n=int(input("please enter first nmuber:"))
s=int(input("please enter second nmuber:")) 
if n>s:
    print(n, "is greater than ",s)
else:
     print(n, "is less than",s)

# swap two variables

n=int(input("please enter first nmuber:"))
s=int(input("please enter second nmuber:"))
y=n
n=s
s=y
print("after swapping :",n)
print("after swapping",s)

#area of circle
r=int(input("please input a nmuber:"))
c=3.14*r*r
print (c)

#square root 
n=int(input("please input a nmuber:"))
c=n**0.5
print(c)

 #area of rectangle
l=int(input("please input length:"))
b=int(input("please input breath:"))
r=l*b
print(r)
 
 #amount,interest,time
a=int(input("please input amount:"))
y=int(input("please input year:"))
r=int(input("please input rate:"))
c=(a*y*r)/100
print(c)

#compound interest
p=float(input("please input principal:"))
y=float(input("please input year:"))
r=float(input("please input rate:"))
amount=p*(1+r/100)**y
CI=amount-p
print(CI)

 #temperature
c=float(input("please input celsius:"))
f=(9/5*c)+32
print(f)
 
#for series loop
 
for x in range(7):
 print(x)
 
for x in range(1,23,2):
 print(x)

for x in range(10,0,-1):
 print(x)

for x in range(1,31,3):
 print(x)

for x in range(28,0,3):
 print(x)


#while loop 
i=0
while i<6:
    i+=1
    print(i)
i=-1
while i<21:
    i+=2
    print(i)

i=1
while i>10:
    print(i)
    i-=1

#km to miles
c=int(input("enter a value:"))
a=c/1.609
print(a)
"""

#using days
a=int(input("please enter a number:"))
if a==1:
    print("it is a monday")
elif a==2:
    print("it is a tuesday")
elif a==3:
    print("it is a wednesday")
elif a==4:
    print("it is a thusday")
elif a==5:
    print("it is a Friday")
elif a==6:
    print("it is a Saturday")
else:
    print("it is sunday")