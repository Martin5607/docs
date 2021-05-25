from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")
@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

app.run()