from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from training import *

xaxis1 = 10
yaxis1 = 10
xaxis2 = 50
yaxis2 = 15
row = 2


def make_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=800, height=550)


def username_focusout(event, user):
    if len(user.get()) == 0:
        user.insert(END, 'username')


def username_focusin(event, user):
    user = user.get()
    if user == 'username':
        user.delete(0, END)


def password_focusout(event, password):
    if len(password.get()) == 0:
        password['show'] = ''
        password.insert(END, 'password')


def password_focusin(event, password):
    password = password.get()
    if password == 'password':
        password.delete(0, END)
        password['show'] = '*'


def logout(win):
    win.destroy()
    login_window()


def message_frame(event, message, win):
    msg = message.get("0.0", "end-1c")
    message.delete("0.0", "end-1c")
    if len(msg) == 0:
        messagebox.showinfo(title="Error", message="Please enter message")
    else:
        print_message(msg, win)
    return 'break'


def message_focusin(event, message):
    message.delete("0.0", "end-1c")


def print_message(msg, win):
    global row

    msg = Label(frame, text="YOU:     " + msg, fg='#f7941e', bg="white", font=('Calibri', 12, 'bold'))
    msg.grid(row=row, column=0, sticky='W')
    win.after(400, lambda: sleep(msg))
    row = row + 2


def sleep(msg):
    global row

    response = chatbot.get_response(msg)
    msg = Label(frame, text="ROBO:   " + str(response), fg='#00e2e2', bg="white", font=('Calibri', 12, 'bold'))
    msg.grid(row=row + 1, column=0, sticky='W')
    row = row + 2


def messenger_window(win, user, password, cb):
    u = user.get()
    p = password.get()
    m = cb.get()

    if u == 'user' and p == 'user' and m == 'Bored':
        win.destroy()
        # messenger window GUI
        global win1
        win1 = Tk()
        win1.configure(background="white")
        win1.title("MessageBOT")
        win1.wm_iconbitmap('icon.ico')
        win1.resizable(0, 0)

        x = 800
        y = 620
        w = win1.winfo_screenwidth()
        h = win1.winfo_screenheight()
        width = (w / 2) - (x / 2)
        height = (h / 2) - (y / 2)
        win1.geometry('%dx%d+%d+%d' % (x, y, width, height))

        # Menu bar
        menu_bar = Menu()
        menu_bar.add_cascade(label="Logout", command=lambda: logout(win1))
        win1.config(menu=menu_bar)

        # upper frame
        upper = Frame(win1, bg="yellow")
        upper.place(x=0, y=0, width=800, height=50)

        photo1 = PhotoImage(file='smiley.png')
        label1 = Label(upper, image=photo1, bg="yellow")
        label1.place(x=50, y=5)

        quote = Label(upper, text="\"Life will bring you pain all by itself. Your responsibility is to create joy\"",
                      fg='#f7941e', bg="yellow", font=('Calibri', 14, 'bold'))
        quote.place(x=100, y=10)

        photo2 = PhotoImage(file='smiley.png')
        label2 = Label(upper, image=photo2, bg="yellow")
        label2.place(x=685, y=5)

        # middle frame
        middle = Frame(win1, bg="white")
        middle.place(x=0, y=50, width=800, height=500)

        global canvas
        canvas = Canvas(middle, bg="white", width=800, height=500)
        global frame
        frame = Frame(canvas, bg="white", width=800, height=500)
        myscrollbar = Scrollbar(middle, orient="vertical", highlightbackground="#f05316", command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right", expand='true', fill='y')
        canvas.pack(side="left")
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", make_canvas)

        # lower frame
        lower = Frame(win1, bg="#f05316")
        lower.place(x=0, y=550, width=800, height=50)

        message_win = Text(lower, bg="#f05316", font=('Calibri', 14, 'bold'), fg="white", insertbackground="white")
        message_win.insert(END, "Enter message here")
        message_win.bind("<Return>", lambda event: message_frame(event, message_win, win1))
        message_win.bind("<FocusIn>", lambda event: message_focusin(event, message_win))
        message_win.place(x=0, y=0, width=800, height=50)
        win1.mainloop()

    else:
        messagebox.showinfo(title="Error", message="Something is missing OR wrong input")


def login_window():
    win = Tk()
    win.configure(background="white")
    win.title("MessageBOT")
    win.wm_iconbitmap('icon.ico')
    win.resizable(0, 0)

    x = 400
    y = 500
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    width = (w / 2) - (x / 2)
    height = (h / 2) - (y / 2)
    win.geometry('%dx%d+%d+%d' % (x, y, width, height))

    photo = PhotoImage(file='messenger.png')
    label = Label(win, image=photo, bg="white")
    label.pack()

    title = Label(win, text='MessageBOT', fg='#f05316', font=('Britannic Bold', 50), bg="white").pack()

    # username
    user1 = StringVar()
    pass1 = StringVar()
    mode1 = StringVar()

    user = Entry(win, cursor="arrow", bg="white", fg="#f05316", font=("Calibri", 15), relief=FLAT,
                 selectbackground="#f05316", selectborderwidth=4, selectforeground="white", width=40,
                 insertbackground="#f05316", textvariable=user1)
    user.insert(END, 'username')
    user.bind("<FocusOut>", lambda event: username_focusout(event, user))
    user.bind("<FocusIn>", lambda event: username_focusin(event, user))
    user.place(x=60, y=230)
    username = Label(win, text="________________________________________________________", fg="#f05316", bg="white")
    username.place(x=60, y=256)

    # password
    password = Entry(win, cursor="arrow", bg="white", fg="#f05316", font=("Calibri", 15), relief=FLAT,
                     selectbackground="#f05316", selectborderwidth=4, selectforeground="white", width=30,
                     insertbackground="#f05316", textvariable=pass1)
    password.insert(END, 'password')
    password.bind("<FocusOut>", lambda event: password_focusout(event, password))
    password.bind("<FocusIn>", lambda event: password_focusin(event, password))
    password.place(x=60, y=290)
    password_widget = Label(win, text="________________________________________________________", fg="#f05316", bg="white")
    password_widget.place(x=60, y=316)

    # drop down menu
    options = ['Sad', 'Happy', 'Bored']
    cb = ttk.Combobox(win, justify=CENTER, values=options, width=30, takefocus=FALSE, height=6, cursor="dot",
                      textvariable=mode1)
    cb.place(x=100, y=360)
    cb.set('Select your mode')
    style = ttk.Style()
    style.configure('Alarm.TCombobox', foreground='#f05316')
    cb.config(style='Alarm.TCombobox')

    # button
    enter = Button(win, text="Login", bg="#f05316", fg="White", font=("Calibri", 14, 'bold'), relief=RAISED, width=10,
                   activebackground="#f3723f", activeforeground="white",
                   command=lambda: messenger_window(win, user1, pass1, mode1))
    enter.place(x=145, y=420)

    win.mainloop()


if __name__ == '__main__':
    login_window()
