 
from primality import get_prime
from main import *

keys = get_keys(11)

cypher = encrypt(keys['public'], 'hello')
plain = decrypt(keys, cypher)

print plain
