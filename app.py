# make necessary imports
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# create a flask instance
app = Flask(__name__)

# HOME
@app.route('/')

# define what happens in the home page
def index():

    """ fetch the todos from the db """
    
    # start by creating  a connection
    conn =sqlite3.connect('todo.db')

    # proceed to create a cursor
    cur = conn.cursor()

    # use cursor to execute sql queries
    cur.execute('select * from todos')

    # specify how many to fetch i.e all or one
    todos = cur.fetchall()

    # close the connection
    conn.close()

    # render template with retreived data
    return render_template('index.html', todos=todos)

# only start development server if runnnig this file directly
if __name__ == '__main__':
    app.run(debug=True)