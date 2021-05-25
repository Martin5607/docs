from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123sql@localhost/nbs'

db = SQLAlchemy(app)

class school(db.Model):
    regno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    marks = db.Column(db.Integer)

student=school()

@app.route("/")
def homepage():
    return render_template("studentform.html")

@app.route("/addrecord",methods=["POST"])
def addrecord():
    student=school()
    student.regno=int(request.form["regno"])
    student.name=request.form["name"]
    student.marks=int(request.form["marks"])
    db.session.add(student)
    db.session.commit()
    return "record inserted"

app.run(debug=True)