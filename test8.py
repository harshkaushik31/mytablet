# To search for roll number 12 and 14 in 'Student.dat'
import pickle
myfile = open('Student.dat','rb')
data = pickle.load(myfile)
found = False
for i in data:
    if i[0]==12 or i[0]==14:
        found = True
        print('The roll number of student is: ',i[0],"\n",'The name of the student is: ',i[i],'\n','The marks of the student is: ',i[2])
        break
if found == False:
    print('Sorry! Not found')
