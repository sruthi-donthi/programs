"""n=int(input(""))
a=input("enter any string:")
print(a*n)"""

"""a=input("enter any string:")
print(a[0])
print(a[-1])"""

a=[]
for i in range(5):
    n=int(input("enter any number:"))
    a.append(n)
print("minimum is:",min(a))
print("maximum is:",max(a))

"""a=int(input("enter any number:"))
for i in range(1,11):
    print(a,"X",i,"=",(a*i))"""

"""a=input("enter signal color:")
if(a=="red"):
    {
        print("stop")
    }
elif(a=="orange"):
    {
        print("ready to move")
    }
elif(a=="green"):
    {
        print("move")
    }
else:
    {
        print("no color")
    }"""

"""a=input("enter any operator:")
b=int(input("enter num1:"))
c=int(input("enter num2:"))
if(a=="+"):
    print(b+c)
elif(a=="-"):
    print(b-c)
elif(a=="*"):
    print(b*c)
elif(a=="/"):
    print(b/c)
else:
    print("no operator found")"""

"""a=int(input("enter marks of the student:"))
if(a>=90):
    print("Ex")
elif(a<90 and a>=80):
    print("A")
elif(a<80 and a>=70):
    print("B")
elif(a<70 and a>=60):
    print("C")
elif(a<60 and a>=50):
    print("D")
elif(a<50 and a>=40):
    print("E")
else:
    print("REMIDIAL")"""

'''a="RGUKT RK Valley"
b=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in b:
        continue
    print(i)''' 

"""n=int(input("enter number:"))
for i in range(n+1):
    if(i%2!=0):
        continue
    print(i)"""

'''a=0
while(a>=0):
   a= int(input("enter any number:"))'''