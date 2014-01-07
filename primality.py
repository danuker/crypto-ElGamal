#Miller-Rabin primality test

import os, random, math#, time

#n-1 = 2^s * t
def grab_twos(n):
    s = 0
    while n % 2 != 1:
        s += 1
        n //= 2

    return s, n

def fermat(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

#Miller-Rabin test (Works only with positive)
def is_prime(n, k):
    if not n&1:
        return False
    
    if k < 1:
        raise Exception("k must be strictly positive")

    if n in (2, 3):
        return True
    if n < 2:
        raise Exception("n must be strictly positive")
        
    k = int(k)
    s, t = grab_twos(n-1)

    b = -1
    for i in range(1, k+1):
        random.seed(os.urandom(k))
        b = random.randrange(2, n-1)
        r = pow(b, t, n)
        if r != 1 and r != n - 1:
            j = 1
            while j <= s - 1 and r != n - 1:
                r = r*r % n
                if r == 1:
                    return False
                j += 1
            if r != n - 1:
                return False

    return True

def get_prime(bits):
    while True:
        random.seed(os.urandom(16))
        num = random.getrandbits(bits)
        if not num&1:
            continue
        #print num
        if fermat(num) == False:
            continue
        if is_prime(num, 10):
            return num

<<<<<<< HEAD
if __name__=='__main__':
    for i in range(2, 10):
        bits = 2**i
        t1 = time.time()
        print bits,
        get_prime(bits)
        print time.time()-t1
=======
##Testing grounds :3
##
##for i in range(2, 10):
##    bits = 2**i
##    t1 = time.time()
##    print bits,
##    get_prime(bits)
##    print time.time()-t1
>>>>>>> 56931a369821a99fbc0f21c98797e20342557157
