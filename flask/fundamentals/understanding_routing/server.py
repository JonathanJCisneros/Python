from flask import Flask  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route("/")          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!"  # Return the string 'Hello World!' as a response

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def insert(name):
    return "Hi " + name + "!"

@app.route("/repeat/<int:num>/<string:name>")
def repeat(num, name):
    output = ""

    for i in range(0, num):
        output += f"<p>{name}</p>"

    return output


# "http://127.0.0.1:5000"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

