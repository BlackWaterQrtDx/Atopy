import os
import sys

class Atopy(object):
	def __init__(self, sfile = None, wdebug = False, run = True, fsep = '\\'):
		self.debug = wdebug
		self.sfile = sfile
		self.dirs = []
		self.mpath = ''
		self.fsep = fsep
		self.ddir = os.path.dirname(os.path.realpath(__file__)).replace(self.fsep, '/')
		self.lists = self.getCwDirectory()
		self.mobjects = {}

		if run:
			self.autoload(self.lists)

	def getCwDirectory(self, apath = None):
		if apath is not None:
			os.chdir(apath)
			return os.listdir(apath)

		os.chdir(self.ddir)
		return os.listdir(self.ddir)

	def setCwDirectory(self, apath = None, supdir = 0):
		if apath is not None:
			ndir = os.path.dirname(os.path.realpath(apath))

			for i in range(0, supdir):
				ndir = os.path.dirname(ndir).replace(self.fsep, '/')

			sys.path.append(ndir)
			self.ddir = ndir

		os.chdir(self.ddir)
		self.lists = os.listdir(self.ddir)

	def autoload(self, lists = None, lev = 0):
		lists = self.lists if lists is None else lists
			
		for fod in lists:
			if self.isValidDir(fod):
				self.dirs.append(fod)
			elif self.isValidFile(fod):
				try:
					imp = __import__(self.getImportPath(fod), locals = True, globals = True, fromlist = [None], level = 0)
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
				self.dirs = []
				self.mpath = mpath
				self.mpath += idir if lev == 0 else '.' + idir
				self.autoload(self.getCwDirectory(self.ddir + '/' + self.mpath.replace('.', '/')), lev = lev + 1)
		return

	def get(self, mname):
		if mname in self.mobjects:
			return self.mobjects.get(mname)

		print('[MODULE] ' + mname + ' [NOT FOUND]')
		return None

	def listModules(self):
		print('\n***********************\n', ' ' * int((len('***********************') / 2) - len('MODULE LIST') / 2 - 1), end="")
		print('MODULE LIST')
		print('***********************')
		for mod in self.mobjects:
			print('[*]', mod, '==>', self.mobjects[mod])
		print('***********************\n')

	def getImportPath(self, file):
		return self.mpath + '.' + file.replace('.py', '') if len(self.mpath) > 0 else self.mpath + file.replace('.py', '')

	def getClassname(self, file):
		return file.replace('.py', '')

	def isValidFile(self, file):
		return os.path.isfile(file) and not file.startswith(__file__.split(self.fsep)[-1]) and not file.startswith(self.sfile.split(self.fsep)[-1]) and file.endswith('.py') and not file.startswith('__') and not file.endswith('__.py')

	def isValidDir(self, cdir):
		return os.path.isdir(cdir) and not cdir.startswith('__') and not cdir.endswith('__') and not '.' in cdir
