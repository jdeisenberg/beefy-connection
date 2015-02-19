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
    databaseConnector = new BeefyDatabase("sqlite3://person.db")
    databaseConnector.addPerson(first_name="Joshua",
                                last_name="Santos",
                                phone="9094360697",
                                city="Fontana",
                                state="California",
                                postal_code="92336",
                                irc="nerdsville",
                                fb="nerdsville",
                                twitter="nerdsvillellc",
                                interests="tennis, programming, math",
                                email="nerdsville@nerdsville.net",
                                fas="nerdsville")
    return databaseConnector.readPerson()

"""
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    phone=Column(String)
    city=Column(String)
    state=Column(String)
    postal_code=Column(String)
    irc=Column(String)
    fb=Column(String)
    twitter=Column(String)
    interests=Column(String)
    email=Column(String)
    fas=Column(String)

"""
@app.route("/bc-success")
def success():
    return render_template('thanks.html',**globals())

if __name__ == "__main__":
    app.debug = True
    app.run()
