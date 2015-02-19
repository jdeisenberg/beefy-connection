from flask import *
app = Flask(__name__)

def globals():
    return { 'title' : 'Beefy Connection!',
             'logo'  : '/static/images/beefy.png'}

@app.route("/")
def form():
    return render_template('mainform.html',**globals())

@app.route("/bc-post",methods=['POST'])
def post():
    return str(request.form)

@app.route("/bc-success")
def success():
    return render_template('thanks.html',**globals())

if __name__ == "__main__":
    app.debug = True
    app.run()
