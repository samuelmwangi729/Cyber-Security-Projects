import random
import string
'''
The random password generator extends random and strings
to allow different passwords to be generated that are strong 
'''
def Generate(pass_length):
    #for a random password, there must be alphabets, uppercase,lowercase, numbers and also 
    #special symbols 
    length = int(pass_length)
    password_characters = string.ascii_letters + string.digits + string.punctuation
    generate_password  = ''.join(random.choice(password_characters) for i in range(length))
    return generate_password