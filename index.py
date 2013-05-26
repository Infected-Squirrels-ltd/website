import os
import bcpl
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/interpret", methods=['POST'])
def interpret():
	return bcpl.run(request.form['code'])


if __name__ == "__main__":
	app.debug = True
	app.run()