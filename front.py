from tkinter import *
from tkinter import messagebox
import sqlite3
import database
win=Tk()
win.geometry('450x600+250+50')
win.title('hoom')
win.config(bg='indigo')

################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def insert(): 
    fname=ent_fname.get()
    lname=ent_lname.get()
    score=ent_score.get()
    database.def_.insert_(fname,lname,score)
    show__()
    clear_()

def clear_():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_score.delete(0,END)

def exit_():
    ask=messagebox.askquestion("exit",'do you want to go?')
    if  ask == 'yes':
        win.destroy()

def show__():
    database.def_.show_()

def get():
    global x
    ent_fname.insert(0,x[1])
    ent_lname.insert(0,x[2])
    ent_score.insert(0,x[3])

    index=lst_.curselection()

    record=lst_.get(index)

    x=(str(record).split(" "))    

def update__():


    fname=ent_fname.get()
    lname=ent_lname.get()
    score=ent_score.get()

    id=x[0]


    database.def_.update_(id,fname,lname,score)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
win.bind('<w>',get(Event))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lbl_fname=Label(win,text='fname =',font='raleway 18')
lbl_fname.place(x='20',y='30')

ent_fname=Entry(win,font='raleway 18')
ent_fname.place(x='120',y='30')

lbl_lname=Label(win,text='lname =',font='raleway 18')
lbl_lname.place(x='20',y='130')

ent_lname=Entry(win,font='raleway 18')
ent_lname.place(x='120',y='130')

lbl_score=Label(win,text='score =',font='raleway 18')
lbl_score.place(x='20',y='230')

ent_score=Entry(win,font='raleway 18')
ent_score.place(x='120',y='230')
#################################################################
lst_=Listbox(win,font='raleway 18')
lst_.place(x='120',y='280')
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
btn_insert=Button(win,text='insert',font='raleway 18',bg='#0000ff',command=insert)
btn_insert.place(x='20',y='280',width='95',height='50')


btn_show=Button(win,text='show',font='raleway 18',bg='#ff0000',command=show__)
btn_show.place(x='20',y='330',width='95',height='50')


btn_delete=Button(win,text='delete',font='raleway 18',bg='orange')
btn_delete.place(x='20',y='380',width='95',height='50')

btn_update=Button(win,text='update',font='raleway 18',bg='#ffff00')
btn_update.place(x='20',y='430',width='95',height='50')


btn_clear=Button(win,text='clear',font='raleway 18',bg='#00ff00',command= clear_)
btn_clear.place(x='20',y='480',width='95',height='50')


btn_exit=Button(win,text='exit',font='raleway 18',bg='#00ffff',command=exit_)
btn_exit.place(x='20',y='530',width='95',height='50')
























win.mainloop()