#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test/nested1')
def layout1():
	return render_template('nested1.html')
	
@app.route('/test/nested2')
def layout1():
	return render_template('nested2.html')

@app.route('/help')
def help():
	return app.send_static_file('help.html')

@app.route('/config')
def config():
	templateData = {
		'Title' : 'Configuration'
		}
	return render_template('template.html', **templateData)

@app.route('/control')
def contro_showlist():
	return 'hello'

@app.route('/control/<config>')
def control_withconfig(config):
	return render_template('template.html', Title=config)

@app.route('/')
def index():
	return render_template('template.html', Title='BuggyThat')
	
	







def main():
	app.run(debug=True, host='0.0.0.0', port=int("5000"))
	
if __name__ == '__main__':
	main()

