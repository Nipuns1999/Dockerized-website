from flask import Flask, render_template,  url_for

app = Flask(__name__)

@app.route("/Home")
def home():
    return render_template('index.html')

@app.route("/AboutMe")
def services():
    return render_template('about.html')

@app.route("/Resume")
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run()
