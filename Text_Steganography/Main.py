from tkinter import *
import tkinter as tk 
from tkinter import font 
from PIL import Image, ImageTk
from tkinter import messagebox
import base64
import os
root = tk.Tk()
LoginPage = Frame(root)
RegisterPage = Frame(root)
Dashboard = Frame(root)
database = f'{os.getcwd()}/database.db'
database = f'{os.getcwd()}/encrypted.enc'
def Encrypt():
    password = str(passwordFieldEnc.get()).strip()
    text_to_encrypt= str(toEncryptField.get()).strip()
    if not text_to_encrypt:
        messagebox.showerror("Error",f"There Must be text to Encrypt")
        return
    else:
        passwordFieldEnc.delete(0,END)
        toEncryptField.delete(0,END)
        encryptedTextLabel.delete(1.0,END)
        encrypted_data = text_to_encrypt.encode("ascii")
        base64_encoded = base64.b64encode(encrypted_data)
        encrypted_string = base64_encoded.decode("ascii")
        with open("encrypted.enc", "a") as f:
            f.write(f"{encrypted_string}:{password}\n")
        encryptedTextLabel.insert(END,f"The encrypted text is {encrypted_string}")

def Decrypt():
    message = str(toDecryptField.get()).strip()
    password = str(passwordFieldDec.get()).strip()
    if not password:
        messagebox.showerror("Error",f"There Must be a password to Decrypt data")
        return
    if not message:
        messagebox.showerror("Error",f"There Must be text to decrypt")
        return  False
    #read the enc file data 
    with open("encrypted.enc", "r") as encrypted_texts:
        for item in encrypted_texts:
            if str(item).split(":")[0] == message:
                if str(str(item).split(":")[1]).strip()==password:
                    decryptedTextLabel.delete(1.0,END)
                    decoded_msg = str(str(item).split(":")[0]).strip().encode("ascii")
                    base64_bytes = base64.b64decode(decoded_msg)
                    decrypted_string = base64_bytes.decode("ascii")
                    decryptedTextLabel.insert(END,f"The decrypted text is {decrypted_string}")
                else:
                    messagebox.showerror("Error",f"Wrong Access Password")
                break;
            else:
               messagebox.showerror("Error",f"Encrypted message not decrypted by Us")
               return
def Sign_in():
    username = str(usernamelField.get()).strip()
    password = str(passwordlField.get()).strip()
    if not username or not password:
        messagebox.showerror("Invalid",f"Username or Password Should not be blank")
        return  False
    else:
        #read the database file 
        with open("database.db","r") as login_details:
            for items in login_details:
                if str(str(items).split(":")[0]).strip()==username:
                    #check the password 
                    if str(str(items).split(":")[1]).strip()==password:
                        #successfully logged in
                        usernamelField.delete(0,END)
                        passwordlField.delete(0,END)
                        usernamelField.focus_force()
                        Dashboard.tkraise()
                    else:
                        messagebox.showerror("Invalid",f"Password Entered is Incorrect")
                        return
                    return
                else:
                    messagebox.showerror("Invalid",f"Username Entered is Invalid")
                    return
def Sign_up():
    username=str(usernameSignUpField.get()).strip()
    password=str(passwordSignupField.get()).strip()
    cpassword=str(passwordConfirmField.get()).strip()
    if not username or not password or not cpassword:
        messagebox.showerror("Invalid",f"You cant Register with Blank Details")
    else:
        # read a file and store the details there
        try:
            with open(database,'a') as f:
                data = f"{username}:{password}\n"
                f.write(data)
            usernameSignUpField.delete(0,END)
            passwordSignupField.delete(0,END)
            passwordConfirmField.delete(0,END)
            usernameSignUpField.focus_force() 
            messagebox.showinfo("success",f"Successfully Registered. Please Login Now")
        except IOError as e:
            messagebox.showerror("Invalid",f"Could Not Sign Your Up. Please try again later")
#fit the pages in the frame
LoginPage.grid(row=0,column=0,sticky="nsew")
RegisterPage.grid(row=0,column=0,sticky="nsew")
Dashboard.grid(row=0,column=0,sticky="nsew")

#####################################
#PLACING OBJECTS IN THE SIGN IN PAGE#
#####################################
image = Image.open("login.jpg")
width= 450
height=500
image = image.resize((width,height))
photo = ImageTk.PhotoImage(image)
Label(LoginPage,image=photo).pack(side=LEFT, expand=True,fill=BOTH)

#add a frame for the objects 
frame = Frame(LoginPage, width=450, height=500, bg="white")
#heading label to the frame 
heading = Label(frame,text="Sign In", fg='green', bg='white',font=("Maiandra GD",25,'bold','underline'))
heading.place(x=180,y=20)
#add username field 
usernameLabel = Label(frame,text="Username", fg='green', bg='white',font=("Maiandra GD",12))
usernameLabel.place(x=40,y=95)
usernamelField = Entry(frame,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12))
usernamelField.place(x=40,y=120,height=35)
usernamelField.insert(0,"")
usernamelField.focus_force() 
# pasword field
passwordLabel = Label(frame,text="Password", fg='green', bg='white',font=("Maiandra GD",12,))
passwordLabel.place(x=40,y=170)
passwordlField = Entry(frame,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12),show="*")
passwordlField.place(x=40,y=195,height=35)
#button here
button = Button(frame, text="Sign In", cursor="hand2",width=37,pady=7, bg="green",fg="white",border=0, command=Sign_in)
button.place(x=40,y=250,height=35)

