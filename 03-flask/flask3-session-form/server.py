from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "type whatever you want as long as it is a secret for you"

@app.route("/")
def test_session_counter_page():
    # 1. If the session is available
    # 2. update the session (by incrementing)
    # 3. If the session is not available  
    # 4. set the initial session
    pass # replace pass with your code

@app.route("/clear")
def clear_session():
    # Clear the session and redirect
    pass

# Step 1: GET request to render a page to display the form.html (how to create a form)
# Step 2: Create a POST function to receive the POST form request 
# Step 3: Process the data (store it in session) and redirect to other routes
# Step 4: Add that redirected route & template file

if __name__=="__main__":   
    app.run(debug=True) 