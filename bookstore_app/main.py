from tkinter import *
import backend
from ttkthemes import themed_tk as tk
from tkinter import ttk

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def entry_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

#  window= Tk()
window = tk.ThemedTk()
window.title(string="Database")
window.get_themes()
window.set_theme("plastik")
window.configure(bg='lightgrey')

label1 = ttk.Label(window, text="Τίτλος")
label1.grid(row=0,column=0)

label3 = ttk.Label(window, text="Συγγραφέας")
label3.grid(row=0,column=2)


label2 = ttk.Label(window, text="'Ετος")
label2.grid(row=1,column=0)


label4 = ttk.Label(window, text="Σειριακός αριθμός")
label4.grid(row=1,column=2)


title_text = StringVar()
entry1 = ttk.Entry(window, textvariable=title_text)
entry1.grid(row=0,column=1)

author_text = StringVar()
entry2 = ttk.Entry(window, textvariable=author_text)
entry2.grid(row=0,column=3)

year_text = StringVar()
entry3 = ttk.Entry(window, textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text = StringVar()
entry4 = ttk.Entry(window, textvariable=isbn_text)
entry4.grid(row=1,column=3)

list1 = Listbox(window, height = 10, width = 26, fg="black")
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window, width = 12, bg="grey")
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

button1 = ttk.Button(window, text="Προβολή Όλων", width=17, command=view_command)
button1.grid(row=2,column=3)

button2 = ttk.Button(window, text="Αναζήτηση", width=17, command=search_command)
button2.grid(row=3,column=3)

button3 = ttk.Button(window, text="Εισαγωγή", width=17, command=entry_command)
button3.grid(row=4,column=3)

button4 = ttk.Button(window, text="Ενημέρωση", width=17, command = update_command)
button4.grid(row=5,column=3)

button5 = ttk.Button(window, text="Διαγραφή", width=17, command=delete_command)
button5.grid(row=6,column=3)

button6 = ttk.Button(window, text="Έξοδος", width=17, command=window.destroy)
button6.grid(row=7,column=3)

window.mainloop()
