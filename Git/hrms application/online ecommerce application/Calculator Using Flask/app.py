from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self):
        result = self.num1 + self.num2
        return f"The Addition of {self.num1} and {self.num2} is {result}"

    def subtract(self):
        result = self.num1 - self.num2
        return f"The Subtraction of {self.num2} from {self.num1} is {result}"

    def multiply(self):
        result = self.num1 * self.num2
        return f"The Multiplication of {self.num1} and {self.num2} is {result}"

    def divide(self):
        if self.num2 != 0:
            result = self.num1 / self.num2
            return f"The Division of {self.num1} by {self.num2} is {result}"
        else:
            return "Cannot divide by zero."

@app.route('/', methods=['GET', 'POST'])
def index():
    calculator = Calculator()

    if request.method == 'POST':
        calculator.num1 = float(request.form['num1'])
        calculator.num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = calculator.add()
        elif operation == 'subtract':
            result = calculator.subtract()
        elif operation == 'multiply':
            result = calculator.multiply()
        elif operation == 'divide':
            result = calculator.divide()
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
