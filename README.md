# Atopy
Python Autoloader


To use this object, place this file at the root of your project and extend your main class of the Atopy class (also put in the root) and call its <__init__> method.

You can also call the Atopy class without inheriting it.

For a "custom" autoloading, create the <__export__> function in your .py files and have it return what you want.

Atopy Methods:

	- __init__(current_file_where_atopy_is_launch, wdebub = False, run = True):
		==> __current_file_where_atopy_is_launch__ parameter specifies the file that initializes the search
		==> __wdebug__ parameter specifies if debug mode is activate
		==> __run__ parameter specifies if run autoload method in the <__init__> method

	- setCwDirectory(new_path, supdir = 0):
		==> __supdir__ parameter determines the number of parent folders to go up for the new path

	- autoload():
		==> launch the research / autoloading

	- get(module_name):
		==> retrieve an module found

	- listModules():
		==> list all modules found
