import string
from random import randint,choice
from tkinter import *
import tkinter.messagebox as tmsg
import pyperclip
import easygui

#function for generating password
def pass_gen():
    all_chars = string.ascii_letters +string.punctuation +string.digits 
    password = "".join(choice(all_chars) for x in range(myslider.get()))        
    password_entry.delete(0,END)
    password_entry.insert(0,password)

def save_pass():
    file = open("mypassword.txt","w")
    file.writelines(password_entry.get())
    file.close()
    file = easygui.filesavebox()
    # msg=tmsg.askquestion("Save As","Do you want to save?")
    # print(msg)
def Copy_password():
    pyperclip.copy(password_entry.get())

#Defining the Window
window = Tk()
window.title("Pass-Gen")
window.geometry("700x500")
window.iconbitmap("Images/logo.ico")
window.config(background='#002447')

#main Frame
frame = Frame(window,bg='#002447')

#Image
width = 340
height = 488
img = PhotoImage(file="Images/lock-icon-1.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#002447', bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=img)
canvas.grid(row=0,column=0,sticky=W)

right_frame = Frame(frame, bg='#002447')

#Application Label
label_title = Label(right_frame,text="Password Generator",font=("lucida",25,"bold","underline"),bg='#002447',fg='Yellow',pady=10)
label_title.pack()

pass_len = Label(right_frame,text="Choose your password Length:",font=("lucida",15),bg='#002447',fg='light blue',pady=3)
pass_len.pack()

myslider=Scale(right_frame, from_=5, to=20,orient=HORIZONTAL,tickinterval=5,bg='#002447',fg='light blue',highlightthickness=0)
myslider.pack(fill=X)

#appearing password text box
password_entry = Entry(right_frame,font=("Helvetica",20),bg='#002447',fg='PeachPuff')
password_entry.pack(fill=X, pady=10)

# footer_title = Label(text="Python Miniproject | Tejas Manasi Prerana Mahendra | DMCE", font="Sanseriff 10",bg='#002447',fg='grey',borderwidth=1,relief=RIDGE,pady=5)
# footer_title.pack(side=BOTTOM,fill=X)

generate_password_button = Button(right_frame,text="Generate",font=("Helvetica",20),bg='#002447',fg='white',command=pass_gen,borderwidth=5,relief=RAISED)
generate_password_button.pack(fill=X)

save_pw_button = Button(right_frame,text="Save",font=("Helvetica",20),bg='#002447',fg='white',command=save_pass,borderwidth=5,relief=RAISED)
save_pw_button.pack(fill=X)

copy_pw_button = Button(right_frame,text="Copy to clipboard",font=("Helvetica",20),bg='#002447',fg='white',command=Copy_password,borderwidth=5,relief=RAISED)
copy_pw_button.pack(fill=X)

right_frame.grid(row=0, column=1,sticky=W)

frame.pack(expand=YES)

#Menu Bar
main_menu = Menu(window)

m1 = Menu(main_menu,tearoff=0)
m1.add_command(label="New",command=pass_gen)
m1.add_command(label="Save", command=save_pass)
m1.add_separator()
m1.add_command(label="Save As", command=save_pass)
m1.add_command(label="Quit", command=window.quit)
main_menu.add_cascade(label="Menu",menu=m1)
window.config(menu=main_menu)

m2 = Menu(main_menu,tearoff=0)
m2.add_command(label="Log", command=window.quit)
m2.add_command(label="Help", command=window.quit)

main_menu.add_cascade(label="Options",menu=m2)
window.config(menu=main_menu)

#writing to files
# with open("records.txt","a") as f:
#     f.write(f"{title.get(), username.get(), password.get()}\n")
#display Window

    
window.mainloop()