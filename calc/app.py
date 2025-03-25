from flask import Flask, request
from calc.operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the calc homepage!"

@app.route('/add')
def addition():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtraction():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def division():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = div(a, b)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
