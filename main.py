from primality import get_prime # For 
from random import randint          # For choosing large numbers
# TODO:
    # GUI
    # Key generation:
        # Find prime number (keep using Miller-Raabin on every number) (CHECK)
        # Find generator

alphabet = "abcdefghijklmnopqrstuvwzy "

def isPrimitiveRoot(g, p):
    #return true if g is primitive root of p
    o = 1
    k = pow(g, o, p)
    
    while k > 1:
        o += 1
        k *= g
        k %= p
        
    if o == (p - 1):
        return True

    return False

def get_keys(bits):
    '''
    Gets key
    '''

    p = get_prime(bits)
    g_bits = bits - randint(1, bits/2)
    
    # Get a random number of at least p's bitlength    
    while(1):
        g = get_prime(g_bits)
        if isPrimitiveRoot(g,p):
            break
    
    a_bits = bits - randint(1, bits/4)
    
    while(1):
        a = get_prime(a_bits)
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
    k = randint(2, p-2)

    alpha = pow(g, k, p)
    
    #add a space if the message length is odd
    if len(message) & 1:
        message += " "

    ciphertext = []
    for i in range(0, len(message), 2):
        l1, l2 = message[i], message[i+1]
        m1, m2 = alphabet.index(l1), alphabet.index(l2)
        m = 27 * m1 + m2
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
        
        m2 = m%27
        m1 = m/27
        plaintext += alphabet[m1] + alphabet[m2]

    #remove any final space added for even character count
    if plaintext[-1] == " ":
        plaintext = plaintext[:-1]

    return plaintext
