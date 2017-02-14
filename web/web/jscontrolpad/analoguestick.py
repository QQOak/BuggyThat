from jscontrolpad.jscontrolbase import JsControlBase
dir
class AnalogueStick(JsControlBase):
	
	def __init__(self, name):
		self._name = name
	
	def showname(self):
		return self._name
