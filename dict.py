'''def sample():
    print("Hello world !")

#functions
#block of reusable code

#1
def sample():
    print("hi")

sample()

#2
def greeting(name):
    msg="welcome"+" "+name
    print(msg)
name=input()
greeting(name)

    (or)

def greeting(arg_1="welcome",arg_2="HCL"):
    print(arg_1+" "+arg_2)

greeting()


#3
def function(s):
    l=list[s]
    k=[]
    for i in range(l):
        b=i**2
        k=b.append()
    print(k)
l=input()
function(l)

#4
def divide(num):
    if num%7==0:
        print(True)
    else:
        print(False)

k=int(input())
divide(k)

    (or)

def divide(n,m):
    if n%m==0:
        print(True)
    else:
        print(False)

divide(21,7)

#5
def square(x):
    area = x**2
    perimeter = 4*x
    print("area","perimeter")

l=input()
square(l)

#6
def sample():
    a="lahya"
    b=a[1]
    print(b)

sample()

    (or)

def fun(a="lahya"):
    print(a[1])

fun()

#7
def fun(a):
    a="LahyaSri"
    count=0
    if a[0:] == a.islower():
        count=count+1
        print(count)
    elif:
        a[0:] == a.isupper():
        count=count+1
        return count

fun(a)

#7
def fun(x):
    upper=0
    lower=0
    for i in x:
        if not(ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
            print("invalid")
        elif i.isupper():
            upper+=1
        else:
            lower+=1
    return lower,upper

c=input()
u,l=fun(c)
print("upper characters is ",u)
print("lower characters is ",l)

#
def divide(n):
    if (n % 3 == 0 and n % 5 == 0):
        print("Macropolo")
    elif n%3==0:
        print("Macro")
    elif n%5==0:
        print("polo")
    else:
        print("no")

divide(23)


#
def fun(a):
    print("area is",a*a)
    print("perimeter is",4*a)
fun(5)

#
def fun(wins,loss,draw):
    total=(wins*4)+(loss*-1)+(draw*2)
    print(total)

fun(2,1,1)



#'''










