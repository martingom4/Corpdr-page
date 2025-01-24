from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Corpdr Page Backend!"

@app.route('/about')
def about():
    return "This is the about page of Corpdr."

if __name__ == '__main__':
    app.run(debug=True)
