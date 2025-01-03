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
    try: 
        answer = a / b 
        return f"{a} / {b} = {answer}" 
    except ZeroDivisionError as e: 
        app.logger.error("ZeroDivisionError: %s", e, exc_info=True) 
        return "Error: Division by zero is not allowed." 
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
            # Handle division by zero explicitly 
            if b == 0: 
                result = "Error: Division by zero is not allowed." 
                app.logger.error("Attempted division by zero: num1=%s, num2=%s", a, b) 
            else: 
                result = div(a, b) 
    return render_template("index.html", result=result) 
if __name__ == "__main__": 
    app.run(debug=True, port=8000)  # INPUT_REQUIRED {Change port if needed}