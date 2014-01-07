from primality import get_prime # For 
from random import randint          # For choosing large numbers

# TODO:
    # GUI
    # Key generation:
        # Find prime number (keep using Miller-Raabin on every number) (CHECK)
        # Find generator

def get_key(bits):
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
    
    ga = pow(g, a, p)
    
    return {"public":(p, g, ga), "private":a}
    