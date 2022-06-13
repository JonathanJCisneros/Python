from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template("index.html")

@app.route("/destroy_session")
def clear_session():
    session["counter"] = 0
    print("The counter has been cleared")
    return redirect("/")

# "http://127.0.0.1:5000"

if __name__ == "__main__":
    app.run(debug = True)