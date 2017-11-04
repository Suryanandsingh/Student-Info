import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

db_name = 'students_info.db'


# first page which is save data into database and go to find the data another page
class student:
    f = 1
    def __init__(self, root):
            self.root=root
            self.root.title("Information")
            info = Label(self.root, text="Student Info", fg='blue', font=('times', 30, 'bold'))
            info.grid(row=0, column=1)
            nameL = Label(self.root, text="Name", font=('times', 20, 'bold'))
            nameL.grid(padx=40, pady=20)
            rollL = Label(self.root, text="Roll No", font=('times', 20, 'bold'))
            rollL.grid(padx=40, pady=20)
            regL = Label(self.root, text="Reg No", font=('times', 20, 'bold'))
            regL.grid(padx=40, pady=20)
            courseL = Label(self.root, text="Course", font=('times', 20, 'bold'))
            courseL.grid(padx=40, pady=20)
            addressL = Label(self.root, text="Address", font=('times', 20, 'bold'))
            addressL.grid(padx=40, pady=20)
            DOBL = Label(self.root, text='Date of Birth', font=('times', 20, 'bold'))
            DOBL.grid(padx=40, pady=20)

            self.name = Entry(self.root)
            self.roll = Entry(self.root)
            self.reg = Entry(self.root)
            self.course = Entry(self.root)
            self.address = Entry(self.root)
            self.DOB = Entry(self.root)
            self.name.grid(row=1, column=1)
            self.roll.grid(row=2, column=1)
            self.reg.grid(row=3, column=1)
            self.course.grid(row=4, column=1)
            self.address.grid(row=5, column=1)
            self.DOB.grid(row=6, column=1)


            save = Button(self.root, text="Save", command=self.data_entry, font=('times', 15, 'bold'))
            save.grid(row=7, column=0)
            search = Button(self.root, text='Find', command=self.search, font=('times', 15, 'bold'))
            search.grid(row=7, column=1)
            clear = Button(self.root, text="Clear", command=self.clear, font=('times', 15, 'bold'))
            clear.grid(row=7, column=2)

            #only for first time execution
            if self.f == 0:
                self.create_table()





    #create table into database
    def create_table(self):
        query = 'CREATE TABLE students_info(Name text, Roll real,Reg integer, Course text, Address text, DOB text, PRIMARY KEY(Reg))'
        run_query(query)

    #validation any column is empty or not
    def validation(self):
        return len(self.name.get()) != 0 and len(self.roll.get()) != 0 and len(self.course.get()) != 0 and len(self.reg.get())!=0 and len(self.address.get())!=0 and len(self.DOB.get()) !=0

    #for primary key checking
    def Primarycheck(self):

        query = 'SELECT Reg FROM students_info WHERE Reg = %s  '% self.reg.get()
        c = run_query(query)
        for i in c:
            if i[0]:
                return False

        return True



    #insert data into database
    def data_entry(self):
        if self.validation():
            # if
            if self.Primarycheck():
                query = 'INSERT INTO students_info VALUES(?, ?, ?, ?, ?, ?)'
                parameters = (self.name.get(), self.roll.get(), self.reg.get(), self.course.get(), self.address.get(), self.DOB.get())
                run_query(query, parameters)
                messagebox.showinfo('save', 'Student information saved')
                self.clear()
                self.name.index(INSERT)
                self.name.index(INSERT)
            else:
                messagebox.showerror('error', 'this registration already exist')
                self.clear()

        else:
            messagebox.showerror('save', 'Please enter information!')



    #clear data
    def clear(self):
        self.name.delete(0, END)
        self.roll.delete(0, END)
        self.reg.delete(0, END)
        self.course.delete(0, END)
        self.address.delete(0, END)
        self.DOB.delete(0, END)

    #for find the student information
    def search(self):
        window = Tk()
        width = 320
        height = 250
        window.minsize(width=width, height=height)

        # Gremetry(window, width, height)
        app2 = Find(window) # Find class down

        #destroy first window
        self.root.destroy()

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






# connectivity database
def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        query_re = c.execute(query, parameters)
        conn.commit()
    # print(query_re)
    return query_re


# screen set
def Gremetry(root, width, height):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - width) / 2
    y = (sh - height) / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

#main
def main():
    root = Tk()

    width = 570
    height = 600
    root.minsize(width=width, height=height)
    Gremetry(root, width, height)
    app = student(root)
    root.mainloop()


if __name__ == '__main__':
    main()