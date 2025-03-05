import sqlite3
class def_:
    def __init__ (self):
        self.con=sqlite3.connect('d:/hossien/my  H O O M/hoom/data.db')
        self.cur=self.con.cursor()
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS  home 
                        (id primary key,fname text, lname text,score text)
                        ''')
        self.con.commit()

    def insert_(self,fname,lname,score):
        self.cur.execute('INSERT INTO home  VALUES (?,?,?)',(fname,lname,score))
        self.con.commit()
#(fname , lname , score)
    def show_(self):
        self.cur.execute('SELECT * FROM home ')
        return self.cur.fetchall()

    def delet_(self,id,fname,lname,score):
        self.cur.execute('DELET * FROM home WHER id=? or fname=? or lname=? or score=?',(id,fname,lname,score))
        self.con.commit()

    def update_(self,id,fname,lname,score):
        self.cur.execute('UPDATE home SET fname=? and lname=? and score=? WHERE id=?',(fname,lname,score,id))
        self.con.commit()
    
    




