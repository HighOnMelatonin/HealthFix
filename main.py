import flask
import cases
import smm
import vaccination
from flask import render_template


app = flask.Flask(__name__)

@app.route('/')
def home():
    newCases = cases.gov()
    updates = smm.govupdate()
    workplace = smm.workplace()
    vacSignup = vaccination.vaccineRegistration()

    return render_template('final.html', newCases = newCases, updates = updates, workplace = workplace, vacSignup = vacSignup)




if __name__ == '__main__':
    app.run()



