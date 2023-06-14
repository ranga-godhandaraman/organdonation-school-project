from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ranga@123',
    'database': 'organdonner',
    'auth_plugin': 'mysql_native_password'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        print(request.form.get('firstName'))
        firstName:str=''.join(request.form.get('firstName'))
        lastName:str=''.join(request.form.get('lastName'))
        dateOfBirth:str=''.join(request.form.get('dateOfBirth'))
        bloodGroup:str=''.join(request.form.get('bloodGroup'))
        organ:str=''.join(request.form.get('organ'))
        addressline1:str=''.join(request.form.get('addressline1'))
        addressline2:str=''.join(request.form.get('addressline2'))
        state:str=''.join(request.form.get('state'))
        phone:str=''.join(request.form.get('phone'))
        # Retrieve other form fields for organ donation

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute the SQL insert statement
        sql = "INSERT INTO donations (firstName, lastName,dateOfBirth,bloodGroup,organ,addressline1,addressline2,state,phone) "
        sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (firstName, lastName, dateOfBirth, bloodGroup, organ, addressline1, addressline2, state, phone)
        cursor.execute(sql, values)
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return render_template('donate.html', success=True)
    else:
        return render_template('donate.html', success=False)


def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print("Error connecting to MySQL database:", e)
        return None
        
@app.route('/request', methods=['GET', 'POST'])
def request_organ():
    if request.method == 'POST':
        print(request.form.get('firstName'))
        firstName:str=''.join(request.form.get('firstName'))
        lastName:str=''.join(request.form.get('lastName'))
        dateOfBirth:str=''.join(request.form.get('dateOfBirth'))
        bloodGroup:str=''.join(request.form.get('bloodGroup'))
        organ:str=''.join(request.form.get('organ'))
        addressline1:str=''.join(request.form.get('addressline1'))
        addressline2:str=''.join(request.form.get('addressline2'))
        state:str=''.join(request.form.get('state'))
        phone:str=''.join(request.form.get('phone'))
        # Retrieve other form fields for organ donation

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute the SQL insert statement
        sql = "INSERT INTO requests (firstName, lastName,dateOfBirth,bloodGroup,organ,addressline1,addressline2,state,phone) "
        sql += " VALUES ('"+firstName+"', '"+lastName+"','"+dateOfBirth+"','"+bloodGroup+"','"+organ+"','"+addressline1+"','"+addressline2+"','"+state+"','"+phone+"')"
        print(sql)
        cursor.execute(sql)
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return render_template('request.html', success=True)
    else:
        # Connect to the database
        conn = connect_to_database()
        if conn is None:
            return render_template('request.html', success=False)

        try:
            cursor = conn.cursor()

            # Execute the SQL select statement
            sql = "SELECT * FROM donations"
            cursor.execute(sql)
            donners = cursor.fetchall()

            # Close the database connection
            cursor.close()
            conn.close()

            return render_template('request.html', success=False, donners=donners)
        except Error as e:
            print("Error executing SQL statement:", e)
            return render_template('request.html', success=False)
if __name__ == '__main__':
    app.run(debug=True, port=8000)

