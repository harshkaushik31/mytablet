# To check wheater the given number is a armstrong number or not
def ARMSTRONG(n):
    sum1 = 0
    temp = n
    while temp>0:
        digit = temp % 10
        sum1 = sum1 + digit**3
        temp//=10
    if sum1 == n:
        print('The number is a armstorng nunber!')
    else:
        print('The number is not a armstrong number!')
n = int(input('Enter the number: '))
ARMSTRONG(n)
