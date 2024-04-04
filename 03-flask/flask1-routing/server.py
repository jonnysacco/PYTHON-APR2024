from flask import Flask 
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "Hello"

@app.route("/success")
def success_message():
    print("AM I here?") # Goes into the terminal (PYTHON)
    return "something" # Response that send back to the browser

# http://localhost:5001/travel/tokyo
@app.route("/travel/<place>")
def show_place(place):
    print(place)
    return "Travelling to " + place


# http://localhost:5001/travel/hokkaido/march
@app.route("/travel/<place>/<int:count>")
def show_place_with_count(place, count):
    message = place * count
    return message

@app.errorhandler(404)
def not_found_page(e):
    print(e)
    return "404 Not Found"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)