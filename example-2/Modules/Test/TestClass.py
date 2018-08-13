from Atopy import Atopy

autoloader = Atopy(__file__, wdebug = True, run = False)
autoloader.setCwDirectory(__file__, supdir = 2)
autoloader.autoload()

autoloader.listModules()

autoloader.get('Main').helloMain()