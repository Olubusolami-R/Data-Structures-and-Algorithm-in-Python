import tkinter

class mygui:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)
        
        self.nameVar=tkinter.StringVar()
        self.addVar=tkinter.StringVar()
        
        self.name_label=tkinter.Label(self.top_frame,textvariable=self.nameVar)
        self.address_label=tkinter.Label(self.bottom_frame,textvariable=self.addVar)

        self.name_label.pack(side='top')
        self.address_label.pack(side='top')

        self.info_button=tkinter.Button(self.button_frame,text='Show Info',command=self.display)
        self.quit_button=tkinter.Button(self.button_frame,text='Quit',command=self.main_window.destroy)

        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        
        tkinter.mainloop()
    def display(self):
        self.name='Roman'
        self.address='World'

        self.nameVar.set(self.name)
        self.addVar.set(self.address)
        
        
gui=mygui()
