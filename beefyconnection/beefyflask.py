from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def form():
    data = { 'title' : 'Beefy Connection'}
    return render_template('mainform.html',**data)

if __name__ == "__main__":
    app.debug = True
    app.run()
