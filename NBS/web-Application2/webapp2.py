from flask import Flask, render_template

app = Flask(__name__)

@app.route("/info/<Ename>/<Esalary>")
def salaryslip4(Ename,Esalary):
    return render_template("salaryslip.html",name=Ename,salary=int(Esalary),C="Green")

app.run()