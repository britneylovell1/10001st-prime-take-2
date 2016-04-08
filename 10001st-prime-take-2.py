def check_prime(n):
    '''
    Divide n by all integers less than n.
    Return true if prime.
    Return false if divisible by an integer less than n.
    '''
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

def find_prime():
    '''
    Starting from 3, check 'primeness' of each integer.
    Keep a count of prime.
    Return 10,001st prime.
    '''
    i = 3
    counter = 1
    while counter < 10001:
        if check_prime(i):
            counter += 1
        i += 1
    return (i - 1)

print find_prime()