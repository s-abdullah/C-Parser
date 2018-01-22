# import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()

# from Tkinter import *
# top = Tk()
# L1 = Label(top, text=" Enter Filename: ")
# L1.pack( side = LEFT)
# E1 = Entry(top, bd =5)
#
# E1.pack(side = RIGHT)
#
# top.mainloop()


import Tkinter
import os
import switch as project

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        print "\n" * 100
        self.geometry('{}x{}'.format(480, 240))

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW',padx=180,pady=75)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.bind("<Escape>", self.End)
        self.entryVariable.set(u"Enter Filename")

        # button = Tkinter.Button(self,text=u"Enter!",
        #                         command=self.OnButtonClick)
        # # button.grid(column=5,row=9)
        # button.place(height=360,width=100)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="red")
        # label.place(width=480)
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"No File Selected!")
        self.update()
        self.geometry(self.geometry())
        # self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    # def OnButtonClick(self):
    #     self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
    #     self.entry.focus_set()
    #     self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        entered = self.entryVariable.get()
        length = len(entered)

        if entered[length-3:] == 'txt':
            if os.path.isfile(entered):
                self.labelVariable.set( " Selected File: " + entered )
                print "\n" * 100
                project.huehue(entered)
                self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)
            else:
                self.labelVariable.set( " Selected File Does Not Exist ")
                self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)
        else :
            # print entered
            self.labelVariable.set( " Please Enter Valid Filename!" )
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)
            # print 'HOOROAAAHH'

        # self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)

    def End(self,event):
        print "EXITING PROGRAM..."
        exit();
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
