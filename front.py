from tkinter import *
from tkinter import messagebox
import database
win=Tk()
win.geometry('450x600+250+50')
win.title('hoom')
win.config(bg='indigo')

db=database.def_('data.db')
################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def insert(): 
    fname=ent_fname.get()
    lname=ent_lname.get()
    phone=ent_phone.get()
    address=ent_address.get()
    db.insert_(fname,lname,phone,address)
    show__()
    clear_()

def clear_():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_phone.delete(0,END)
    ent_address.delete(0,END)

def exit_():
    ask=messagebox.askquestion("exit",'do you want to go?')
    if  ask == 'yes':
        win.destroy()

def show__():
    lst_.delete(0,END)
    y=db.show_()
    lst_.insert(END,y)

def get(event):
    global x

    index=lst_.curselection()
    if index:
        record=lst_.get(index)
        x=(str(record).split(" "))
        clear_()
        ent_fname.insert(0,x[1])
        ent_lname.insert(0,x[2])
        ent_phone.insert(0,x[3])
        ent_address.insert(0,x[4])


def update__():


    fname=ent_fname.get()
    lname=ent_lname.get()
    phone=ent_phone.get()
    address=ent_address.get()

    id=x[0]


    db.update_(id,fname,lname,phone,address)

def delete__():
    fname=ent_fname.get()
    lname=ent_lname.get()
    phone=ent_phone.get()
    address=ent_address.get()
    db.delet_(fname,lname,phone,address)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lbl_fname=Label(win,text='fname =',font='raleway 18')
lbl_fname.place(x='20',y='20')

ent_fname=Entry(win,font='raleway 18')
ent_fname.place(x='120',y='20')

lbl_lname=Label(win,text='lname =',font='raleway 18')
lbl_lname.place(x='20',y='70')

ent_lname=Entry(win,font='raleway 18')
ent_lname.place(x='120',y='70')

lbl_phone=Label(win,text='score =',font='raleway 18')
lbl_phone.place(x='20',y='120')

ent_phone=Entry(win,font='raleway 18')
ent_phone.place(x='120',y='120')

lbl_address=Label(win,text='adrees=',font='raleway 18')
lbl_address.place(x='20',y='170')

ent_address=Entry(win,font='raleway 18')
ent_address.place(x='120',y='170')
#################################################################
lst_=Listbox(win,font='raleway 18')
lst_.place(x='120',y='300')
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





















lst_.bind('<Enter>',get)


win.mainloop()