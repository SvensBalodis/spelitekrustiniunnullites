from tkinter import *
from tkinter import messagebox
mansLogs=Tk()
mansLogs.title("TicTacToe")

speletajsX=True
count=0

def btnClick(button):
    global speletajsX,count
    if button ["text"]==""and speletajsX==True:
        button["text"]="x"
        speletajsX=False
        count+=1
        checkWinner()
    elif button["text"]==""and speletajsX==False:
        button["text"]="0"
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")

def disableButtons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''
    
def checkWinner():
    global winner
    winner=False
    if(btn1["text"]=="x" and btn2["text"]=="x" and btn3["text"]=="x"or
       btn4["text"]=="x" and btn5["text"]=="x" and btn6["text"]=="x" or
       btn7["text"]=="x" and btn8["text"]=="x" and btn9 ["text"]=="x" or
       btn1["text"]=="x" and btn4["text"]=="x" and btn7 ["text"]=="x" or
       btn2["text"]=="x" and btn5["text"]=="x" and btn8 ["text"]=="x" or
       btn3["text"]=="x" and btn6["text"]=="x" and btn9 ["text"]=="x" or
       btn1["text"]=="x" and btn5["text"]=="x" and btn9 ["text"]=="x" or
       btn3["text"]=="x" and btn5["text"]=="x" and btn7 ["text"]=="x"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētājs X uzvarēja")

    elif(btn1["text"]=="0" and btn2["text"]=="0" and btn3["text"]=="0"or
       btn4["text"]=="0" and btn5["text"]=="0" and btn6["text"]=="0" or
       btn7["text"]=="0" and btn8["text"]=="0" and btn9 ["text"]=="0" or
       btn1["text"]=="0" and btn4["text"]=="0" and btn7 ["text"]=="0" or
       btn2["text"]=="0" and btn5["text"]=="0" and btn8 ["text"]=="0" or
       btn3["text"]=="0" and btn6["text"]=="0" and btn9 ["text"]=="0" or
       btn1["text"]=="0" and btn5["text"]=="0" and btn9 ["text"]=="0" or
       btn3["text"]=="0" and btn5["text"]=="0" and btn7 ["text"]=="0"):
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētājs 0 uzvarēja")
    elif count==9 and winner==False:
        winner=False
        disableButtons()
        messagebox.showinfo("TicTacToe","Neizšķirts")
    return

btn1=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn9))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

galvenaIzvelne=Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)
opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)
opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

mansLogs.mainloop()