from tkinter import *

win = Tk()
win.geometry('324x340')
win.resizable(0, 0)
win.title("My First calculator")




#Frame is for Enter input data
input_frame = Frame(win, width=312, height=50, bd=10, highlightbackground="Black",highlightcolor="Black", highlightthickness=2)
input_frame.pack(side=TOP)

input_text = StringVar()


#Text fild inside Frame
input_fild = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, bg="#eee", bd=0, justify=RIGHT)
input_fild.pack()


#Btn Frame
btn_frame = Frame(win, width=312, height=324, bg="grey")
btn_frame.pack()


#Btns

#First row
Clear = Button(btn_frame, text="C", fg="black", width=34, height=3, cursor="hand1",command = lambda:btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
Divide = Button(btn_frame, text="/", fg="black", width=10, height=3, cursor="hand1",command = lambda:btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

#Second row
Seven = Button(btn_frame, text="7", width=10, height=3, cursor="hand1", command= lambda:btn_click("7")).grid(row=1, column = 0, padx=1, pady=1)
eight = Button(btn_frame, text="8", width=10, height=3, cursor="hand1", command= lambda:btn_click("8")).grid(row=1, column = 1, padx=1, pady=1)
nine = Button(btn_frame, text="9", width=10, height=3, cursor="hand1", command= lambda:btn_click("9")).grid(row=1, column = 2, padx=1, pady=1)
plus = Button(btn_frame, text="+", width=10, height=3, cursor="hand1", command= lambda:btn_click("+")).grid(row=1, column = 3, padx=1, pady=1)


#theird row

foure = Button(btn_frame, text="4", width=10, height=3, cursor="hand1", command= lambda:btn_click("4")).grid(row=2, column = 0, padx=1, pady=1)
five = Button(btn_frame, text="5", width=10, height=3, cursor="hand1", command= lambda:btn_click("5")).grid(row=2, column = 1, padx=1, pady=1)
six = Button(btn_frame, text="6", width=10, height=3, cursor="hand1", command= lambda:btn_click("6")).grid(row=2, column = 2, padx=1, pady=1)
minus = Button(btn_frame, text="-", width=10, height=3, cursor="hand1", command= lambda:btn_click("-")).grid(row=2, column = 3, padx=1, pady=1)

#fourth row
multiply = Button(btn_frame, text="*", width=10, height=3, cursor="hand1", command= lambda:btn_click("-")).grid(row=3, column = 3, padx=1, pady=1)
one = Button(btn_frame, text="1", width=10, height=3, cursor="hand1", command= lambda:btn_click("4")).grid(row=3, column = 0, padx=1, pady=1)
two = Button(btn_frame, text="2", width=10, height=3, cursor="hand1", command= lambda:btn_click("5")).grid(row=3, column = 1, padx=1, pady=1)
three = Button(btn_frame, text="3", width=10, height=3, cursor="hand1", command= lambda:btn_click("6")).grid(row=3, column = 2, padx=1, pady=1)

#fifith row
one = Button(btn_frame, text="0", width=22, height=3, cursor="hand1", command= lambda:btn_click("0")).grid(row=4, column = 0, columnspan=2 ,padx=1, pady=1)
two = Button(btn_frame, text=".", width=10, height=3, cursor="hand1", command= lambda:btn_click(".")).grid(row=4, column = 2, padx=1, pady=1)
three = Button(btn_frame, text="=", width=10, height=3, cursor="hand1", command= lambda:btn_ans()).grid(row=4, column = 3, padx=1, pady=1)


#function

def btn_click(item):
    global expresssion
    expresssion = expresssion + str(item)
    input_text.set(expresssion)

def btn_clear():
    global expresssion
    expresssion = ""
    input_text.set(expresssion)

def btn_ans():
    global expresssion
    result = str(eval(expresssion))
    input_text.set(result)

expresssion = ""


win.mainloop()
