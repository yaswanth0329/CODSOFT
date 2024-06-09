from tkinter import *
import random
from tkinter import messagebox

def results():
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    symbol="#@$^&*()<>%"

    length=int(ulenght.get())

    option=choice.get()

    if option==1 and(length>=8 and length<=20):
        messagebox.showinfo("Note","Weak passwords consists of only lowercase alphabets")
        g_pass="".join(random.choices(lowercase,k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)

    elif option==2 and(length>=8 and length<=20):
        messagebox.showinfo("Note","Normal passwords does not include symbols")
        g_pass="". join(random.choices(uppercase+lowercase+numbers,k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)

    elif option==3 and(length>=8 and length<=20):
        g_pass="".join(random.choices(uppercase+lowercase+numbers,k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)
    else:
        messagebox.showerror("ERROR","Specify the length and complexity of your passsword as per to the instructions")

ui=Tk()
ui.geometry("600x600")
ui.resizable(False,False)
ui.config(bg="lightblue")
ui.title("internship(Task)")

frame1=Frame(ui,bg="yellow")
frame1.pack(fill="x")
heading=Label(frame1,text="Random Password Generator",font="aerial 24 bold",bg="yellow")
heading.pack(pady=10)

frame2=Frame(ui,bg="lightblue")
frame2.place(x=10,y=60)
len=Label(frame2,text="1.LENGTH(Specify the length of your password in the rangefrom8~20)",font="arial 16 bold",bg="lightblue",wraplength=580)
len.pack(pady=1)
ulenght=Entry(frame2,font="arial 15")
ulenght.pack()

choice=IntVar()

frame3=Frame(ui,bg="lightblue")
frame3.place(x=10,y=140)
com=Label(frame3,text="2.COMPLEXITY(Select the complexity type of your password)",font="arial 16 bold" ,bg="lightblue",wraplength=580)
com.pack(pady=20)
easy=Radiobutton(frame3,text="Weak",variable=choice,bg="yellow",wraplength=60,font="arial 16",value=1)
easy.pack(anchor="nw")
normal=Radiobutton(frame3,text="Normal",variable=choice,bg="yellow",wraplength=100,font="arial 16",value=2)
normal.pack()

hard=Radiobutton(frame3,text="Strong",variable=choice,bg="yellow",wraplength=100,font="arial 16",value=3)
hard.pack(anchor="ne")
bt=Button(ui,text="Create Password and copy",font="arial 12 bold",command=results,borderwidth=10,bg="yellow")
bt.place(x=170,y=380)

password=Label(ui,text="",font="arial 24 bold",bg="white",borderwidth=10,wraplength=2500)
password.place(x=150,y=315)

ui.mainloop()          