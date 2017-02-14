from jscontrolpad.analoguestick import AnalogueStick


class JsControlPad:

	__jscontrols = []
	
	def __init__(self):
		self.__jscontrols = []
	
	
	def addControlToControlPad(self, controltype, controlname):
			
		if controltype == "analoguestick":
			self.__jscontrols.append(AnalogueStick(controlname))
		
		return('Added %s named %s' % (controltype, len(self.__jscontrols)))



	def renderPad(self):
		return('rendering pad')
