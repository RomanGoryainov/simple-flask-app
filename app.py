import os
from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_wtf import FlaskForm
app = Flask(__name__)
csrf = CsrfProtect()
csrf.init_app(app) # Compliant

@app.route("/")
def main():
    return "Welcome!"
class unprotected_form(FlaskForm):
    class Meta:
        csrf = True # Compliant

@app.route('/howareyou')
def hello():
    return 'I am good, how about you?'
class unprotected_form(FlaskForm):
    class Meta:
        csrf = True # Compliant
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)