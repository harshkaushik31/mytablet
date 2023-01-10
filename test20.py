# Stack inplementation of hostel wala
def Push(L,item):
    L.append(item)
def Pop(L):
    return L.pop()
def Display(L):
    if  L == []:
        print('Underflow!')
    else:
        for i in range(len(L)-1,-1,-1):
            print(L[i][0], L[i][1], L[i][2])
# Main flow
L = []
ans = 'y'
while ans.lower() == 'y':
    print('-'*20)
    print('1. Push item')
    print('2. Pop item')
    print('3. Display Stack')
    print('4. Exit')
    choice = int(input(': '))
    if choice == 1:
        no_in = int(input('Enter number of records to enter: '))
        for i in range(no_in):
            h_no = int(input('Enter hostel number: '))
            r_no = int(input('Enter room number: '))
            stu_no = int(input('Enter number of students: '))
            Push(L,[h_no,r_no,stu_no])
    elif choice == 2:
        no_pop = int(input('Enter number of elements to pop: '))
        for i in range(no_pop):
            print('The deleted items are: ',Pop(L))
    elif choice == 3:
        Display(L)
    elif choice == 4:
        print('Bye')
        exit()
    else:
        print('Wrong choice')
    ans = input('Do you want to continue(y): ')

