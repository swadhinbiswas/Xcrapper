import sqlite3


class User:
  def __init__(self):
    self.db=sqlite3.connect("userinfo.db")
    self.cursor=self.db.cursor()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
    
    
  def set_user(self,username:str,password:str):
    self.cursor.execute("INSERT INTO users VALUES(?,?)",(username,password))
    self.db.commit()
   
    
  def get_user(self)->str:
    self.cursor.execute("SELECT * FROM users")
    user=self.cursor.fetchall()

    return user
    
  def delete_user(self):
    self.cursor.execute("DELETE FROM users")
    self.db.commit()

    
  def check_user(self)->bool:
    self.cursor.execute("SELECT * FROM users")
    user=self.cursor.fetchall()
  
    if user==[]:
      return False
    else:
      return True
    
  def get_username(self)->str:
    self.cursor.execute("SELECT username FROM users")
    username=self.cursor.fetchall()
   
    return username
    
  def get_password(self)->str:
    self.cursor.execute("SELECT password FROM users")
    password=self.cursor.fetchall()
    return password
  
  def closedb(self):
    self.db.close()

