import os, datetime,re
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
    session['name'] = request.form.get('first-name') + request.form.get('last-name')
    return str(request.form)

@app.route("/bc-upload",methods=['POST'])
def upload():
    try:
        name = session['name']
        f = re.sub('data:image/png;base64,','',request.form['photo'] +'++').decode('base64') 
        fn = open("%s/%s/%s" % (os.path.dirname(os.path.realpath(__file__)),"uploads",name + str(datetime.datetime.now()) + ".png"),'wb')
	fn.write(f)
	fn.close()
	return jsonify(stat="Success")
    except Exception as e:
        return jsonify(**{ "stat" : "Error",
                           "message" : str(e),
                           "data" : f})

@app.route("/bc-success")
def success():
    return render_template('thanks.html',**globals())

if __name__ == "__main__":
    app.secret_key = 'beefy-connect'
    app.debug = True
    app.run()
