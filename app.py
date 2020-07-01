from __future__ import unicode_literals
import subprocess
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
lnk = ''

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    print("The url address is '" + email + "'")
    global lnk
    lnk = email
    file1 = open("url.txt", "w")
    file1.write(email)
    file1.close()
    process = subprocess.Popen('py amazon.com.py', shell=True)
    process.wait()
    print("app file")
    return render_template('table.html')


# main driver
if __name__ == '__main__':
 # run app
 app.run(debug=True, threaded=True)