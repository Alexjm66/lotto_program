from tkinter import *
from tkinter import messagebox
from random import sample

root=Tk()
root.title("Lottery Program")
root.geometry("500x350")
root.config(bg="White")

def login():
    try:
        age = age_entry.get()
        ages = int(age)

        if ages <18:
            messagebox.showerror("Error","You're to Young " +  name_entry.get())
        else:
            messagebox.showinfo("","Welcome " + name_entry.get())

    except ValueError:
        messagebox.showerror("Error", "Please Enter a Number")

def exit():
    root.destroy()

welcome=Label(root,text="Welcome To",bg="gold", fg="black", width="500", height="1", font=['Arial',23,'bold'])
welcome.pack()

wel=Label(root,text="Ithuba Lottery", bg="gold", fg="black", width="500", font=['Arial',23,'bold'])
wel.pack(side=BOTTOM)

name=Label(root, text="Name", bg="white")
name.place(x = 10, y = 90)

name_entry=Entry(root)
name_entry.place(x = 90, y = 90)

surname=Label(root, text="Surname",bg="white")
surname.place(x = 10, y =121)
surname_entry=Entry(root)
surname_entry.place(x = 90, y = 120)

age=Label(root, text="Age",bg="white")
age.place(x = 10, y = 153)

age_entry=Entry(root)
age_entry.place(x = 90, y = 150)

login_btn=Button(root, text="Login",width="10", font=["Arial",15,"bold"], command=login)
login_btn.place(x = 10, y = 230)

exit_btn=Button(root, text="Exit Program",width="12", font=["Arial",15,"bold"], command=exit)
exit_btn.place(x = 160, y = 230)


def lotto_numbers():
    lotto_numbers = Tk()
    lotto_numbers.title("Play The Lotto")
    lotto_numbers.geometry("500x350")
    lotto_numbers.config(bg="white")

    play_label=Label(lotto_numbers, text="Time To Play", bg="gold", width=500, font=['Arial', 24, "bold"])
    play_label.pack()

    intro=Label(lotto_numbers,text="These are the Lotto Numbers",bg="white", fg="red",font=['Arial', 18,"bold"])
    intro.pack()

    lblframe=LabelFrame(lotto_numbers,text="Lucky Number", padx=120, bg="gold", fg="red")
    lblframe.pack(fill="both")

    intro1=Label(lotto_numbers, text="Enter Your Lucky Numbers: (1, 49)",bg="white", fg="red",font=['Arial', 18,"bold"])
    intro1.pack()

    lblframe1=LabelFrame(lotto_numbers, text="Number Entry", padx=93, pady=10, bg="gold", fg="red")
    lblframe1.pack(fill="both")

    label1=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label1.grid(row=1, column=1,padx=10)
    label2=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label2.grid(row=1, column=2, padx=10)
    label3=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label3.grid(row=1, column=3, padx=10)
    label4=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label4.grid(row=1, column=4, padx=10)
    label5=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label5.grid(row=1, column=5, padx=10)
    label6=Label(lblframe, text="", bg="gold", font=["Arial", 15, "bold"])
    label6.grid(row=1, column=6, padx=10)

    num1 = Entry(lblframe1, width=5)
    num1.grid(row=0, column=1, padx=3)

    num2 = Entry(lblframe1, width=5)
    num2.grid(row=0, column=2, padx=3)

    num3 = Entry(lblframe1, width=5)
    num3.grid(row=0, column=3, padx=3)

    num4 = Entry(lblframe1, width=5)
    num4.grid(row=0, column=4, padx=3)

    num5 = Entry(lblframe1, width=5)
    num5.grid(row=0, column=5, padx=3)

    num6 = Entry(lblframe1, width=5)
    num6.grid(row=0, column=6, padx=3)

    winlbl=Label(lotto_numbers,text="Press To Find Out If You Win",bg="white",fg="red",font=["Arial",18,"bold"])
    winlbl.pack()

    click_btn=Button(lotto_numbers, text="Click",width="10", font=["Arial",12,"bold"])
    click_btn.place(x = 190, y = 260)

    endlabel=Label(lotto_numbers,text="@ithubaLottery",bg="gold", fg="black",width="500", font=["Arial", 20, "bold"])
    endlabel.pack(side=BOTTOM)

    def entries():
        n1=int(num1.get())
        n2=int(num2.get())
        n3=int(num3.get())
        n4=int(num4.get())
        n5=int(num5.get())
        n6=int(num6.get())

        numlist=[n1,n2,n3,n4,n5,n6]
        return numlist

    def random_numbers():
        random_no = sample(range(1, 49 ), 6)
        random_no.sort()
        label1.configure(text=random_no[0])
        label2.configure(text=random_no[1])
        label3.configure(text=random_no[2])
        label4.configure(text=random_no[3])
        label5.configure(text=random_no[4])
        label6.configure(text=random_no[5])

        print(random_no)


        count =0

        for num in entries():
            if num in random_no:
                count += 1
            print(count)
        if count <= 1:
            messagebox.showerror("Attetion","You got 1 number, unfortunately you won nothing. Please login again to play")
            lotto_numbers.destroy()

        elif count == 2:
            messagebox.showinfo("Congratz", "You Won R20.00")
            lotto_numbers.destroy()
        elif count == 3:
            messagebox.showinfo("Congrtaz","You won R100.50")
            lotto_numbers.destroy()
        elif count == 4:
            messagebox.showinfo("Congrtaz","You won R2.384")
            lotto_numbers.destroy()
        elif count == 5:
            messagebox.showinfo("Congrtaz","You won R8.584.00")

        elif count == 6:
            messagebox.showinfo("Congrtaz","You won R10.000 000.00")
            lotto_numbers.destroy()

    click_btn.configure(command=random_numbers)

root.mainloop()
