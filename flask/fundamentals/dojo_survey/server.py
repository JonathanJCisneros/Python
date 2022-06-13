from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "Maybe important info.."


@app.route("/")
def lets_start():
    return render_template("form.html")

@app.route("/process", methods = ['POST'])
def new_survey():
    print(request.form)
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("results.html")




if __name__=="__main__":
    app.run(debug=True)

# "http://127.0.0.1:5000"
