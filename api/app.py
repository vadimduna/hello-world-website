from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)

@app.route("/submit_sum", methods=["POST"])
def sumbit_sum():
    input_num_1 = request.form.get("num_1")
    input_num_2 = request.form.get("num_2")
    return render_template("sum.html", num1=input_num_1, num2=input_num_2)


