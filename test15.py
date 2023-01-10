# Function to write the sum of the following series 1 + X + X**2 + X**3 + ;;; + X**n
def SERIES(x,n):
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1 + x**i
    return sum1
x = int(input('Enter the number whose power is to be raised: '))
n = int(input('Enter the number of exponential you want to go to: '))
print(SERIES(x,n))
