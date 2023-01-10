def MATHOP(a,b):
    sum1 = a+b
    diff = a-b
    prod = a*b
    rem = a%b
    quoint = a//b
    quo = a/b
    print('The sum of a and b is: ',sum1)
    print('The difference of a and b is: ',diff)
    print('The product of a and b is: ',prod)
    print('The remainder of a and b is: ',rem)
    print('The quotient of a and b is: ',quoint)
    print('The quotient in interger of a and b is: ',quo)
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
MATHOP(a,b)
