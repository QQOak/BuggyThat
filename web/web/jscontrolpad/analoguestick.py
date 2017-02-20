from .jscontrolbase import JsControlBase

class AnalogueStick(JsControlBase):
	
	def __init__(self, name):
		self._name = name
	
	def showname(self):
		return self._name
