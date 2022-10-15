from flask import Flask,render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("frontpage.html")
@app.route('/abo')
def about():
    return render_template("abo.html")
if __name__ == '__main__':
    app.run()