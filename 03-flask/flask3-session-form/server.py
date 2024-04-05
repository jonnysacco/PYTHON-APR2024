from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "type whatever you want as long as it is a secret for you"

# Step 1: GET request to render a page to display the form.html (how to create a form)
@app.route("/bugs/new")
def new_bug_form():
    return render_template("new_bug.html")

# Step 2: Create a POST function to receive the POST form request 
@app.route("/bugs/new/process", methods=["POST"]) # Route must match form action
def process_new_bug():
    print("In post route")
    print(request.form)
    print(request.form["title"])
    # Step 3: Process the data (store it in session) and redirect to other routes
    session["title"] = request.form["title"]
    session["assignment"] = request.form["assignment"]
    session["description"] = request.form["description"]
    session["username"] = request.form["username"]
    return redirect("/bugs/result")

# Step 4: Add that redirected route & template file
@app.route("/bugs/result")
def bug_result_page():
    return render_template("bug_result.html")

if __name__=="__main__":   
    app.run(debug=True, port=5001) 