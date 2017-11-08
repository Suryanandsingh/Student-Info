from database import run_query
from tkinter import *
from tkinter import ttk, messagebox
# second page which is find the information of student

class Find:
    sett = 0
    def __init__(self, root, main):
        self.main = main
        self.root2 = root
        self.root2.title("Search")
        labelframe = LabelFrame(self.root2, text='Search')
        labelframe.grid(row=0, column=1)
        rollL = Label(labelframe, text="Roll No", font=('times', 20, 'bold'))
        rollL.grid(row = 1, padx=40, pady=30)
        orL = Label(labelframe, text="or", font=('times', 15, 'bold'))
        orL.grid(row=2, column=1)
        regL = Label(labelframe, text="Reg No", font=('times', 20, 'bold'))
        regL.grid(row=3, padx=40, pady=30)
        self.roll = Entry(labelframe)
        self.roll.grid(row=1, column=1)
        self.reg = Entry(labelframe)
        self.reg.grid(row=3, column=1)




        self.find = Button(labelframe, text='Ok', command=self.find, font=('times', 15, 'bold'))
        self.find.grid(row=4, column=0)
        self.back = Button(labelframe, text='Back', command=self.finish ,font=('times', 15, 'bold'))
        self.back.grid(row=4, column=1)



    #validation your registration number or roll number empty
    def valid(self):
        return len(self.reg.get())!=0 or len(self.roll.get()) !=0

    #for searching data which you want to search
    def find(self):
        if self.valid():
            query=''
            if self.reg.get():
                query = "SELECT * FROM students_info WHERE Reg = %s" % (self.reg.get())#UNION SELECT * FROM students_info WHERE Name = %s " % (self.reg.get(), self.name.get())
            else:
                query = "SELECT * FROM students_info WHERE Name ="+"'"+self.roll.get()+"'"
            # print(query)
            c = run_query(query)
            a = 0
            for i in c:
                # print(i)
                if i[0:]:
                    Geometry(self.root2, 690, 350)
                    # Tree View
                    a = 1
                    self.tree = ttk.Treeview(self.root2, height=5, column=2)
                    self.tree.grid(row=0, column=4, columnspan=3)
                    self.tree.heading('#0', text='Details', anchor=CENTER)
                    self.tree.heading('#1', text='Values', anchor=CENTER)

                    # print information

                    self.tree.insert('', 0, text='Name', values=i[0:])
                    self.tree.insert('', 1, text='Roll', values=i[1])
                    self.tree.insert('', 2, text='Reg', values=i[2])
                    self.tree.insert('', 3, text='Course', values=i[3:])
                    self.tree.insert('', 4, text='Address', values=i[4:])

                    #update button
                    self.upbtn = Button(self.root2, text='Update', command=self.select, font=('times', 13, 'bold'))
                    self.upbtn.grid(row=4, column=5)
            if a == 0:
                messagebox.showerror('error', 'this key is not available')
        else:
            messagebox.showerror('error', 'Enter any answer')#error
            # Label(self.root2, text='Please choose any option', fg='red', font=('times', 10, 'bold')).grid(row=5 ,column=1)

    # select information update
    def select(self):
        try:
            self.updat = self.tree.item(self.tree.selection())['values'][0]
            self.text = self.tree.item(self.tree.selection())['text']
            # print(updat)
            self.Update()
        except IndexError as e:
            messagebox.showerror('error', 'Please select any info to update')#error



    #destroy second window and call first window
    def finish(self):

        self.root2.destroy()
        self.main.deiconify()


    #update your selected information
    def Update(self):

        self.Upwin = Toplevel()
        self.Upwin.title('update')
        Geometry(self.Upwin, 120, 230)
        self.Upwin.minsize(height=120, width=230)
        self.main_frame=Frame(self.Upwin,height=120,width=230)
        self.main_frame.pack()
        self.msg_label=Label(self.main_frame, text='Enter your new data', font=('times',15,'bold'))
        self.msg_label.grid(row=1, column=2, padx=5, pady=11)
        self.upd = Entry(self.main_frame)
        self.upd.grid(row=2, column=2, padx=5, pady=11)
        self.ok=Button(self.main_frame, text='Ok', command=self.set, font=('times',15,'bold'))
        self.ok.grid(row=3, column=2, padx=5, pady=11)

    # set into database which data you select for update
    def set(self):
        if len(self.upd.get()) !=0:
            query = 'UPDATE students_info SET %s = ? WHERE %s = ? ' % (self.text, self.text)
            parameters = (self.upd.get(), self.updat )
            run_query(query, parameters)
            messagebox.showinfo('save', 'your data updated ')
            self.tree.destroy()
            self.upbtn.destroy()
            self.reg.delete(0, END)
            self.roll.delete(0, END)
            self.Upwin.destroy()
            Geometry(self.root2, 350, 300)
        else:
            messagebox.showerror('error', 'please enter data')

def Geometry(root, width, height):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - width) / 2
    y = (sh - height) / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def mains(root):
    window = Toplevel()
    width = 350
    height = 300
    window.minsize(width=width, height=height)
    Geometry(window, width, height)
    apps = Find(window, root)
    window.protocol('WM_DELETE_WINDOW',apps.finish)
