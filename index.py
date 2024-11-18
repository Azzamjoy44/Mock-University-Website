from flask import Flask, render_template, url_for, request, redirect
import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="user2003", password="4321", database="studentdb")

app = Flask(__name__)

mycursor = mydb.cursor()

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/displayTable")
def displayTable():
  mycursor.execute("SELECT * FROM student")
  myResult = mycursor.fetchall()
  return render_template('displayTable.html', my_list = myResult)

@app.route("/electrical")
def electrical():
  return render_template('electrical.html')

@app.route("/chemical")
def chemical():
  return render_template('chemical.html')

@app.route("/power")
def power():
  return render_template('power.html')

@app.route("/medical")
def medical():
  return render_template('medical.html')

@app.route("/aerospace")
def aerospace():
  return render_template('aerospace.html')

@app.route("/form", methods =  ['GET', 'POST'])
def form():
  if request.method == 'POST':
    userDetails = request.form
    first_name = userDetails['first_name']
    last_name = userDetails['last_name']
    age = userDetails['age']
    gender = userDetails['gender']
    email = userDetails['email']
    faculty = userDetails['faculty']
    mycursor.execute("INSERT INTO student (first_name, last_name, age, gender, email, faculty) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, last_name, age, gender, email, faculty))
    mydb.commit()
    return 'The form has been submitted successfully'
  return render_template('form.html')

@app.route("/delete/<id>", methods = ['GET'])
def delete(id):
  if request.method == 'GET':
    sql = "DELETE FROM student WHERE id = %s"
    mycursor.execute(sql, (id, ))
    mydb.commit()
  return redirect(url_for('displayTable'))

@app.route("/edit/<id>")
def edit(id):
  sql = "SELECT * from student WHERE id = %s"
  mycursor.execute(sql, (id, ))
  myResult = mycursor.fetchall()
  return render_template('edit.html', my_list = myResult)

@app.route("/update", methods = ['POST'])
def update():
  if request.method == 'POST':
    userDetails = request.form
    print(userDetails)
    sql = "UPDATE student SET first_name = %s, last_name = %s, age = %s, gender = %s, email = %s, faculty = %s WHERE id = %s"
    val = (userDetails['first_name'], userDetails['last_name'], userDetails['age'], userDetails['gender'], userDetails['email'], userDetails['faculty'], userDetails['id'])
    mycursor.execute(sql, val)
    mydb.commit()
  return redirect(url_for('displayTable'))


if __name__ == '__main__':
  app.run(host='localhost', port=8080, debug=True)
