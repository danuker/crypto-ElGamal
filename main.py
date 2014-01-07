from primality import get_prime # For 
from random import randint          # For choosing large numbers

# TODO:
    # GUI
    # Key generation:
        # Find prime number (keep using Miller-Raabin on every number) (CHECK)
        # Find generator

alphabet = "abcdefghijklmnopqrstuvwzy "

def get_keys(bits):
    '''
    Gets key
    '''

    p = get_prime(bits)    
    g_bits = bits - randint(1, bits/2)
    
    # Get a random number of at least p's bitlength    
    while(1):
        g = get_prime(g_bits)
        if g<p:
            break
    
    a_bits = bits - randint(1, bits/4)
    
    while(1):
        a = get_prime(a_bits)
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
    k = randint(1, p)
    alpha = pow(g, k, p)
    
    #add a space if the message length is odd
    if len(message) & 1:
        message += " "

    ciphertext = []
    for i in range(0, len(message), 2):
        l1, l2 = message[i], message[i+1]
        m1, m2 = string.index(l1), string.index(l2)
        m = 27 * m1 + m2
        beta = m * pow(ga, k, p)
        ciphertext.append((alpha,beta))

    return ciphertext

def decrypt(private_key, ciphertext):
    '''
        ciphertext is a list of tuples
    '''
    plaintext = ""
    for c in ciphertext:
        alpha, beta = c
        m = pow(alpha, -private_key, p) * beta % p
        m1 = m/27
        m2 = m % 27
        plaintext += m1 + m2

    return plaintext
