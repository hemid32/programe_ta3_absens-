# -*- coding : utf-8 -*-
import sys
from PyQt4.QtGui import *
import sqlite3
a = 'hemidi benameur'
b = 'hakmi mohamed'
c = 'hocine benziadi'
d = 'kjfvnjlkfvn '

liste = [a,b,c,d]


file = ("C:\Users\hemidi benameur\Desktop\project_\data.db")
conn = sqlite3.connect(file)
cur = conn.cursor()

cur.execute("SELECT * FROM etidient ")
l  = cur.fetchall()
for i in l  :
    print i[0]
