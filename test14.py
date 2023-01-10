# Palindrome
def PALINDROME(n):
    temp = n
    rev = 0
    while temp>0:
        digit = temp %  10
        rev = rev * 10 + digit
        temp = temp // 10
    if rev == n:
        print('The number is a palindrome')
        print('The reverse of the number is: ',rev)
    else:
        print('The number is not a palindrome')
        print('The reverse of the number is: ',rev)
n = int(input('Enter the number to check for palindrome: '))
PALINDROME(n)
