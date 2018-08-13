
from Atopy import Atopy

class Main(Atopy):
	def __init__(self):
		print('[INIT] Main')
		super().__init__(__file__, wdebug = False)

	def startExample(self):
		self.listModules()

		self.get('function').helloFunction()
		self.get('Bar').helloBar()
		self.get('BazClass').Baz().helloBaz()

Main().startExample()

##########
print("\n[OR]","="*20, "[OR]")
##########

autoloader = Atopy(__file__)
autoloader.listModules()

autoloader.get('function').helloFunction()
autoloader.get('Bar').helloBar()
autoloader.get('BazClass').Baz().helloBaz()
