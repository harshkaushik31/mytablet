# To Create a binary file Student.dat to store roll numbers and name, search using roll number and display name if roll number nor found display and appropriate msg
import pickle
student = []
ans = 'y'
myfile = open('Student.dat','wb')
while ans.lower() == 'y':
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    L=[roll,name]
    student.append(L)
    ans = input("Do you want to continue(y): ")
pickle.dump(student,myfile)
myfile.close()
myfile = open('Student.dat','rb')
data = pickle.load(myfile)
ans = 'y'
while ans.lower() == 'y':
    n = int(input("Enter student roll number to search for: "))
    is_found = False
    for i in data:
        if n == i[0]:
            is_found = True
            print("The name of the student is: ",i[1])
    if is_found == False:
        print("No student found!")
    ans = input("Do you want to continue(y): ")
print("Thank you for using the program! ")
