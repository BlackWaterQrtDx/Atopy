import os

class Atopy(object):
	def __init__(self, sfile = None, wdebug = False):
		self.debug = wdebug
		self.sfile = sfile
		self.dirs = []
		self.mpath = ''
		self.ddir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
		self.lists = self.getCwdDirectory()
		self.mobjects = {}

		self.autoload(self.lists)

	def getCwdDirectory(self, apath = None):
		if apath is not None:
			os.chdir(apath)
			return os.listdir(apath)

		os.chdir(self.ddir)
		return os.listdir(self.ddir)

	def autoload(self, lists, lev = 0):
		for fod in lists:
			if self.isValidDir(fod):
				self.dirs.append(fod)
			elif self.isValidFile(fod):
				try:
					imp = __import__(self.getImportPath(fod), locals = True, 
						globals = True, 
						fromlist = [None], 
						level = 0)

					self.mobjects[self.getClassname(fod)] = imp.__export__() if hasattr(imp, '__export__') else imp

					if self.debug:
						print('[IMPORT] ' + self.getImportPath(fod) + ' [SUCCESS]')
				except:
					print('[IMPORT] ' + self.getImportPath(fod) + ' [FAILED]')
					pass

		dirs = self.dirs
		mpath = self.mpath

		for idir in dirs:
			os.chdir(self.ddir + '/' + mpath.replace('.', '/'))

			if self.isValidDir(idir):
				self.mpath = mpath
				self.dirs = []
				self.mpath += idir if lev == 0 else '.' + idir
				cpath = self.ddir + '/' + self.mpath.replace('.', '/')
				self.autoload(self.getCwdDirectory(cpath), lev = lev + 1)
		return

	def get(self, mname):
		if mname in self.mobjects:
			return self.mobjects.get(mname)

		print('[MODULE] ' + mname + ' [NOT FOUND]')
		return None

	def listModules(self):
		print('\n***********************')
		print(' ' * int((len('***********************') / 2) - len('MODULE LIST') / 2 - 1), end=" ")
		print('MODULE LIST')
		print('***********************')
		for mod in self.mobjects:
			print('[*] ', end="")
			print(mod, end="")
			print(' ==> ', end="")
			print(self.mobjects[mod])
		print('***********************\n')

	def getImportPath(self, file):
		if len(self.mpath) > 0:
			return self.mpath + '.' + file.replace('.py', '')
		else:
			return self.mpath + file.replace('.py', '')

	def getClassname(self, file):
		return file.replace('.py', '')

	def isValidFile(self, file):
		if self.sfile is not None and file.startswith(self.sfile.split('\\')[-1]):
			return False
		return os.path.isfile(file) and not file.startswith(__file__.split('\\')[-1]) and file.endswith('.py') and not file.startswith('__') and not file.endswith('__.py')

	def isValidDir(self, cdir):
		return os.path.isdir(cdir) and not cdir.startswith('__') and not cdir.endswith('__') and not cdir.startswith('.')
