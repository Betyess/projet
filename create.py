import sqlite3

conn = sqlite3.connect('hopital.db')
cur = conn.cursor()
req = "create table patient(code int,nom text,prenom text,age text,adresse text,telephone text,remarque text)"
cur.execute(req)
conn.commit()
conn.close()