# To create the binary file 'Student.dat' to store roll number, name and marks as long as the user wants and then read the file to display the contents
import pickle 
myfile = open('Student.dat','wb')
student = []
ans = 'y'
while ans.lower() == 'y':
    roll = int(input('Enter roll number: '))
    name = input('Enter name of the student: ')
    marks = int(input('Enter the marks of the sudent: '))
    student.append([roll,name,marks])
    ans = input('Do you want to continue(y): ')
pickle.dump(student,myfile)
myfile.close()
myfile = open('Student.dat','rb')
data = pickle.load(myfile)
for i in data:
    print(i[0],i[1],i[2])

