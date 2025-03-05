import sqlite3
class def_:
    def __init__ (self,db):
        self.con=sqlite3.connect('d:/hossien/my  H O O M/hoom/data.db')
        self.cur=self.con.cursor()
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS  home 
                        (id INTEGER primary key,fname text, lname text,score text)
                        ''')
        self.con.commit()

    def insert_(self,fname,lname,score):
        self.cur.execute('INSERT INTO home (fname , lname , score) VALUES (?,?,?)',(fname,lname,score))
        self.con.commit()

    def show_(self):
        self.cur.execute('SELECT * FROM home ')
        return self.cur.fetchall()

    def delet_(self,id,fname,lname,score):
        self.cur.execute('DELETE * FROM home WHERE id=? or fname=? or lname=? or score=?',(id,fname,lname,score))
        self.con.commit()

    def update_(self,id,fname,lname,score):
        self.cur.execute('UPDATE home SET fname=? , lname=? , score=? WHERE id=?',(fname,lname,score,id))
        self.con.commit()
    
    