##allow users to register
Label(frame,text="Do not have an Account?",fg='green', bg='white',font=("Maiandra GD",12,)).place(x=40,y=300)
Button(frame, text="Sign Up", cursor="hand2", width=10,pady=7, bg="green",fg="white",border=0,command=lambda:RegisterPage.tkraise() ).place(x=255,y=295,height=35)
Label(frame,text="Do not have an Account?",fg='green', bg='white',font=("Maiandra GD",12,)).place(x=40,y=300)
frame.pack(side=LEFT, expand=True,fill=BOTH)

#####################################
#PLACING OBJECTS IN THE SIGN UP PAGE#
#####################################
image2 = Image.open("register.jpg")
width= 450
height=500
image2 = image2.resize((width,height))
photo2 = ImageTk.PhotoImage(image2)
Label(RegisterPage,image=photo2).pack(side=LEFT, expand=True,fill=BOTH)

#add a frame for the objects 
frame2 = Frame(RegisterPage, width=450, height=500, bg="white")
#add username field 
usernameLabel = Label(frame2,text="Username", fg='green', bg='white',font=("Maiandra GD",12))
usernameLabel.place(x=40,y=95)
usernameSignUpField = Entry(frame2,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12))
usernameSignUpField.place(x=40,y=120,height=35)
usernameSignUpField.insert(0," ")
usernameSignUpField.focus_force() 
# pasword field
passwordLabel = Label(frame2,text="Password", fg='green', bg='white',font=("Maiandra GD",12,))
passwordLabel.place(x=40,y=170)
passwordSignupField = Entry(frame2,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12),show="*")
passwordSignupField.place(x=40,y=195,height=35)
# pasword field
passwordLabel = Label(frame2,text="Confirm Password", fg='green', bg='white',font=("Maiandra GD",12,))
passwordLabel.place(x=40,y=240)
passwordConfirmField = Entry(frame2,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12),show="*")
passwordConfirmField.place(x=40,y=270,height=35)
#button here
button = Button(frame2, text="Register", cursor="hand2",width=37,pady=7, bg="green",fg="white",border=0, command=Sign_up)
button.place(x=40,y=330,height=35)
Button(frame2, text="Sign In", cursor="hand2", width=10,pady=7, bg="green",fg="white",border=0,command=lambda: LoginPage.tkraise()).place(x=255,y=405,height=35)

Label(RegisterPage,text="Fill In the Following Details",fg='green', bg='white',font=("Maiandra GD",25,'bold','underline')).place(x=200,y=10)

frame2.pack(side=LEFT, expand=True,fill=BOTH)



#####################################
#PLACING OBJECTS IN THE DASHBOARD   #
#####################################
framedash = Frame(Dashboard, width=900, height=230)
Label(Dashboard,text="Welcome to Text Encryptor tool",fg='green',font=("Maiandra GD",25,'bold','underline')).place(x=50,y=10)
Button(Dashboard, text="Logout", cursor="hand2", width=20,pady=7, bg="red",fg="white",border=0,command=lambda: LoginPage.tkraise()).place(x=700,y=12,height=35)
covertextLabel = Label(framedash,text="Access Password", fg='green',font=("Maiandra GD",12))
covertextLabel.place(x=50,y=60)
passwordFieldEnc = Entry(framedash,width=40,fg='green',border=0,font=("Times New Roman",12),show="*")
passwordFieldEnc.place(x=50,y=90,height=40)
textLabel = Label(framedash,text="Text to Encrypt", fg='green',font=("Maiandra GD",12))
textLabel.place(x=400,y=60)
toEncryptField = Entry(framedash,width=60,fg='green',border=0,font=("Times New Roman",12))
toEncryptField.place(x=400,y=90,height=40)
Button(framedash, text="Encrypt Text", cursor="hand2", width=30,pady=7, bg="green",fg="white",border=0,command=Encrypt).place(x=50,y=190,height=35)
encryptedTextLabel = Text(framedash, fg='green',font=("Maiandra GD",12),relief=GROOVE,bd=0)
encryptedTextLabel.place(x=50,y=132,width=830,height=45)
framedash.pack()

framedash2 = Frame(Dashboard, width=900, height=280, bg="gray")
Label(framedash2,text="Welcome to Text Decryptor tool",fg='green',bg="gray",font=("Maiandra GD",25,'bold','underline')).place(x=50,y=10)
textLabel = Label(framedash2,text="Access Password", bg="gray", fg='green',font=("Maiandra GD",12))
textLabel.place(x=50,y=60)
passwordFieldDec = Entry(framedash2,width=40,fg='green',border=0,font=("Times New Roman",12),show="*")
passwordFieldDec.place(x=50,y=90,height=40)
textLabel = Label(framedash2,text="Text to Decrypt",bg="gray", fg='green',font=("Maiandra GD",12))
textLabel.place(x=400,y=60)
toDecryptField = Entry(framedash2,width=60,fg='green',border=0,font=("Times New Roman",12))
toDecryptField.place(x=400,y=90,height=40)
Button(framedash2, text="Decrypt Text", cursor="hand2", width=30,pady=7, bg="green",fg="white",border=0,command=Decrypt).place(x=50,y=180,height=35)
decryptedTextLabel = Text(framedash2, fg='green',font=("Maiandra GD",12),relief=GROOVE,bd=0)
decryptedTextLabel.place(x=50,y=132,width=830,height=45)
framedash2.pack()

LoginPage.tkraise()
root.title("Login To Text Streganography App")
root.geometry("900x500+200+100")
root.configure(bg="white")
root.resizable(False,False)

root.mainloop()