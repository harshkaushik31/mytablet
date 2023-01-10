# To create a csv file to store student data roll number name marks in the form of 5 recored and then display the records
import csv
with open('student.csv',mode='a') as myfile:
    mywriter = csv.writer(myfile,delimiter=',')
    for i in range(5):
        roll = int(input('Enter roll number: '))
        name = input('Enter name: ')
        marks = int(input('Enter marks: '))
        mywriter.writerow([roll,name,marks])
with open('student.csv',mode='r') as myfile:
    myreader = csv.reader(myfile,delimiter=',')
    for row in myreader:
        if len(row) == 0:
            continue
        else:
            print(row[0],row[1],row[0])