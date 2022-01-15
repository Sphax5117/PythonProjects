from tkinter import *
#add fonctions



# create
window = Tk()
# personalise

window.title("Calculator")
window.geometry("300x400")
window.minsize(300, 400)
window.maxsize(300, 400)

# add a frame

frame_1 = Frame(window)

# add a button

butt_1 = Button(window, text="1", bg="#c8bebc", width=4)
butt_2 = Button(window, text="2", bg="#c8bebc", width=4)
butt_3 = Button(window, text="3", bg="#c8bebc", width=4)
butt_4 = Button(window, text="4", bg="#c8bebc", width=4)
butt_5 = Button(window, text="5", bg="#c8bebc", width=4)
butt_6 = Button(window, text="6", bg="#c8bebc", width=4)
butt_7 = Button(window, text="7", bg="#c8bebc", width=4)
butt_8 = Button(window, text="8", bg="#c8bebc", width=4)
butt_9 = Button(window, text="9", bg="#c8bebc", width=4)
butt_0 = Button(window, text="0", bg="#c8bebc", width=4)
butt_equal = Button(window, text="=", bg="#c8bebc", width=4)
butt_plus = Button(window, text="+", bg="#c8bebc", width=4)
butt_minus = Button(window, text="-", bg="#c8bebc", width=4)
butt_divide = Button(window, text="/", bg="#c8bebc", width=4)
butt_multiply = Button(window, text="*", bg="#c8bebc", width=4)
input_frame = Frame(window, width=300, height=65, bd=0, bg="#c8bebc")
input_frame.pack()
input_frame.place(x=0, y=50)

butt_1.pack()
butt_2.pack()
butt_3.pack()
butt_4.pack()
butt_5.pack()
butt_6.pack()
butt_7.pack()
butt_8.pack()
butt_9.pack()
butt_0.pack()
butt_equal.pack()
butt_multiply.pack()
butt_divide.pack()
butt_plus.pack()
butt_minus.pack()
butt_1.place(x=40, y=300)
butt_2.place(x=120, y=300)
butt_3.place(x=200, y=300)
butt_4.place(x=40, y=250)
butt_5.place(x=120, y=250)
butt_6.place(x=200, y=250)
butt_7.place(x=40, y=200)
butt_8.place(x=120, y=200)
butt_9.place(x=200, y=200)
butt_0.place(x=120, y=350)
butt_equal.place(x=200, y=350)
butt_minus.place(x=200, y=150)
butt_plus.place(x=120, y=150)
butt_divide.place(x=40, y=350)
butt_multiply.place(x=40, y=150)

#window.iconbitmap("logo.ico") test on windows

# show
window.mainloop()