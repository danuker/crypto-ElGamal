from primality import get_prime
from main import *

for i in range(10):
    keys = get_keys(256) # Ask about what happens <16 bits
    #keys = {'public': (163L, 23L, 125L), 'private': 131L}

    cipher = encrypt(keys['public'], 'this is a longer message than before')
    plain = decrypt(keys, cipher)

    print keys
    print plain
