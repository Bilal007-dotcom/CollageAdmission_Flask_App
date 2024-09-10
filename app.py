from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",  # Replace with your MySQL username
        password="root",  # Replace with your MySQL password
        database="CollegeAdmission"
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        course = request.form['course']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO admission_form (name, dob, gender, email, phone, address, course) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, dob, gender, email, phone, address, course)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

