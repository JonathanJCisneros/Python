from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    return "You're in the wrong page bro"

@app.route("/play")
def start():    
    return render_template("index.html", num = 3, color = "blue")

@app.route("/play/<int:num>")
def custom(num):
    return render_template("index.html", num=num, color = "blue")

@app.route("/play/<int:num>/<string:color>")
def custom1(num, color):
    return render_template("index.html", num=num, color = color)



# http://127.0.0.1.5000

if __name__=="__main__":
    app.run(debug=True)

