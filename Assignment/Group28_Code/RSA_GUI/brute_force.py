import math


def nearestOddUnder(number):
    if (number % 2) == 0:
        number = number -1
    else:
        number = number -2
    return number


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def bruteRSA(n,e):
    c = math.floor((math.sqrt(n)))
    c = nearestOddUnder(c)

    for i in range(c, 1 , -2):
        if(n%i == 0):
            p = i
            break

    if (p == None):
        raise Exception()

    q = n / p
    q = math.floor(q)

    if (n -p*q) != 0:
        raise Exception('Brute force failed')

    phin = (p-1) * (q-1)
    d = modinv(e,phin)
    if (d*e %phin != 1):
         raise Exception('Brute force failed')

    return d
