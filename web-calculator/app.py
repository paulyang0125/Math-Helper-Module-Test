from flask import Flask, request, render_template
import math

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def natural_logarithm(x):
    try:
        return math.log(x)
    except ValueError:
        return "Error: Non-positive value for logarithm"

def exponential(x):
    return math.exp(x)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        operation = request.form.get("operation")
        a = float(request.form.get("a"))
        b = float(request.form.get("b", 0))
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        elif operation == "natural_logarithm":
            result = natural_logarithm(a)
        elif operation == "exponential":
            result = exponential(a)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
