#!/usr/bin/python
'''
Create a frequency analysis  program to decrypt an encrypted 
text stored in a file 
'''
from operator import itemgetter
import json
content=''
class FrequencyAnalysis():
    def __init__(self):
        self.Banner()
        print("\n[+] Starting Frequency Analysis Attack....")
        self.Banner()
    def Banner(self):
        for i in range(0,50):
            print("=",end="")
    def get_encrypted_text(self,file_enc):
        with open(file_enc, 'r') as f:
            content=f.read()
        return content
    def getContents(self,file_name):
        text=''
        with open(file_name, 'r') as f:
            text = f.read()
        return text
    ###########################################
    # Create a Dictionary of Plain text       #
    # and Check the frequency in given text   #
    #And Sort them depending on the frequency #
    ###########################################
    def plain_text_frequencies(self,filename=None):
        if not filename:
            text = self.get_encrypted_text(filename)
        else:
            text = self.getContents(filename)
        frequencies = {}

        for asciicode in range(65, 91):
            frequencies[chr(asciicode)] = 0

        for letter in text:
            asciicode = ord(letter.upper())
            if asciicode >= 65 and asciicode <= 90:
                frequencies[chr(asciicode)] += 1

        sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

        return sorted_by_frequency
    ###########################################
    # Create An estimated mappings between    #
    # Encrypted Letters and plain text letters#
    #Comparing plain text and Encrypted texts #
    ###########################################
    def Create_Decryption_Dictionary(self,plain_text,encrypted_text):
        dictionary_name = "decryption_dict"
        sample_plaintext_frequencies = self.plain_text_frequencies(plain_text)
        encrypted_text_frequencies = self.plain_text_frequencies(encrypted_text)

        decryption_dict = {}
        for i in range(0, 26):
            decryption_dict[encrypted_text_frequencies[i][0]] = sample_plaintext_frequencies[i][0].lower()

        f = open(f"{dictionary_name}.json", "w")
        json.dump(decryption_dict, f)
        f.close()
        print("[+] The dictionary has been created")
        return f"{dictionary_name}.json"
    ###########################################
    # After the dictionary has been create    #
    # Use the dictionary to decrypt the encry-#
    #pted text and created a decrypted file   #
    ###########################################
    def Decrypt_content(self,enc_tex_file,attack_dictionary):
        enc_text = self.getContents(enc_tex_file)
        decrypted_file_name = "decrypted.txt"
        f = open(attack_dictionary, "r")
        decryption_dict = json.load(f)
        f.close()

        decrypted_list = []

        for letter in enc_text:
            asciicode = ord(letter.upper())
            if asciicode >= 65 and asciicode <= 90:
                decrypted_list.append(decryption_dict[letter])

        decrypted_text = "".join(decrypted_list)

        f = open(decrypted_file_name, "w")
        f.write(decrypted_text)
        f.close()
        return True

if __name__ == "__main__":
    attack = FrequencyAnalysis()
    #ask for the filename from the user
    sample_plaintext = str(input("\nEnter path to a Plain text file\n"))
    encrypted_text = str(input("\nEnter path to a Encrypted text file\n"))
    dict_file = attack.Create_Decryption_Dictionary(sample_plaintext,encrypted_text)
    if attack.Decrypt_content(encrypted_text,dict_file):
        print("[+] Successfully Decrypted the Encyrpted Text\n")
        print("[+] Exiting ...\n")