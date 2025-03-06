import sqlite3
class def_:
    def __init__ (self,db):
        self.con=sqlite3.connect('d:/hossien/my  H O O M/hoom/data.db')
        self.cur=self.con.cursor()
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS  home 
                        (id INTEGER PRIMARY KEY,fname text, lname text,phone text,address text)
                        ''')
        self.con.commit()

    def insert_(self,fname,lname,phone,address):
        self.cur.execute('INSERT INTO home (fname , lname , phone , address) VALUES (?,?,?,?)',(fname,lname,phone,address))
        self.con.commit()
 
    def show_(self):
        self.cur.execute('SELECT * FROM home ')
        return self.cur.fetchall()

    def delet_(self,id,fname,lname,phone,address):
        self.cur.execute('DELETE FROM home WHERE id=? or fname=? or lname=? or phone=? or address=?',(id,fname,lname,phone,address))
        self.con.commit()

    def update_(self,id,fname,lname,phone,address):
        self.cur.execute('UPDATE home SET fname=? , lname=? , phone=? , address=? WHERE id=?',(fname,lname,phone,address,id))
        self.con.commit()
    
    




