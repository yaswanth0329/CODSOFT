
from tkinter import *
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())
    entry.delete(0,END)
def delete():
    listbox.delete(listbox.curselection())
    list.config(height=listbox.size())

window=Tk()
window.geometry("800x800")
window.title("To Do List")
label1=Label(window,
       text="To-Do List",
       font=("Courier",30,"italic"),
       fg="white",
       bg="green",
       width=150,
       height=4,
       relief=RAISED
       )
label1.pack()
label2=Label(window,
        text="Add Items:",
        font="red"
        )
label2.place(x=10,y=160)

entry=Entry(window,
      font=("Courier",25),
      fg="black"
      )
entry.place(x=20,y=200)

addbutton=Button(window,
          text="Add task",
          bg="yellow",
          fg="black",
          font=("Courier",14),
          command=add,
          relief=RAISED,
          bd=5
           )
addbutton.place(x=400,y=200)

deletebutton=Button(window,
             text="remove",
             bg="blue",
             fg="black",
             font=("Courier",13),
             command=delete,
             relief=RAISED,
             bd=5
             )
deletebutton.place(x=520,y=200)


label3=Label(window,
       text="Task to do",
       font=("Courier",25),
       fg="Purple"
       )
label3.place(x=300,y=240)


listbox=Listbox(window,
        width=100,
        fg="black",
        font=("Courier",30),
        bg="lightgrey"
        )
listbox.place(x=20,y=320)


window.mainloop()
    