from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# 1. render template
# 2. passing data
# 3. jinja
@app.route("/")          
def index_page():
    return render_template("index.html", message="My first successful Flask page", count=2)

# 4. routes with templates
@app.route("/textgame/<textcolor>")
def textgame_page(textcolor):
    print(textcolor)
    return render_template("textgame.html", color_in_page=textcolor)

# 5. static files
@app.route("/stylingdemo")
def styling_page():
    return render_template("styledpage.html")

# 6. Like dashboard
@app.route("/students")
def student_dashboard():
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("dashboard.html", student_list = student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

