class User():
	def __init__(self) -> None:
		# key states
		self.id = 0
		self.account = ''
		self.password = ''
		# non-key states
		self.name = ''
		self.email = ''
		self.phone = ''
		self.head_image = '' # an URL storing the image on cloud