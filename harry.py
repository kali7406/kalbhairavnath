# here i making my own website from bootstraps after learning so let'start the projects?
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Home_page():
    return render_template('index.html')