from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/timestableof/<num>")
def timestable(num):
    return render_template("timestable.html",T=int(num))

app.run(port=81,debug=True)