from flask import Flask,render_template
import request


app = Flask(__name__)

@app.route('/')
def main_data():
    return render_template()

@app.route('/home')
def home_page():
    return render_template('home_page.html')

@app.route('/website')
def my_website_home():
    return render_template('my_website_home.html')

@app.route('/legend')
def legend_form():
    return render_template('legend.html')




if __name__ == "__main__":
    app.run(debug=True)