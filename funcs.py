from __future__ import print_function
import sys

def die(*mes):
	if len(mes) != 0:
		s = ' '.join([str(m) for m in mes])
		sys.stdout.write(s + '\n')
	sys.exit(0)

def int_all(*li):
	return [int(i) for i in li]

def str_all(*li):
	return [str(i) for i in li]

class Counter:
	def __init__(self):
		self.nb = 1

	def update(self):
		self.nb += 1

	def th(self, nb):
		# 5th for example
		return self.nb % nb == 0

def get_mtd(obj):
	all = dir(obj)
	all.remove('__doc__')
	all.remove('__module__')
	mtd = []
	for el in all:
		if 'method' in str(type(getattr(obj, el))):
			mtd.append(el)
	return mtd

def get_attr(obj):
	all = dir(obj)
	all.remove('__doc__')
	all.remove('__module__')
	attr = []
	for el in all:
		if not 'method' in str(type(getattr(obj, el))):
			attr.append(el)
	return attr

def echo(*args, **kwargs):
	""" To not match the research "print" """
	text = kwargs.get('sep', ' ').join([str(el) for el in args]) + kwargs.get('end', '\n')
	sys.stdout.write(text)

def debug(*anything, **args):
	""" 
		A simple function that print list and arg nicely.
		@params:
			start: char(s) to print at the begining         (default ``)
			sep  : char(s) to print between each `anything` (default `\n`)
			end  : char(s) to print at the end              (default `\n`)

	"""
	class window: # object to save var (like js)
		pass

	def get_type(anything):
		return str(type(anything)).replace("<type '", "").replace("'>", '')

	def default_val(d, key, val):
		if not key in d.keys():
			d[key] = val
		return True

	def debug_list(arr, indent=True):
		text = []
		window.indent += 1
		for i, thing in enumerate(arr):
			if type(thing) == list:
				text.append(debug_list(thing))
			elif type(thing) == dict:
				text.append(debug_dict(thing))
			else:
				if type(thing) == str:
					thing = '"' + thing + '"'
				elif type(thing) == int:
					thing = str(thing)
				else:
					thing = str(thing)
				text.append((window.char * window.indent) + thing + (',\n' if i < len(arr) - 1 else ''))
		text = ''.join(text)
		window.indent -= 1
		text = (window.indent * window.char * int(indent)) + '[\n' + text + '\n' + (window.indent * window.char) + ']\n'
		return text

	def debug_dict(arr, indent=True):
		text = []
		window.indent += 1
		for i, key in enumerate(arr.keys()):
			text.append((window.char * window.indent) + key + ': ')
			thing = arr[key]
			if type(thing) == list:
				text.append(debug_list(thing, False))
			elif type(thing) == dict:
				text.append(debug_dict(thing, False))
			else:
				if type(thing) == str:
					thing = '"' + thing + '"'
				elif type(thing) == int:
					thing = str(thing)
				else:
					thing = str(thing)
				text.append(thing + (',\n' if i < len(arr) - 1 else ''))
		text = ''.join(text)
		window.indent -= 1
		text = (window.indent * window.char) + '{\n' + text + '\n' + (window.indent * window.char) + '}\n'
		return text


	window.char = ' '
	default_val(args, 'tab', 4)
	if type(args['tab']) == int:
		window.char *= args['tab']
	elif type(args['tab']) == str:
		window.char = args['tab']
	else:
		echo('!error! `tab` args is not valid')

	window.indent = 0
	text = []
	for thing in anything:
		if type(thing) == list:
			text.append(debug_list(thing))
		elif type(thing) == dict:
			text.append(debug_dict(thing))
		else:
			if type(thing) == str:
				thing = '"' + thing + '"'
			elif type(thing) == int:
				thing = str(thing)
			text.append(thing)

	default_val(args, 'sep', '\n')
	default_val(args, 'end', '')
	default_val(args, 'start', '')

	final_text = args['start']
	final_text += str(args['sep']).join(text) + str(args['end'])
	if args.get('rtn', False):
		return final_text
	else:
		echo(final_text, sep='', end='')
