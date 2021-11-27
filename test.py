import random

def prime(x):
    isprime = True
    for j in range(2, int(x**0.5) + 1):
        if x%j == 0:
            isprime = False
            break
    return isprime

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res*=i
    return res

def choice(n, k):
    return(fac(k)/(fac(n) * fac(k - n)))

def permutation(n, k):
    return(fac(k)/fac(k - n))

def harmonic(n):
    res = 0
    for i in range(1, n):
        res += 1/i
    print(res)

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)

def get_smallest_factor(n):
    if n == 1:
        return 1
    for i in range (2, n + 1):
        if n % i == 0:
            return i

def factorize(n):
    factors = [1]
    while n > 1:
        smallest_factor = get_smallest_factor(n)
        factors.append(smallest_factor)
        n = int(n/smallest_factor)
    return factors

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

def gcd(*a):
    res = a[0]
    for i in range(1, len(a)):
        res = get_gcd(res, a[i])
    return res

def lcm(a, b):
    return (a * b) / get_gcd(a, b)

def print_primes(n):
    for i in range(2, n):
        if prime(i):
            print(i)

def mirror(n):
    n = str(n)
    x = n[::-1]
    for i in range(1, len(x)):
        if int(x[0:i]) * int(x[i:len(x)+1]) == int(n):
            return True
    return False


def check_digits(n):
    n = str(n)
    for i in range(0, len(n)):
        if int(n[i]) > 3 or (n[i]) == 0:
            return False
    return True

def abs_value(x):
    if x>=0:
        return x
    return -x


