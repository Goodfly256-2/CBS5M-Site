import os

from flask import Flask, send_from_directory
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/WOSN.html')
def wosn():
  return render_template("WOSN.html")

@app.route('/rul.html')
def rul():
  return render_template("rul.html")

@app.route('/ser.html')
def ser():
  return render_template("ser.html")

@app.route('/news.html')
def news():
  return render_template("news.html")

@app.route('/Team.html')
def Team():
  return render_template("Team.html")

@app.route('/wallets.html')
def wal():
  return render_template("wallets.html")
@app.route('/ACKP.html')
def ACKR():
  return render_template("ACKP.html")


app.run(debug=True, host='0.0.0.0')
