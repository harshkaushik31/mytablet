myfile = open("Answer.txt",'r')
data = myfile.read()
L = data.split()
for i in L:
    print(i, end='# ')
myfile.close()
