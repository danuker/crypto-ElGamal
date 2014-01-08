from primality import get_prime, is_prime
import random, os
from math import log
# TODO:
    # GUI
    # Key generation:
        # Find prime number (keep using Miller-Raabin on every number) (CHECK)
        # Find generator

alphabet = "abcdefghijklmnopqrstuvwxyz "

def get_keys(bits):
    '''
    Gets key
    '''

    while(1):
        p = get_prime(bits)
        if p < len(alphabet) * (len(alphabet) - 1) + len(alphabet):
            continue;
        
        p1 = p - 1
        q = p1/2
        if is_prime(q, log(bits)):
            break

    #use a value in the top 50% of the number of p's bits
    g_bits = bits - random.randint(1, bits/2)

    while(1):
        random.seed(os.urandom(int(log(g_bits))))
        g = random.randrange(2, p-1)
        if pow(g, q, p) == 1 and pow(g, 2, p) != 1:
            break


    #use a value in the top 25% of the number of p's bits
    a_bits = bits - random.randint(1, bits/4)
    
    while(1):
        random.seed(os.urandom(int(log(a_bits))))
        a = random.randrange(1, p-1)
        if a > 0 and a < p - 1:
            break
    
    ga = pow(g, a, p)
    
    return {"public":(p, g, ga), "private":a}

def valid(message):
    for c in message:
        if c not in alphabet:
            return False

    return True

def encrypt(public_key, message):
        
    
    if not valid(message):
        raise Exception("Invalid message")
    
    p, g, ga = public_key
    k = random.randint(2, p-2)
##    print k

    alpha = pow(g, k, p)
    
    #add a space if the message length is odd
    if len(message) & 1:
        message += " "

    ciphertext = []
    for i in range(0, len(message), 2):
        l1, l2 = message[i], message[i+1]
        m1, m2 = alphabet.index(l1), alphabet.index(l2)
        m = 27 * m1 + m2
##        print "enc_m=",m
        beta = m * pow(ga, k, p)
        ciphertext.append((alpha,beta))
    
    return ciphertext

def decrypt(keys, ciphertext):
    '''
        ciphertext is a list of tuples
    '''
    p = keys['public'][0]
    a = keys['private']
    plaintext = ""
    for c in ciphertext:
        alpha, beta = c
        
        inverse = pow(alpha, a, p)
        m = pow(inverse, p-2, p)*beta  %p
##        print "dec_m=",m
        
        m2 = m%27
        m1 = m/27
        
        plaintext += alphabet[m1] + alphabet[m2]

    #remove any final space added for even character count
    if plaintext[-1] == " ":
        plaintext = plaintext[:-1]

    return plaintext
