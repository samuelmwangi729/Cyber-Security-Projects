from tkinter import *
import tkinter as tk 
from tkinter import font 
from PIL import Image, ImageTk
from tkinter import messagebox
import base64
import os
import AES
import Generator
username=''
root = tk.Tk()
Decryptor = Frame(root)
LoginPage = Frame(root)
RegisterPage = Frame(root)
Dashboard = Frame(root)
database = f'{os.getcwd()}/users.db'
passwords = f'{os.getcwd()}/passwords.enc'
def DecryptPassword():
    decryptedPasswordField.delete(1.0,END)
    encrypted_pass = str(EncryptedPasswordField.get()).strip()
    if not encrypted_pass:
        messagebox.showerror("Error",f"Encrypted Message Can not be blank")
        return
    else:
        decrypted_password = AES.decrypt_password(encrypted_pass)
        decryptedPasswordField.insert(1.0,decrypted_password)
def showDecryptor():
    Decryptor.tkraise()
def Sign_in():
    username = str(usernamelField.get()).strip()
    password = str(passwordlField.get()).strip()
    if not username or not password:
        messagebox.showerror("Invalid",f"Username or Password Should not be blank")
        return  False
    else:
        #read the database file 
        with open(database,"r") as login_details:
            for items in login_details:
                if str(str(items).split(":")[0]).strip()==username:
                    #check the password 
                    #get the password from the database and its iv 
                    encrypted_password = str(str(items).split(":")[1]).strip()
                    decrypted_password = AES.decrypt_password(encrypted_password)
                    if decrypted_password==password:
                        #successfully logged in
                        usernamelField.delete(0,END)
                        passwordlField.delete(0,END)
                        usernamelField.focus_force()
                        #when you login, create a session file 
                        with open('session.sqlite','a') as session:
                            session.write(username)
                        #load this field with the passwords 
                        passwords_enc=""
                        with open ('passwords.enc','r') as f:
                            passwords_enc = f.read()
                            passwordsEntry.insert(1.0,passwords_enc)
                        Dashboard.tkraise()
                    else:
                        messagebox.showerror("Invalid",f"Password Entered is Incorrect")
                        return
                    return
                else:
                    messagebox.showerror("Invalid",f"Username Entered is Invalid")
                    return
def SavePassword():
    passwordsEntry.delete(1.0,END)
    platform = str(platformField.get()).strip()
    password = str(generatedPassword.get())
    if platform and password:
        #encrypt the password using AES
        enc_password = AES.encrypt_password(password)
        # //save the password in a file 
        with open(passwords,'a') as f:
            content = f.write(f"{platform}:{enc_password}\n")
        generatedPassword.delete(0,END)
        platformField.delete(0,END)
        passwordLengthField.delete(0,END)
        messagebox.showinfo("Success",f"Password Saved")
        #read the passwords file 
        passwords_enc=""
        with open ('passwords.enc','r') as f:
            passwords_enc = f.read()
        passwordsEntry.insert(1.0,passwords_enc)
    else:
        messagebox.showerror("Error",f"Unknown Error Occurred")
        return
def GeneratePassword():
    generatedPassword.delete(0,END)
    #get the values from the fields
    platform = str(platformField.get()).strip()
    passwordLength =passwordLengthField.get()
    if passwordLength.isdigit():
        passwordLength = round(float(passwordLength),0)
        enc_pass = Generator.Generate(passwordLength)
        generatedPassword.insert(0,enc_pass)
        Button(framedash, text="Save Password", cursor="hand2", width=47,pady=7, bg="deeppink",fg="white",border=0,command=SavePassword).place(x=420,y=150,height=35)
        #read passwords file 
    else:
        passwordLengthField.delete(0,END)
        messagebox.showerror("Error",f"Password Length Should be a Number")
        return
