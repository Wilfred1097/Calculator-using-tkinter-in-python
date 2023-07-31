from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x395+700+200")
root.resizable(False, False)
root.configure(bg='#1C1C1C')

screen = StringVar()
hist = StringVar()
expression = ""

def bttn(x,y,text,bcolor,fcolor, cmd):

	def on_enter(e):
		mybutton['background'] = bcolor
		mybutton['foreground'] = fcolor
		mybutton['font'] = ("Helvetica 15 italic")

	def on_leave(e):
		mybutton['background'] = fcolor
		mybutton['foreground'] = bcolor
		mybutton['font'] = ("Helvetica 16")

	mybutton = Button(root, width=7, height=2, text=text,
		fg=bcolor,
		bg=fcolor,
		border=0,
		activeforeground=fcolor,
		activebackground=bcolor,
		font=("Helvetica 16"),
		command=cmd,)

	mybutton.bind("<Enter>", on_enter)
	mybutton.bind("<Leave>", on_leave)

	mybutton.place(x=x,y=y)

# e1 = Entry(root, textvariable=hist,font='helvetica 25', bg='#1C1C1C', fg='white', bd=0, width=18, state='normal', justify= RIGHT)
# e1.place(x=9,y=9)
e2 = Entry(root, textvariable=screen,font='helvetica 47', bg='#1C1C1C', fg='white', bd=0, width=10, state='normal', justify= RIGHT)
e2.place(x=4,y=10)

def press(num):
	global expression
	expression = expression + str(num)
	screen.set(expression)

def clear():
	global expression
	expression = ""
	e2.delete(0, 'end')

def calculate():
	global expression
	try:
		total = e2.get()
		e2.delete(0, 'end')
		e2.insert(0, eval(total))
		expression = ""
	except:
		e2.insert(0, "Error")
		expression = ""
def delete():
	global expression
	expression = expression[:-1]
	e2.delete(0, 'end')
	e2.insert(0, expression)

bttn(0,86,"CE", "#ffcc66", "#141414", clear)
bttn(90,86,"C", "#ffcc66", "#141414", clear)
bttn(180,86,"DEL", "#ffcc66", "#141414", delete)
bttn(270,86,"/", "magenta", "#141414", lambda: press("/"))
bttn(0,148,"7", "cyan", "#141414", lambda: press(7))
bttn(90,148,"8", "cyan", "#141414", lambda: press(8))
bttn(180,148,"9", "cyan", "#141414", lambda: press(9))
bttn(270,148,"*", "magenta", "#141414", lambda: press("*"))
bttn(0,210,"4", "cyan", "#141414", lambda: press(4))
bttn(90,210,"5", "cyan", "#141414", lambda: press(5))
bttn(180,210,"6", "cyan", "#141414", lambda: press(6))
bttn(270,210,"-", "magenta", "#141414", lambda: press("-"))
bttn(0,272,"1", "cyan", "#141414", lambda: press(1))
bttn(90,272,"2", "cyan", "#141414", lambda: press(2))
bttn(180,272,"3", "cyan", "#141414", lambda: press(3))
bttn(270,272,"+", "magenta", "#141414", lambda: press("+"))
bttn(0,334,"+/-", "#11ff2D", "#141414", lambda: press("-"))
bttn(90,334,"0", "cyan", "#141414", lambda: press(0))
bttn(180,334,".", "#11ff2D", "#141414", lambda: press("."))
bttn(270,334,"=", "grey", "#141414", calculate)


mainloop()
