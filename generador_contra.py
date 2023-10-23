import random
import string

def generar(self):
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod