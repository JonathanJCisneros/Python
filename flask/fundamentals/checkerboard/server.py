from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def standard_board():
    return render_template("index.html", x = 8, y = 8, color1 = "blue", color2 = "red")

@app.route("/4")
def custom_row():
    return render_template("index.html", x = 4, y = 8, color1 = "blue", color2 = "red")

@app.route("/<int:x>/<int:y>")
def custom_board(x,y):
    return render_template("index.html", x = x, y = y, color1 = "blue", color2 = "red")

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def custom_all(x,y,color1,color2):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)


if __name__ == "__main__":
    app.run(debug = True)

# "http://127.0.0.1:5000"