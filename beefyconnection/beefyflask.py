import os,re
from flask import *
from beefy_db import BeefyDatabase
app = Flask(__name__)

def globals():
    return { 'title' : 'Beefy Connection!',
             'logo'  : '/static/images/beefy.png'}

@app.route("/")
def form():
    return render_template('mainform.html',**globals())

@app.route("/bc-post",methods=['POST'])
def post():
    session['name'] = request.form.get('first-name') + request.form.get('last-name')
    return jsonify(status="Success")

@app.route("/bc-upload",methods=['POST'])
def upload():
    try:
        name = session['name']
        f = re.sub(r'data.*,','',request.form['photo'] +'==').decode('base64') 
        fn = open("%s/%s/%s" % (os.path.dirname(os.path.realpath(__file__)),"uploads",name + ".png"),'wb')
	fn.write(f)
	fn.close()
	return jsonify(status="Success")
    except Exception as e:
        return jsonify(**{ "status" : "Error",
                           "message" : str(e)})

@app.route("/bc-success")
def success():
    return render_template('thanks.html',**globals())

if __name__ == "__main__":
    app.secret_key = 'beefy-connect'
    app.debug = True
    app.run()
