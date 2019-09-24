from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title("Tic Tac Toe")

flag_turn = True 
p1 = StringVar()
p2 = StringVar()

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED) 

def btnClicked(button):
    global flag_turn

    if button["text"] == " " and flag_turn == True:
        button["text"] = "X"
        flag_turn = False
        checkForWinner()
    elif button["text"] == " " and flag_turn == False:
        button["text"] = "O" 
        flag_turn = True 
        checkForWinner()
    else:
       messagebox.showinfo("Error", "This button already clicked")

def checkForWinner():
    if (button1["text"]==button2["text"] and button2["text"]==button3["text"]=="X" or
       button4["text"]==button5["text"] and button5["text"]==button6["text"]=="X" or
       button7["text"]==button8["text"] and button8["text"]==button9["text"]=="X" or 
       button1["text"]==button4["text"] and button4["text"]==button7["text"]=="X" or 
       button2["text"]==button5["text"] and button5["text"]==button8["text"]=="X" or
       button3["text"]==button6["text"] and button6["text"]==button9["text"]=="X" or
       button2["text"]==button5["text"] and button5["text"]==button8["text"]=="X" or
       button1["text"]==button5["text"] and button5["text"]==button9["text"]=="X" or
       button3["text"]==button5["text"] and button5["text"]==button7["text"]=="X"):
            disableButton()
            messagebox.showinfo("Game Over",  p1.get()+" Win!")

    if (button1["text"]==button2["text"] and button2["text"]==button3["text"]=="O" or
    button4["text"]==button5["text"] and button5["text"]==button6["text"]=="O" or
    button7["text"]==button8["text"] and button8["text"]==button9["text"]=="O" or 
    button1["text"]==button4["text"] and button4["text"]==button7["text"]=="O" or 
    button2["text"]==button5["text"] and button5["text"]==button8["text"]=="O" or
    button3["text"]==button6["text"] and button6["text"]==button9["text"]=="O" or
    button2["text"]==button5["text"] and button5["text"]==button8["text"]=="O" or
    button1["text"]==button5["text"] and button5["text"]==button9["text"]=="O" or
    button3["text"]==button5["text"] and button5["text"]==button7["text"]=="O"):
        disableButton()
        messagebox.showinfo("Game Over", p2.get()+" Win!")





player1_name = Entry(tk, textvariable=p1, bd=5)

player2_name = Entry(tk, textvariable=p2, bd=5)


label = Label( tk, text="Player 1:", font='Times 20 bold', bg='purple', fg='black', height=1, width=8)
label.grid(row=1, column=0)
player1_name.grid(row=1, column=1, columnspan=8)

label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)
player2_name.grid(row=2, column=1, columnspan=8)


button1 = Button(tk, text=" ", font='Times 20 bold', bg='purple', fg='black', height=4, width=8, command=lambda: btnClicked(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black', height=4, width=8, command=lambda: btnClicked(button2))
button2.grid(row=3, column=1)

button3 = Button(tk,text =" ",font = "Times 20 bold",bg ='purple',fg = 'black',height = 4, width=8,command=lambda: btnClicked(button3))
button3.grid(row=3,column=2)

button4 = Button(tk,text=" ",font = "Times 20 bold",bg = "gray",fg="black",height= 4,width=8,command=lambda: btnClicked(button4))
button4.grid(row=4,column=0)

button5 = Button(tk,text=" ",font="Times 20 bold",bg="purple",fg="black",height=4,width=8,command=lambda:btnClicked(button5))
button5.grid(row=4,column=1)

button6 = Button(tk,text=" ",font="Times 20 bold",bg="gray",fg="black",height=4,width=8,command=lambda:btnClicked(button6))
button6.grid(row=4,column=2)

button7 = Button(tk,text=" ",font="Times 20 bold",bg="purple",fg="black",height=4,width=8,command=lambda:btnClicked(button7))
button7.grid(row=5,column=0)

button8 = Button(tk,text=" ",font="Times 20 bold",bg="gray",fg="black",height=4,width=8,command=lambda:btnClicked(button8))
button8.grid(row=5,column=1)

button9 = Button(tk,text=" ",font="Times 20 bold",bg="purple",fg="black",height=4,width=8,command=lambda:btnClicked(button9))
button9.grid(row=5,column=2)

tk.mainloop()