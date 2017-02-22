#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import render_template, send_from_directory
from flask import request

from jscontrolpad import JsControlPad
import json

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
	return render_template('controlpad.html', Title='Control Pad')
	

	
@app.route('/controlpad/api/', methods=['GET','POST'])
def controlPadApi():
	
	leftStickDirection = 0
	leftStickMagnitude = 0
	rightStickDirection = 0
	rightStickMagnitude = 0
	
	jsoncontent = request.get_json()
	
	#print(jsoncontent['thumbstickValues'][0]['id'])
		
	if (jsoncontent['thumbstickValues'][0]['id'] == 'LeftStick'):
		print('LeftStick')
		leftStickDirection = jsoncontent['thumbstickValues'][0]['direction']
		leftStickMagnitude = jsoncontent['thumbstickValues'][0]['magnitude']

	if (jsoncontent['thumbstickValues'][0]['id'] == 'RightStick'):
		print('RightStick')
		rightStickDirection = jsoncontent['thumbstickValues'][0]['direction']
		rightStickMagnitude = jsoncontent['thumbstickValues'][0]['magnitude']		
		

	
	leftstick = {}
	leftstick['id'] = 'LeftStick'
	leftstick['xAxis'] = 0
	leftstick['yAxis'] = 0
	leftstick['direction'] = leftStickDirection
	leftstick['magnitude'] = leftStickMagnitude
	
	

	rightstick = {}
	rightstick['id'] = 'RightStick'
	rightstick['xAxis'] = 0
	rightstick['yAxis'] = 0
	rightstick['direction'] = rightStickDirection
	rightstick['magnitude'] = rightStickMagnitude
	

	thumbstickValues = {}
	thumbstickValues['LeftStick'] = leftstick
	thumbstickValues['RightStick'] = rightstick

	response = {}
	response['id'] = 0
	response['thumbstickValues'] = thumbstickValues
	

	#$leftStick = array('id' => 'LeftStick', 'xAxis' => 0, 'yAxis' => 0, 'direction' => 0, 'magnitude' => 0);
	#$rightStick = array('id' => 'RightStick', 'xAxis' => 0, 'yAxis' => 0, 'direction' => 0, 'magnitude' => 0);
	#$controller = array('id' => 0, 'thumbstickValues' => array('LeftStick' => $leftStick, 'RightStick' => $rightStick));
	#$controllerPosition = json_encode($controller, JSON_FORCE_OBJECT);
	#print($controllerPosition);
	

	#pint(jsoncontent)
	#for key,value in jsoncontent.items():
	#	print(key, value)

	
	return json.dumps(response)
	



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
	app.run(debug=True, host='0.0.0.0', port=int("5000"))

	
if __name__ == '__main__':
	main()

