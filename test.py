from primality import get_prime
from main import *

message = 'this is a new message'

for i in range(10):
    keys = get_keys(256) # Ask about what happens <16 bits
    #keys = {'public': (163L, 23L, 125L), 'private': 131L}

    cipher = encrypt(keys['public'], message)
    plain = decrypt(keys, cipher)

    if plain != message:
        print keys
        print plain

print "done"
