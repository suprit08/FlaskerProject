from flask import Flask, render_template

app = Flask(__name__)

#Sample JSON data
Students = [
    {"name":"Suprit Sonar", "subject":"php"},
    {"name":"nilesh rajput", "subject":"html"},
    {"name":"rohit deshmukh", "subject":"python"},
]

@app.route('/')
def showIndex():
    return render_template("index.html", students=Students)

@app.route('/about')
def showAbout():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=3000)