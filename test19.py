# Menu driven prorm for stack implementation using list
def Push(L):
    n = int(input('Enter number of elements to enter: '))
    for i in range(n):
        elem = int(input('Enter element: '))
        L.append(elem)
def Pop(S):
    n = int(input('Enter the number of elements to pop: '))
    for i in range(n):
        print(S.pop())
def Display(L):
    if L == []:
        print('Underflow!')
    else:
        for i in range(len(L)-1,-1,-1):
            print(L[i])
ans = 'y'
L = []
while ans.lower() == 'y':
    print("-"*20)
    print('1. Input Elements')
    print('2. Pop Elements')
    print('3. Display Elements')
    print('4. Exit')
    choice = int(input(': '))
    if choice == 1:
        Push(L)
    elif choice == 2:
        Pop(L)
    elif choice == 3:
        Display(L)
    elif choice == 4:
        print("Bye!")
        exit()
    else:
        print('Wrong Keyword entered!')
    ans = input('Do you want to continue(y):')

