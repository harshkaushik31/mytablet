# UDF to print table of any number
def TABLE(n):
    for i in range(1,11):
        print(n,' x ',i,' = ',n*i)
n = int(input('Enter any number to print table for: '))
TABLE(n)
