#!/usr/bin/python3
'''
THis is a python file used to check the strength of 
a password in a scale of 0-4 where 0 represents
an easy password to crack where 4 represents a very hard 
password to crack
This script is created as part of my classwork. 
It is therefore free to use under MIT License.
You can modify and redistribute modified copies of the program
'''
from zxcvbn import zxcvbn
import re
pattern = re.compile(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|<,./?>]')
def passwordValidate(passwd):
    if len(passwd) < 8 :
        print("[+] Your Password %s must be at least 8 characters" %passwd)
    elif not any(char.isdigit() for char in passwd):
        print("[+] Your password %s must include a digit" %passwd)
    elif(not pattern.search(passwd)):
        print("[+] Your password %s must include at least a special character" %passwd)
    elif not any(char.isalpha() for char in passwd):
        print("[+] Your password %s should  have at least one letter" %passwd)
    else:
        test(passwd)
    getScore(passwd)

def test(p):
    test_results = zxcvbn(password)
    printLine()
    print("[+]Here are the reasons your password score is %s" % test_results['score'])
    printLine()
    if(test_results['feedback']['warning']):
        print("[-] %s" % test_results['feedback']['warning'])
    print("[-] We suggest that you %s" % test_results['feedback']['suggestions'][0] if test_results['feedback']['suggestions'] else '[+] You have Selected a good password')
    print("[-] Your Password can be cracked for %s" % test_results['crack_times_display']['offline_slow_hashing_1e4_per_second'])

def getScore(passwd):
    print(f'[+] Your Password score is %s' % zxcvbn(password)['score'])
    test(passwd)

def printBanner():
    for i in range(0,47):
        print("=",end="")
def printLine():
    for i in range(0,47):
        print("_",end="")
    print("\n")
try:
    printBanner()
    print("\n This Program is designed to rate your password")
    printBanner()
    password = input("\nEnter the password:\n")
    passwordValidate(password)
    printBanner()
except KeyboardInterrupt:
    print("\n[+] Cancelled by User")
    exit()