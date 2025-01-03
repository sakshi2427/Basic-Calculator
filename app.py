from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
    answer = a + b
    return f"{a} + {b} = {answer}"

def sub(a, b):
    answer = a - b
    return f"{a} - {b} = {answer}"

def mul(a, b):
    answer = a * b
    return f"{a} * {b} = {answer}"

def div(a, b):
    answer = a / b
    return f"{a} / {b} = {answer}"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        operation = request.form["operation"]
        a = int(request.form["num1"])
        b = int(request.form["num2"])

        if operation == "add":
            result = add(a, b)
        elif operation == "sub":
            result = sub(a, b)
        elif operation == "mul":
            result = mul(a, b)
        elif operation == "div":
            result = div(a, b)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
