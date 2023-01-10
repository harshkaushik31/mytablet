myfile = open("Marks.txt",'w')
ans = 'y'
while ans.lower() == 'y':
    roll = int(input("Enter roll number: "))
    name = input("Enter name of the student: ")
    marks = int(input("Enter marks of the student: "))
    L = str(roll) + " " + name + " " + str(marks) + '\n'
    myfile.write(L)
    ans = input("Do you want to add more(y): ")
myfile.close()
myfile = open("Marks.txt",'r')
data = myfile.read()
print(data)
