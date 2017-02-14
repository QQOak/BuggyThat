class JsControlBase:
	"""Class from which all JsControls are to be inherited"""
		
	# Name
	@property
	def name(self, name):
		return self._name
		
	@name.setter
	def name(self, value):
		self._name = value
	
	@name.deleter
	def name(self):
		del self._name
	

	# Position on page.
	@property
	def position(self, positionXY):
		return self._positionXY
		
	@name.setter
	def name(self, value):
		self._positionXY = value
	
	@name.deleter
	def name(self):
		del self._positionXY
	

	