def Sign_up():
    username=str(usernameSignUpField.get()).strip()
    password=str(passwordSignupField.get()).strip()
    cpassword=str(passwordConfirmField.get()).strip()
    if not username or not password or not cpassword:
        messagebox.showerror("Invalid",f"You cant Register with Blank Details")
    elif password != cpassword:
        messagebox.showerror("Invalid",f"Two password must match")
    else:
        # read a file and store the details there
        try:
            new_password = AES.encrypt_password(password)
            with open(database,'r') as usernames:
                for usernamer in usernames:
                    if str(str(usernamer).split(":")[0]).strip() ==username:
                        messagebox.showerror("Invalid",f"Please use a different Username")
                        return
            with open(database,'a') as f:
                data = f"{username}:{new_password}\n"
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
Decryptor.grid(row=0,column=0,sticky="nsew")
#####################################
#PLACING OBJECTS IN THE SIGN IN PAGE#
#####################################
image = Image.open("locked.jpg")
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
image2 = Image.open("vault.jpg")
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

Label(RegisterPage,text="Register With Us",fg='green', bg='white',font=("Maiandra GD",25,'bold','underline')).place(x=500,y=10)

frame2.pack(side=LEFT, expand=True,fill=BOTH)



#####################################
#PLACING OBJECTS IN THE DASHBOARD   #
#####################################
framedash = Frame(Dashboard, width=900, height=230)
Label(Dashboard,text="Welcome to a Secure Password Manager",fg='green',font=("Maiandra GD",25,'bold','underline')).place(x=50,y=10)
Button(Dashboard, text="Logout", cursor="hand2", width=20,pady=7, bg="red",fg="white",border=0,command=lambda: LoginPage.tkraise()).place(x=50,y=460,height=35)
Button(Dashboard, text="Decrypt A Password", cursor="hand2", width=20,pady=7, bg="deeppink",fg="white",border=0,command=showDecryptor).place(x=400,y=460,height=35)
platformLabel = Label(framedash,text="Platform", fg='green',font=("Maiandra GD",12))
platformLabel.place(x=50,y=60)
platformField = Entry(framedash,width=20,fg='green',borderwidth=15,border=0,font=("Times New Roman",12))
platformField.place(x=50,y=90,height=40)
textLabel = Label(framedash,text="Password Length",textvariable="number", fg='green',font=("Maiandra GD",12))
textLabel.place(x=230,y=60)
generatedPasswordLabel =Label(framedash,text="Generated Password", fg='deeppink',font=("Maiandra GD",12))
generatedPasswordLabel.place(x=420,y=60)
generatedPassword = Entry(framedash,width=50,fg='deeppink',borderwidth=15,border=0,font=("Times New Roman",12))
generatedPassword.place(x=420,y=90,height=40)
passwordLengthField = Entry(framedash,width=20,fg='green',border=0,font=("Times New Roman",12))
passwordLengthField.place(x=230,y=90,height=40)
Button(framedash, text="Generate Password", cursor="hand2", width=40,pady=7, bg="green",fg="white",border=0,command=GeneratePassword).place(x=50,y=150,height=35)
framedash.pack()
frameleft = Frame(Dashboard,width=900 ,height=220,bg="gray")
frameleft.place(x=0,y=231)
passwordsEntry = Text(frameleft)
passwordsEntry.place(x=0,y=0,width=900)

#adding frame to a decrypting password panel
decryFrame = Frame(Decryptor,width=900, height=500,bg="gray")
Label(Decryptor,text="Descrypt A Password",fg='green',font=("Maiandra GD",25,'bold','underline')).place(x=200,y=10)
Button(Decryptor, text="Logout", cursor="hand2", width=20,pady=7, bg="red",fg="white",border=0,command=lambda: LoginPage.tkraise()).place(x=50,y=460,height=35)
Button(Decryptor, text="Back", cursor="hand2", width=20,pady=7, bg="deeppink",fg="white",border=0,command=lambda: Dashboard.tkraise()).place(x=400,y=460,height=35)
EncryptedPasswordField = Entry(decryFrame,width=110,fg='deeppink',borderwidth=15,border=0,font=("Times New Roman",12))
EncryptedPasswordField.place(x=10,y=90,height=40)
Button(decryFrame, text="Decrypt Password", cursor="hand2", width=40,pady=7, bg="green",fg="white",border=0,command=DecryptPassword).place(x=10,y=150,height=35)
decryptedPasswordField = Text(decryFrame)
decryptedPasswordField.place(x=0,y=231,width=900)
decryFrame.pack()
LoginPage.tkraise()
root.title("Welcome to a Secure Password Manager")
root.geometry("900x500+200+100")
root.configure(bg="white")
root.resizable(False,False)

root.mainloop()