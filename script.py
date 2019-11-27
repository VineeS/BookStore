from tkinter import *
import backend

window = Tk()

window.wm_title("Vin's Book Store")

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[2])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.ViewAll():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.Search(e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get()):
        list1.insert(END, row)

def add_command():
    backend.Insert(e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get())
    list1.delete(0,END)
    list1.insert(END,(e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get()))

def delete_command():
    backend.Delete(selected_tuple[0])

def update_command():
    backend.Update(selected_tuple[0],e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get())






# label for the tab 
l1 = Label(window, text = "Title")
l1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)
# Year
l2 = Label(window, text = "Year")
l2.grid(row=1,column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 1, column = 1)
# Author
l3 = Label(window, text = "Author")
l3.grid(row=0,column=2)

e3_value = StringVar()
e3 = Entry(window, textvariable = e3_value)
e3.grid(row = 0, column = 3)
# ISBN
l4 = Label(window, text = "ISBN")
l4.grid(row=1,column=2)

e4_value = StringVar()
e4 = Entry(window, textvariable = e4_value)
e4.grid(row = 1, column = 3)

# Buttons view all , Search Entry,Add Entry , Update Selected, Delete selected , close

b1 = Button(window, text = "View All",width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry",width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry",width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected",width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete selected",width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close",width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

# Text Box controlled by scroll
list1 = Listbox(window, height = 6 ,width =35)
list1.grid(row = 2, column = 0,rowspan = 6, columnspan = 2)


sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)



window.mainloop()
