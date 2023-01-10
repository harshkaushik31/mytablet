# Prime Cheacker
def PRIME(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime == False:
        print('Not a prime number')
    else:
        print('Prime number')
n = int(input('Enter the number to check for: ' ))
PRIME(n)
