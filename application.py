from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
    return render_template("index.html")

@app.route('/application-form')
def application_form():
    """show application form"""

    return render_template("application-form.html")

@app.route('/response', methods=['POST'])
def application_response():
    """response to the application form"""

    # firstname = request.form.get('firstname')
    # lastname = request.form.get('lastname')
    # job = request.form.get('job')
    # salary = request.form.get('salary')

    # return render_template("application-response.html", firstname=firstname,
    # lastname=lastname, job=job, salary=salary)

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    job = request.form['job']
    salary = request.form['salary']

    return render_template('application-response.html')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
