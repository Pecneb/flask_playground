from flask import Flask, render_template, url_for, request
from markupsafe import Markup
app = Flask(__name__)
'''
This is a playground for creating webapp features with flask.
'''

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
        return do_the_login(user, passw)
    else:
        return show_the_login_form()


def do_the_login(username, password):
    return 'Welcome %s! Login successful! Your password is %s'%(username, password)

def show_the_login_form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)