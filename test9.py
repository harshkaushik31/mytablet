import csv
# with open('myfile.csv',mode='a') as myfile:
#     mywriter = csv.writer(myfile,delimiter=',')
#     ans = 'y'
#     while ans.lower() == 'y':
#         emp_no = int(input('Enter employee number: '))
#         name = input('Enter employee name: ')
#         salary = int(input('Enter salary: '))
#         mywriter.writerow([emp_no,name,salary])
#         ans = input('Do you want to continue(y): ')
with open('myfile.csv',mode='r') as myfile:
    myreader = csv.reader(myfile,delimiter=',')
    # ans = 'y'
    # while ans.lower() == 'y':
    #     eno = int(input('Enter employee number to search for: '))
    #     for row in myreader:
    #         found = False
    #         # if len(row)!=0:
    #         #     if int(row[0]) == eno:
    #         #         print('The Employee is: ',row[1],'Salary is: ',row[2])
    #         #         found = True
    #         #         break
    #         if row == []:
    #             continue
    #         else: 
    #             if int(row[0]) == eno:
    #                 print('Name of the employee is ',row[1])
    #                 found = True
    #     if found == False:
    #         print('Sorry Employee not found!')
    #     ans = input('Do you want to continue(y): ')
    found = False
    eno = int(input('Enter employee to search for: '))
    for row in myreader:
        if row == []:
            continue
        else:
            if int(row[0]) == eno:
                print('The employee is: ',row[1])
                found = True
    if found == False:
        print('Employee not found')
            
    