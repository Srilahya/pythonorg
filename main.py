# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



list_1=[1,2,3,4,2,4,6]
set_a=set(list_1)
print(set_a)

k=input("enter numbers:")
l=k.split(" ")
set=set(l)
print(set)



list_1=input([])
list_2=input([])
set1=set(list_1)
set2=set(list_2)
symmetric_diff = set1 - set2
print(symmetric_diff)




k=input([22,33,44,55,99])
l=input([66,77,88,99,33])
m=k.split(" ")
n=l.split(" ")
set1=set(k)
set2=set(n)
intersection=(set1 | set2)
print(intersection)


k=[1,2,3,4]
l=[3,4]
m=set(k)
n=set(l)
o=m-n
print("original list: ", o)


k=list(map(int,input("enter:").strip().split(" ")))
set1=set(k)
l=list(map(int,input("enter:").strip().split(" ")))
set2=set(l)
intersection = set1 & set2
print(intersection)
m=list(intersection)
print(m)


#REMOVE DUPLICATE NUMBERS IN THE LIST
list_1=[1,2,3,2]
set=set(list_1)
list_2=list(set)
print(list_2)

#REMOVE A LIST OF NUMBERS IS PRESENT IN THE SET READ INPUTS  AS COMMA SEPERATED
#REMOVE THE ELEMENTS OTHERTHAN THE NUMBERS
l=[1,2,3,"@","#",6]
l1=l.copy()
for i in range(len(l)):
    if str(l[i].isdigit:
        print(l)
    else:
        l1.remove(l)
        print(l1)



l1=input()
l2=[]
for i in l1:
    if i.isdigit()==True:
        l2.append(i)
    print(l2)
set_a={1,2,3,4,5,6}
set_b={3,4,5}
print(set_a.issuperset(set_b))


list1=["@","#",2,4,5]
list2=list1.copy()
for i in range(len(list1)):
    if str(list1[i].isdigit()):
        print(list1)
    else:
        list2.remove(list1)
    print(list2)








set_a={1,2,3}
set_b={4,5,6}
print(set_a.isdisjoint(set_b))



set_a={1,2,3,4,5,6}
set_b={4,5,6}
print(set_b.issubset(set_a))


set_a={1,2,3,4,5,6,7,8,9}
set_b={4,5,6}
print(set_a.issuperset(set_b))


list1=list(map(int,input().split()))
k=len(list1)
list3=int(input())
for i in range(k):
    for j in range(i+1,k):
        if (list1[i]+list1[j]==list3):
            list3=(list1[i],list1[j])
print(k)

list_a=["Five","Six"]
print(list_a[0][1])




l_1=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l=l_1[0]
    l_1.remove(l)
    l_1.append(0,l)
    print(l_1)


set_a=list(map(int,input().strip().split()))
set1=list(set_a)
set_b=list(map(int,input().strip().split()))
set2=list(set_b)
set_c=list(map(int,input().strip().split()))
set3=list(set_c)
intersection=set1 & set2
print(intersection)
i=intersection & set3
print(i)

l1={1,2,3,4}
l2={4,5,6}
l3={4,7,8,9}
k= l1 & l2 & l3
print(k)


l1=list(map(int,input().split()))
print(min(l1))

l1=[(5,6),(7,8),(2,3)]
min_tuple=min(l1,key,value)
print(min_tuple)


dict_a={"name":"lahya","rollno":430}
print(dict_a)
dict_a.update({"rollno":405})
print(dict_a)

#update a key value
dict_a={"name":"lahya","colour":"blue"}
dict_a["name"]="ammu"
print(dict_a)


#deleting a key
dict_a = {"name": "lahya", "colour": "blue"}
del dict_a["name"]
print(dict_a)


#squares of keys
k=list(map(int,input().split(" ")))
dict_a={}
for key in k:
    dict_a[key]=(key**2)
print(dict_a)


k=list(map(str,input().split()))
l=list(map(str,input().split()))
count=0
for i in range(len(l)):
    if l!=k:
        v=l[0]
        l.remove(v)
        l.append(v)
        count+=1
print(count)



m=list(map(int,input("enter:").split("")))
n=list(map(int,input("enter:").split("")))
list1=[]
for i in range(m,n):
    s=i*i
    if s>m & s<n:
        list1.append(s)
print(list1)



k=[1,2,3,4,5]
l=int(input())
for i in range(l):
    m=k[0]
    k.remove(m)
    k.append(m)
    print(k)



m=input()
n=input()
t=0
while(m!=n):
    l=m[0]
    m=m[1:]
    m+=l
    t+=1
print(t)


if False:
    print("good")
print("bye")
a=1
while a<=6:
    print("hi")
    a=a+1


#
a=1
while(a<=10):
    print(a)
    a+=1

#
    a=5
    for i in range(1,a+1,1):
        for j in range(1,i+1):
            print(j,end=' ')
        print("")


a=10
for i in range(1,a+1,1):
    for j in range(1,i+1):
        print(j,end=' ')
    print("")

a=[]
for i in range(1,100):
    sum+=1
    k=a.append()
    print(k)

a=1
c=0
for i in range(1,a+1,1):
    i+=1
    print(c)





