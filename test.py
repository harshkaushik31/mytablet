st = []
n = int(input("Enter number of elements to insert intot the stack: "))
for i in range(n):
    inp = input('Enter the element: ')
    st.append(inp)
print('The stack is ')
for i in range(len(st)-1,-1,-1):
    print(st[i])
n2 = int(input("Enter the number of elements to pop: "))
for i in range(n2):
    if st == []:
        print("The stack is empty!")
    else: 
        print("The poped elements are: ",st.pop())
print('The final stack is: ')
for i in range(len(st)-1,-1,-1):
    print(st[i])
