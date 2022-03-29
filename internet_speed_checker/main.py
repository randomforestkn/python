from tkinter import *
from tkinter import messagebox
import pyspeedtest

def logic():
    st = pyspeedtest.SpeedTest("www.google.com")
    a = (str(st.download())+"[Bytes per second]")
    print(a)
    a = round(float(a[:-18]) / 125000, 3)
    messagebox.showinfo("Your download speed: ", str(a)+" Mbps")
    # b = (str(st.upload())+"[Bytes per second]")
    # messagebox.showinfo("Your upload speed:", b)

root = Tk()
root.title("My Speed Test")
root.geometry('900x700')
filename = PhotoImage(file="speedtest-preview.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

c = Button(root,text='Click to see the internet speed',font=('San serif',20),bg='Blue',height=1,width=30, command=logic).pack()
root.mainloop()
