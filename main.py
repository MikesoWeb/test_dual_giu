from tkinter import *
from tkinter import messagebox
 
def add_message():
  if message_entry.get() != '':
    message_entry1.insert(0, message.get())
    
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x200+150+150")
 
message = StringVar()
add = StringVar() 



message_entry = Entry(textvariable=message)
message_entry.place(x=150, y=50, anchor="c")

message_entry1 = Entry(textvariable=add)
message_entry1.place(x=150, y=100, anchor="c")
 
message_button = Button(text="Click Me", command=add_message)
message_button.place(x=150, y=150, anchor="c")
 
root.mainloop()

