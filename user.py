class User():
	def __init__(self,
				 id,
				 account,
				 password,
				 name,
				 email,
				 phone,
				 head_image) -> None:
		# key states
		self.id = id
		self.account = account
		self.password = password
		# non-key states
		self.name = name
		self.email = email
		self.phone = phone
		self.head_image = head_image  # an URL storing the image on cloud
		# TODO : add personal setting page to finish non-key states