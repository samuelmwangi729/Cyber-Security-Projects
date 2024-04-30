import random
import string
'''
The random password generator extends random and strings
to allow different passwords to be generated that are strong 
'''
class RandomGenerator():
    def __init__(self):
        print("Launching the Random Password Generator")
    def Generate(self, pass_length):
        #for a random password, there must be alphabets, uppercase,lowercase, numbers and also 
        #special symbols 
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generate_password  = ''.join(random.choice(password_characters) for i in range(pass_length))
        return generate_password

if __name__ == "__main__":
    randomGenerator = RandomGenerator()
    ch=True
    while ch:
        password_length = int(input("Enter the length of the password: "))
        no_of_passwords = int(input("How many passwords do you want to generate?"))
        for i in range(1, no_of_passwords+1):
            #generate the passwords one after the other 
            print(f"[+] The {i}  password is {randomGenerator.Generate(password_length)}")
        print("Do you wish to continue? Y/N")
        choice = input().lower()
        if choice =='y':
            ch=True
        else:
            ch=False
    print("[!!] Exiting...")