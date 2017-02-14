#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from jscontrolpad import JsControlPad

app = Flask(__name__)
jscp = JsControlPad()


@app.route('/config')
def config():
	templateData = {
		'Title' : 'Configuration'
		}
	return render_template('template.html', **templateData)



@app.route('/control/<config>')
def control_withconfig(config):
	return render_template('template.html', Title=config)
	
@app.route('/control/render')
def contro_showlist():
	return jscp.renderPad()
	
	
@app.route('/controller/addcontrol/<controltype>/<controlname>')
def addControlToControlPad(controltype, controlname):
	eventArgs = {
		'controltype' : controltype,
		'controlname' : controlname
	}
	return jscp.addControlToControlPad(**eventArgs)
	

@app.route('/')
def index():
	return render_template('template.html', Title='BuggyThat')
	
	







def main():
	#app.run(debug=True, host='0.0.0.0', port=int("5000"))
	#app.run(debug=False, host='0.0.0.0', port=int("5000"))
	app.run(threaded=True, debug=True, host='0.0.0.0', port=int("5000"))
	
if __name__ == '__main__':
	main()

