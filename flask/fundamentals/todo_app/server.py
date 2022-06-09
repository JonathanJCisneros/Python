from flask import Flask

app = Flask(__name__)

@app.route("/hello")

def hello_from_flask():
    return "Hello class! This message is coming from your first server with flask!"

@app.route("/goodbye/class")
def goodbye_from_flask():
    print("This works so far...")
    return "<h1> goodbye class, time to enter your breakout rooms!</h1>"

@app.route("/number/<num:int>")
def show_number(num):
    print(f"This number: {num}")
    return "This works because you can see the number here:"

"http://127.0.0.1:5000"

if __name__ == "__main__":
    app.run(debug = True)

