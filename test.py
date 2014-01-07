 
from primality import get_prime
from main import *

keys = get_keys(256) # Ask about what happens <10 bits

cypher = encrypt(keys['public'], 'hello')

print keys
print decrypt(keys, cypher)
