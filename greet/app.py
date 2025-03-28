from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the homepage!"

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

if __name__ == "__main__":
    app.run(debug=True)