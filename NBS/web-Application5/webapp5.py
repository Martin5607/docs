from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("inputfor.html")

@app.route("/registration",methods=["POST"])
def regPage():
    return render_template("registration.html",data=request.form)
    
    #return request.form["na"]+" is getting " + request.form["sa"] + " salary ";


app.run()