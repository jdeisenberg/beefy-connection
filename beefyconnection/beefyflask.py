from flask import Flask,render_template
app = Flask(__name__)

def globals():
    return { 'title' : 'Beefy Connection!',
             'logo'  : '/static/images/beefy.png'}

@app.route("/")
def form():
    return render_template('mainform.html',**globals())

if __name__ == "__main__":
    app.debug = True
    app.run()
