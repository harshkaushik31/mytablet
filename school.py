#code for finding largest and smallest in a list
"""L=[]
n=int(input("Enter the length of list "))
for i in range(n):
    d=int(input("Enter number:=> "))
    L.append(d)
print(L)
max1=0
min1=L[0]
for i in range(n):
    if L[i]>max1:
        max1=L[i]
for i in range(n):
    if L[i]<min1:
        min1=L[i]
print("The largest number is ",max1)
print("The smallest number is ",min1)
"""

#for largest and smallest in a list
"""N=int(input("Enter the number of elements "))
L=[]
for i in range(N):
    n=int(input("Enter the number "))
    L.append(n)
print("The Entered List is ",L)

max1=0
min1=L[0]
for i in range(N):
    if L[i]>max1:
        max1=L[i]
for i in range(N):        
    if L[i]<min1:
        min1=L[i]
print("The maximum number is",max1,"The minunum number is",min1)"""

# for searching of item in a tuple
L=[]
n=int(input("Enter the number of elements "))
for i in range(n):
    d=input("Enter the element ")
    L.append(d)
print("The entered list is",L)
T=tuple(L)
print("The derived tuple is",T)
sts=False
itm=input("Enter the item to search for ")
for i in range(n):
    if itm==T[i]:
        sts=True
        print("Item ",itm," found at index ",i," at position ",i+1)
if sts==False:
    print("Sorry, item is not in the list")





























