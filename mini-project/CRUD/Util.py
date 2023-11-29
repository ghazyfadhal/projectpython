'''UTILITY'''

import random
import string

# Fungsi membuat primary key secara Random

def random_string(panjang : int) -> str :
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang)) 
    return hasil_string
# panjang diisi di tempat fungsi dipanggil / bisa di custom 