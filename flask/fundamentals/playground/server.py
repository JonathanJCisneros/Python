from flask import Flask, render_templates


app = Flask(__name__)
@app.route('/')
def index():
    return "You're in the wrong page bro"

@app.route("/play")
    return render_templates("index.html")




if __name__=="__main__":
    app.run(debug=True)

