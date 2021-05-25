from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<n>")
def first(n):
    if n=="Martin":
        return "Nationwide"
    else:
        return redirect('/login')
        

@app.route("/login")
def login()):
    return render_template("login.html")

@app.route("/company")
def company():
    return "Welcome to the office"

app.run(port=81,debug=True)