import tkinter as tk
import time as tm

class Psifiako:
    def __init__(self,root):
        self.root = root
        self.root.wm_attributes('-toolwindow', True,"-alpha",0.9)
        self.root.title('Ψηφιακό ρολόι')
        self.root.iconbitmap('clock.ico')
        self.root.resizable(height = False, width = False)
        self.roloi_label=tk.Label(self.root,font='ariel 30',bg='black',fg='green')
        self.roloi_label.grid(row=0,column=0)
        self.menou()
        self.apotiposi()
        

    def menou(self):
        self.my_menou = tk.Menu(self.root)
        self.my_dropdown_menu = tk.Menu(self.my_menou, tearoff=False)
        self.my_dropdown_menu.add_command(label='Μικρό', command=self.mikro_mege8os)
        self.my_dropdown_menu.add_command(label='Μεσαίο', command=self.mesaio_mege8os)
        self.my_dropdown_menu.add_command(label='Μεγάλο ', command=self.megalo_mege8os)
        
        self.my_dropdown_menu2 = tk.Menu(self.my_menou, tearoff=False)
        self.my_dropdown_menu2.add_command(label='Άσπρο', command=self.white_colour)
        self.my_dropdown_menu2.add_command(label='Κόκκινο', command=self.red_colour)
        self.my_dropdown_menu2.add_command(label='Κίτρινο ', command=self.yellow_colour)
        self.my_dropdown_menu2.add_command(label='Μπλε ', command=self.blue_colour)
        self.my_dropdown_menu2.add_command(label='Πράσινο ', command=self.green_colour)
        
        
        self.my_menou.add_cascade(label='Μέγεθος',menu=self.my_dropdown_menu)
        self.my_menou.add_cascade(label='Χρώμα',menu=self.my_dropdown_menu2)
        self.my_menou.add_command(label='Έξοδος',command=self.quit_app)
        self.root.config(menu=self.my_menou)

    def mikro_mege8os(self):
        self.roloi_label['font']="ariel 10"

    def mesaio_mege8os(self):
        self.roloi_label['font']="ariel 20"

    def megalo_mege8os(self):
        self.roloi_label['font']="ariel 30"

    def white_colour(self):
        self.roloi_label['bg']='white'
        self.roloi_label['fg']='black'

    def red_colour(self):
        self.roloi_label['bg']='red'
        self.roloi_label['fg']='black'

    def yellow_colour(self):
        self.roloi_label['bg']='yellow'
        self.roloi_label['fg']='black'

    def blue_colour(self):
        self.roloi_label['bg']='blue'
        self.roloi_label['fg']='black'
        
    def green_colour(self):
        self.roloi_label['bg']='green'
        self.roloi_label['fg']='black'

    def quit_app(self):
        self.root.destroy()

    def apotiposi(self):
        self.wra = tm.strftime('%A %d %B %Y  \n%H:%M:%S')
        self.roloi_label['text']=self.wra
        self.root.after(150,self.apotiposi)

root = tk.Tk()
root2 = tk.Tk()
psifiako_roloi = Psifiako(root)
psifiako_roloi = Psifiako(root2)
root.mainloop()
