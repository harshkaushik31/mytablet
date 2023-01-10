# To Create a binary file "Emp.dat" to store employee details in form of dictonarites and then read the file to display the contents
import pickle
myfile = open('Emp.dat','wb')
emp = {}
ans = 'y'
while ans.lower() == 'y':
    emp_no = int(input('Enter employee number: '))
    emp_name = input("Enter employee name: ")
    emp[emp_no] = emp_name
    ans = input("Do you want to continue(y): ")
pickle.dump(emp,myfile)
myfile.close()
myfile = open('Emp.dat','rb')
data = pickle.load(myfile)
print(data)
