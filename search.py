from database import run_query
from tkinter import *
from tkinter import ttk, messagebox
from student_info import main

# second page which is find the information of student
class Find:
    def __init__(self, root2):
        self.root2 = root2
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
                query = "SELECT * FROM students_info WHERE Reg = %s " % (self.reg.get())#UNION SELECT * FROM students_info WHERE Name = %s " % (self.reg.get(), self.name.get())
            else:
                query = "SELECT * FROM students_info WHERE Roll = %s " % (self.roll.get())
            # print(query)
            c = run_query(query)
            a = 0
            for i in c:
                if i[0]:
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
            messagebox.showerror('error', 'Enter any answer')
            # Label(self.root2, text='Please choose any option', fg='red', font=('times', 10, 'bold')).grid(row=5 ,column=1)

    # select information update
    def select(self):
        try:
            self.updat = self.tree.item(self.tree.selection())['values'][0]
            self.text = self.tree.item(self.tree.selection())['text']
            # print(updat)
            self.Update()
        except IndexError as e:
            messagebox.showerror('error', 'Please select any info to update')



    #destroy second window and call first window
    def finish(self):

        self.root2.destroy()
        main()

    #update your selected information
    def Update(self):

        self.Upwin = Tk()
        self.Upwin.title('update')
        self.Upwin.minsize(height=150, width=230)
        Label(self.Upwin, text='Enter your new data', font=('times',15,'bold')).grid(row=1, column=2)
        self.upd = Entry(self.Upwin)
        self.upd.grid(row=2, column=2)
        Button(self.Upwin, text='Ok', command=self.set, font=('times',15,'bold')).grid(row=3, column=2)

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
            self.Upwin.destroy()
        else:
            messagebox.showerror('error', 'please enter data')
