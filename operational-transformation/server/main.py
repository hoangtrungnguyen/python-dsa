# Import the Flask class from the flask module
from flask import Flask, render_template, request, jsonify

# Create an instance of the Flask class.
# The __name__ argument helps Flask locate resources like templates and static files.
app = Flask(__name__)

# Define a route for the home page.
# The '@app.route('/')' decorator associates the 'home' function with the URL '/'.
@app.route('/')
def home():
    """
Renders the home page of the Flask application.
This function will be executed when a user navigates to the root URL.
    """
    return "<h1>Welcome to the Flask App!</h1><p>Navigate to /hello/yourname to see a personalized greeting.</p>"

# Define a route that accepts a dynamic part in the URL.
# The '<name>' part captures a value from the URL and passes it as an argument to the function.
@app.route('/hello/<name>')
def hello(name):
    """
Greets the user with a personalized message.
The 'name' parameter is captured from the URL.
    """
    return f"Hello, {name.capitalize()}! Welcome to your Flask app."

# Define a route that demonstrates handling different HTTP methods.
# This route allows both GET and POST requests.
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """
Handles form submissions.
- On GET request, it might show a form.
- On POST request, it processes the submitted data.
    """
    if request.method == 'POST':
        # If the request is POST, get data from the form
        data = request.form.get('user_input')
        if data:
            return f"You submitted: {data}"
        else:
            return "No data submitted.", 400 # Return 400 Bad Request if no data
    else:
        # If the request is GET, show a simple form
        return """
<h1>Submit Data</h1>
<form method="POST">
<label for="user_input">Enter something:</label><br>
<input type="text" id="user_input" name="user_input"><br><br>
<input type="submit" value="Submit">
</form>
"""

# Define a route for a simple API endpoint returning JSON.
@app.route('/api/data')
def api_data():
    """
Returns a JSON response.
This demonstrates how to create a basic API endpoint.
    """
    data = {
        "message": "This is a JSON response from your Flask API.",
        "version": "1.0",
        "items": ["apple", "banana", "cherry"]
    }
    # jsonify automatically sets the Content-Type header to application/json
    return jsonify(data)

# Run the Flask application.
# 'if __name__ == '__main__':'' ensures that the app.run() command is only executed
# when the script is run directly (not when imported as a module).
# debug=True enables debug mode, which provides detailed error messages and
# automatically reloads the server when code changes.
if __name__ == '__main__':
    app.run(debug=True)
    