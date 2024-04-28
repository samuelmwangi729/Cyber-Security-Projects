from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Login TO Text Streganography App")
root.geometry("900x500+200+100")
root.configure(bg="white")
root.resizable(False,False)
#create components
image = Image.open("login.jpg")
width= 450
height=500
image = image.resize((width,height))
photo = ImageTk.PhotoImage(image)
Label(root,image=photo).place(x=0,y=0)

#add a frame for the objects 
frame = Frame(root, width=450, height=500, bg="white")
frame.place(x=450,y=0)
#heading label to the frame 
heading = Label(frame,text="Sign In", fg='green', bg='white',font=("Maiandra GD",25,'bold','underline'))
heading.place(x=180,y=20)
#add username field 
usernameLabel = Label(frame,text="Username", fg='green', bg='white',font=("Maiandra GD",12))
usernameLabel.place(x=40,y=95)
usernameField = Entry(frame,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12))
usernameField.place(x=40,y=120,height=35)
usernameField.insert(0," ")
usernameField.focus_force() 
# pasword field
passwordLabel = Label(frame,text="Password", fg='green', bg='white',font=("Maiandra GD",12,))
passwordLabel.place(x=40,y=170)
passwordField = Entry(frame,width=40,fg='green',border=0,bg='white',font=("Times New Roman",12),show="*")
passwordField.place(x=40,y=195,height=35)
#button here
button = Button(frame, text="Sign In", cursor="hand2",width=37,pady=7, bg="green",fg="white",border=0)
button.place(x=40,y=250,height=35)

##allow users to register
Label(frame,text="Do not have an Account?",fg='green', bg='white',font=("Maiandra GD",12,)).place(x=40,y=300)
Button(frame, text="Sign Up", cursor="hand2", width=10,pady=7, bg="green",fg="white",border=0).place(x=255,y=295,height=35)
mainloop()