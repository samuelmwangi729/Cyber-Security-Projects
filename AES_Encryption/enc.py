from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class ImageAESEncryptor():
    def __init__(self):
        self.Banner()
        print("\n LAUNCHING AN IMAGE ENCRYPTION/DESCRYPTION TOOL")
        self.Banner()
        super().__init__()
    def Banner(self):
        for i in range(0,50):
            print("=",end="")
    def Encrypt(self,image_file,encrypted_image,decryption_password):
        with open(image_file, 'rb') as file:
            image_data = file.read()
            salt = get_random_bytes(AES.block_size)
            key_iv = PBKDF2(decryption_password, salt, 32 + 16, count=1000000, hmac_hash_module=SHA256)
            key = key_iv[:32]
            iv = key_iv[32:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
            with open(encrypted_image, 'wb') as file:
                file.write(salt)
                file.write(encrypted_data)
            return True
    def Decrypt(self,image_file,encrypted_image,decryption_password):
        with open(image_file, 'rb') as file:
            salt = file.read(AES.block_size)
            encrypted_data = file.read()
        key_iv = PBKDF2(decryption_password, salt, 32 + 16, count=1000000, hmac_hash_module=SHA256)
        key = key_iv[:32]
        iv = key_iv[32:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        with open(encrypted_image, 'wb') as file:
            file.write(decrypted_data)
        return True
    def get_encrytion_props(self):
        input_obj= input("Enter the Image Path to be encrypted...\n")
        output_obj = input("Enter the Name of the encrypted Image...\n")
        password = input("Enter the Password to encrypt the Image\n")
        try:
            if self.Encrypt(input_obj,output_obj,password):
                print("Image Successfully Encrypted!")
        except:
            print("Could not Encrypt the Image")
    def get_decrytion_props(self):
        input_obj= input("Enter the Path of the Encrypted file\n")
        output_obj = input("Enter the Name of the New Image File\n")
        password = input("Enter the decryption Password to encrypt the Image\n")
        try:
            if self.Decrypt(input_obj,output_obj,password):
                print("Image Successfully Decrypted!")
        except:
            print("Could Not decrypt the Image")
imageEncryptor = ImageAESEncryptor()
ch=True
while ch:
    try:
        print("\nPlease Choose an Option\n")
        print("1:Encrypt an Image")
        print("2:Decrypt an Image")
        print("3:Encrypt an Image")
        choice = int(input())
        if choice==1:
            imageEncryptor.get_encrytion_props()
        elif choice==2:
            imageEncryptor.get_decrytion_props()
        elif choice==3:
            print("[+] Exiting\n")
            exit()
        con = input("Do you want to Continue? Y/N\n").lower()
        if con=="y":
            ch=True
        else:
            ch=False
    except KeyboardInterrupt:
        print("[+] Cancelled by the user\n")
        exit()
imageEncryptor.Banner()
print("\n[+] Thank you for using the tool")
imageEncryptor.Banner()