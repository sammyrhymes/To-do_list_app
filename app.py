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

# ADDing new tasks
@app.route('/add', methods=['POST'])
def add_task():

    # store value gotten from form in a varibale
    task = request.form.get('task')

    # establish a conncetion to the database
    con = sqlite3.connect('todo.db')

    # create a cursor
    cur = con.cursor()

    # execute insert query
    cur.execute('INSERT into TODOS (task, completed) VAlUES (?,?)', (task, 0))

    # commit the changes
    con.commit()

    # close conncetion
    con.close()

    #redirect
    return redirect(url_for('index'))

# UPDATE existing tasks
@app.route('/update/<int:todo_id>', methods=['POST'])
def update_task(todo_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT completed FROM todos WHERE id = ?', (todo_id,))
    result = cursor.fetchone()
    if result:
        completed = 0 if result[0] else 1
        cursor.execute('UPDATE todos SET completed = ? WHERE id = ?', (completed, todo_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))



# only start development server if runnnig this file directly
if __name__ == '__main__':
    app.run(debug=True)