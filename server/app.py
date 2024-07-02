#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "Python Operations with Flask Routing and Views"
    return render_template('index.html', title=title)

@app.route("/print/<string:data>")
def print_string(data):
    print(data)
    return f"<h1>Printed string: {data}</h1>"

@app.route("/count/<int:count>")
def count(number):
    return "\n".join(str(x) for x in range(number + 1))   

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    operations = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "div": lambda a, b: a / b, "%": lambda a, b: a % b}
    if operation not in operations: 
      return "Invalid operation provided."
    result = operations[operation](num1, num2)
    return f"<h1>Result: {num1} {operation} {num2} = {result}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
