alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

class CeaserCipher():
    def encrypt(self,text, shift):
        #this is there inde
        cipher_text = ""
        for letter in text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                pos = alphabet.index(letter) + shift
                cipher_text += alphabet[pos]
        print(f"The encrypted string is: {cipher_text}\n")


    def decrypt(self,text, shift):
        cipher_text = ""
        for letter in text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                pos = alphabet.index(letter) + 26 - shift
                cipher_text += alphabet[pos]
        print(f"The decoded text is: {cipher_text}\n")
    def Banner(self):
        for i in range(0,50):
            print("=",end="")

ch = True
while ch:
    try:
        action = CeaserCipher()
        action.Banner()
        print("\nCeaser Cipher Encryptor and Decryptor tool")
        action.Banner()
        print("\nChoose An Option...\n")
        print("1. Encrypt a Text\n")
        print("2. Decrypt a Text\n")
        print("3. Exit\n")
        option = int(input())
        if option==1:
            text_to_encrypt = input("\nType text to encrypt:\n").lower()
            shift = int(input("Enter the numeric number to shift the alphabets\n"))
            action.encrypt(text_to_encrypt,shift)
        elif option==2:
            text_to_encrypt = input("\nType text to Decrypt:\n").lower()
            shift = int(input("Enter the numeric number used shift the alphabets\n"))
            action.decrypt(text_to_encrypt,shift)
        elif option==3:
            print("[-] Exiting...")
            exit()
        choice = input("Do You Want to Continue(Y/N): \n").lower()
        if choice == 'n':
            ch = False
            print("\n[+] Exiting ....")
        elif choice == 'y':
            ch = True
    except KeyboardInterrupt:
        print("\n[-] Program Terminated by User...")
        exit()