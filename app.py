from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__) #Initialize Flask app

DATABASE = 'expenses.db' #Define SQLite database file

def get_db(): 
    conn = sqlite3.connect(DATABASE) #Connect to SQLite database and return connection obj
    return conn

@app.route('/')
def index(): 
    '''
    Render the main page showing all expenses.
    '''
    conn = get_db() #Connect to the database
    cursor = conn.cursor() #Create cursor obj
    cursor.execute("SELECT * FROM expenses") #Execute query to retrieve all expenses
    expenses = cursor.fetchall() #Fetch all rows from result
    conn.close() #Close database connection
    return render_template('index.html', expenses=expenses) #Render the template with expenses data

@app.route('/add_expenses', methods=['POST'])
def add_expenses(): 
    '''
    Add a new expense to the database.
    '''
    amount = request.form['amount'] #Get the amount from the form
    category = request.form['category'] 
    description = request.form['description']

    conn = get_db() #Connect to db
    cursor = conn.cursor() #Create cursor obj

    #Insert new expense into database
    cursor.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)", (amount, category, description))
    conn.commit() #Commit transaction
    conn.close() #Close database connection
    return redirect(url_for('index')) #Redirect to main page

@app.route('/delete/<int:id>')
def delete_expense(id):
    '''
    Delete an expense from the database by its ID.   
    '''
    conn = get_db() #Connect to db
    cursor = conn.cursor() #Create cursor obj
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,)) #Delete the expense with specified ID
    conn.commit() #Commit the transaction
    conn.close() #Close the database connection
    return redirect(url_for('index')) #Redirect to the main page

@app.route('/summary')
def summary():
    '''
    Render a summary of expenses grouped by category.
    '''
    conn = get_db() #Connect to the database
    cursor = conn.cursor() #Create a cursor object
    #Query to group expenses by category and sum their amounts
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    summary_data = cursor.fetchall() #Fetch all rows from result
    conn.close() #Close db connection
    return render_template('summary.html', summary_data = summary_data) #Render the template with summary data

if __name__ == '__main__':
    conn = get_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object
    # Create the expenses table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL,
                        category TEXT,
                        description TEXT
                    )''')
    conn.commit()  # Commit the transaction
    conn.close()  # Close the database connection
    app.run(debug=True)  # Run the Flask application in debug mode