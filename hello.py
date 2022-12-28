#print("Hello World!")
#print("My First Python prgrm")
#print("make any prgrm using touch command ex. touch hello.py py for python .c for c .cpp for c++ and .java for java prgrm compile - java using javac hello.java c using gcc hello.c c++ using g++ hello.cpp")
#print("run using python3 hello.py, java hello, ./a.out hello.c/cpp(command is same for c and c++) ")
#print("no need to compile python program as interpreter based")
#print("rm hello.py for deleting and ls command for list")

def push(H):
    no_of_elements_to_input=int(input("Enter number of elements: "))
    for i in range(no_of_elements_to_input):
        hostel_number=int(input("Enter the hostel number: "))
        number_of_rooms=int(input("Enter the nuber of rooms: "))
        number_of_students=int(input("Enter the number of students: "))
        temp=[hostel_number,number_of_rooms,number_of_students]
        H.append(temp)
def pop(H):
    if len(H)==0:
        print("The list is empty!")
    else:
        number_of_elements_to_be_popped=int(input("Enter the number of Elements to be popped: "))
        for i in range(number_of_elements_to_be_popped):
            print("The Elements popped are ",H.pop())
def display(H):
    length_of_H=len(H)
    if(length_of_H==0):
        print("The List is Empty ")
    else:
        print("Hostel Number\t\tNumber of Rooms\t\tNumber of Students")
        for i in range(length_of_H-1,-1,-1):
            print(H[i][0],"\t\t\t\t",H[i][1],"\t\t\t",H[i][2])
#main flow of program
H=[]
go_again="y"
while(go_again=="y" or go_again=="Y"):
    print(".....MENU.....")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    user_choice=int(input("Enter your choice: "))
    if(user_choice==1):
        push(H)
    elif(user_choice==2):
        pop(H)
    elif(user_choice==3):
        display(H)
    elif(user_choice==4):
        exit()
    else:
        print("Wrong Input")
        print("The input was wrong!")
    go_again=input("Do you want to go again(y/n): ")
