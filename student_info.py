from database import run_query
from tkinter import *
from tkinter import messagebox
import search


# first page which is save data into database and go to find the data another page
class student:
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
        app2 = search.Find(window) # Find class down

        #destroy first window
        self.root.destroy()

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