from tkinter import *
from tkinter.ttk import Combobox,Style
from tkinter import messagebox 
import string, random

root = Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg="white")
root.resizable(False,False)

def password_generate():
  try:
    length_password=solidboss.get()
    small_letters=string.ascii_lowercase
    capital_letters=string.ascii_uppercase
    digits=string.digits
    special_character=string.punctuation
    all_list=[]
    all_list.extend(list(small_letters))
    all_list.extend(list(capital_letters))
    all_list.extend(list(digits))
    all_list.extend(list(special_character))
    random.shuffle(all_list)
    password.set("".join(all_list[0:length_password]))
  except:
    messagebox.askretrycancle("A Problem Has Been Occured","Please Try Again")
    
all_no = {"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10"}

Title = Label(root, text="Password Generator", bg="white", fg="blue", font=("futura",15,"bold"))
Title.pack(anchor="center", pady="20px")


length = Label(root, text="Enter Password Length :", fg="black", bg="white", font=("ubuntu", 12, "bold"))
length.place(x="20px", y="65px")

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "blue"
    generate_btn['fg'] = "black"

solidboss=IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly"  )
Selector['values']=[l for l in all_no.keys()]
Selector.current(7)
Selector.place(x="180px", y="66px")


generate_btn=Button(root, text="Generate Password", bg="blue", fg="white", font=("ubuntu", 15), cursor="hand2", command=password_generate)

generate_btn.pack(anchor="center",pady="50px")

generate_btn.bind("<Enter>",on_enter)
generate_btn.bind("<Leave>",on_leave)

result_label = Label(root, text="Generated Password: ", bg="white", fg="black", font=("ubuntu",12, "bold"))
result_label.place(x="20px", y="170px")

password = StringVar()
password_final = Entry(root, textvariable=password, state="readonly", fg="black", font=("ubuntu", 15), width=15)
password_final.place(x="180px", y="169px")
root.mainloop()