#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, send_from_directory
from jscontrolpad import JsControlPad

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile=('config.py')

jscp = JsControlPad()


@app.route('/settings')
def settings():
	templateData = {
		'Title' : 'Settings'
		}
	return render_template('template.html', **templateData)

@app.route('/about')
def about():
	return render_template('template.html', Title='About')
	
@app.route('/controlpad')
def controlpad():
	#return jscp.renderPad()
	return render_template('template.html', Title='Control Pad')
	





# favicon cludge for older browsers
# -------
# debatable as to it's use here as it will be used from a phone or tablet.
# included onlyfor reference
@app.route('/favicon.ico')
def favIcon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microosft.icon')



@app.route('/')
def index():
	return about()
	
	







def main():
	app.run(host='0.0.0.0', port=int("5000"))

	
if __name__ == '__main__':
	main()

