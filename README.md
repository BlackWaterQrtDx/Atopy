# Atopy
## This is an Python Autoloader


To use this object, place this file anywhere in your project and call the Atopy class directly or inherit it from your main class, and then call its <__init__> method.

You can also call the Atopy class without inheriting it.

For a "custom" autoloading, create the <__export__> function in your .py files and have it return what you want.

Atopy Methods:

	* __init__(current_file_where_atopy_is_launch, wdebub = False, run = True, fsep = '\\'):
		 * __current_file_where_atopy_is_launch__ parameter specifies the file that initializes the search ==> pass <__file__> var
		 * __wdebug__ parameter specifies if debug mode is activate
		 * __run__ parameter specifies if run autoload method in the <__init__> method
		 * __fsep__ parameter specifies the filename separator

	* setCwDirectory(new_path, supdir = 0):
		* __new_path__ parameter determines the master path of the research
		* __supdir__ parameter determines the number of parent folders to go up for the new path

	* autoload():
		* launch the research / autoloading

	* get(module_name):
		* retrieve an module found

	* listModules():
		* list all modules found

Example:

```python
# App/Atopy.py
# App/Main.py
# App/Bar/Bar.py

# In App/Bar/Bar.py
class Bar(object):
	def __init__(self):
		pass

	def sayHello(self):
		print('Hello World')

def __export__():
	return Bar()


# In App/Main.py
from Atopy import Atopy

class Main(Atopy):
	def __init__(self):
		super().__init__(__file__, wdebug = True)

app = Main()
app.listModules()
app.get('Bar').sayHello() # print ==> "Hello World"
```
