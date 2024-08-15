Expense Tracker
A simple web application to track and manage personal expenses using Flask and SQLite. This project allows users to add, view, and delete expenses, providing a straightforward interface for financial management.

Features
Add Expenses: Easily input and categorize your expenses.
View Expenses: Display a list of all recorded expenses.
Delete Expenses: Remove entries from the expense list.

Technologies Used
Flask: A lightweight WSGI web application framework in Python.
SQLite: A self-contained, serverless SQL database engine.
HTML/CSS: For structuring and styling the web pages.

Demo


Setup and Installation
1)Clone the Repository:
  Copy code: git clone https://github.com/nikammrohit/expense-tracker.git
  
2) Navigate to the Project Directory:
  cd expense-tracker

4) Create a Virtual Environment:
  Copy code: python -m venv venv

6) Activate the Virtual Environment:
  On Windows:
      Copy code: .\venv\Scripts\activate
  On macOS/Linux:
      Copy code: source venv/bin/activate
   
7) Install Dependencies:
   Copy code: pip install -r requirements.txt
   
8) Set Up the Database:
Run the following Python script to create the database and initial table:
  Copy code: python setup_db.py
Run the Flask Application:
  Copy code: python app.py
Access the Application:
  Open your web browser and navigate to http://127.0.0.1:5000/ to start using the Expense Tracker.

Project Structure
app.py: The main Flask application script.
setup_db.py: A script to initialize the SQLite database.
templates/: Directory containing HTML templates.
static/css/: Directory containing CSS stylesheets.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.


