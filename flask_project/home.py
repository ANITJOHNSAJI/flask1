from flask import Flask, render_template,request,redirect
# import sqlite3
import mysql.connector

App=Flask(__name__)
# con=sqlite3.connect('database.db')
# con.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,age INTEGER)")

con=mysql.connector.connect(
    host='localhost',
    user='anit',
    password='anit',
    database='anit'
)
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,age INTEGER)")



@App.route('/',methods=['GET','POST'])
# def index():
#     # return "hello world"
#     # return render_template('index.html')
#     if request.method == 'POST':
#         name=request.form.get('name')
#         age=request.form.get('age')
#         print(name,age)
#         print(request.form)
#         con=sqlite3.connect('database.db')
#         con.execute("INSERT INTO users(name,age) VALUES(?,?)",(name,age))
#         con.commit()
#         con.close()
#         return redirect('/')
#     return render_template('index.html')

def index():
    if request.method == 'POST':
        name=request.form.get('name')
        age=request.form.get('age')
        print(name,age)
        cur=con.cursor()
        cur.execute("INSERT INTO users(name,age) VALUES(%s,%s)",(name,age))
        con.commit()
        return redirect('/')
    return render_template('index.html')

App.run()