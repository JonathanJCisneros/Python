from flask import Flask, render_template

app = Flask(__name__)

list_todos = [{
    "todo" : "Learn templates in flask",
    "status" : "Complete"
},
{
    "todo" : "Learn Object Orientation Programming",
    "status" : "Complete"
},
{
    "todo" : "Learn Deployment",
    "status" : "Cancel"
}]

@app.route("/hello")
def hello_from_flask():
    return "Hello class! This message is coming from your first server with flask!"

@app.route("/goodbye/class")
def goodbye_from_flask():
    print("This works so far...")
    return "<h1> goodbye class, time to enter your breakout rooms!</h1>"

@app.route("/number/<int:num>")
def show_number(num):
    print(f"This number: {num}")
    return f"This works because you can see the number here: {num}"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", first_name = "Alexander", list_todos = list_todos)

"http://127.0.0.1:5000"

if __name__ == "__main__":
    app.run(debug = True)

