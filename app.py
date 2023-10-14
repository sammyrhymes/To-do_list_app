# make necessary imports
from flask import Flask, render_template, request, redirect, url_for, request
import sqlite3

# create a flask instance
app = Flask(__name__)

# HOME
@app.route('/', methods = ['POST', 'GET'])
def index():

    """ fetch the todos from the db """
    if request.method == 'GET':
    # start by creating  a connection
        conn =sqlite3.connect('todo.db')

        # proceed to create a cursor
        cur = conn.cursor()

        # use cursor to execute sql queries
        cur.execute('select * from todos order by id desc')

        # specify how many to fetch i.e all or one
        todos = cur.fetchall()

        # commit changes
        conn.commit()
        # close the connection
        conn.close()
        return render_template('index.html', todos=todos)
    else:
        # start by creating  a connection
        conn =sqlite3.connect('todo.db')

        # proceed to create a cursor
        cur = conn.cursor()

        cur.execute("INSERT INTO TODOS(TASK) VALUES(?)", (request.form['task'],))

        conn.commit()

        conn.close()
        
        return redirect(url_for('index'))

@app.route("/update/<int:id>", methods = ['GET', 'POST'])
def update(id):
    pass

# only start development server if runnnig this file directly
if __name__ == '__main__':
    app.run(debug=True)