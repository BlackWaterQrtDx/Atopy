
class Bar():
	def __init__(self):
		pass

	def helloBar(self):
		print('[IN Bar.py] Hello World')

def __export__():
	return Bar()