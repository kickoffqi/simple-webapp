from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome! Hello, World!"

@app.route('/2026')
def hello():
    return 'Let's change yourself in 2026!!!'

if __name__ == "__main__":
    app.run()
