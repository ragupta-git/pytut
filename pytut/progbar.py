
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: 2009 Nadia Alramli
# License: BSD
"""Draws an animated terminal progress bar
Usage:
	p = ProgressBar("blue")
	p.render(percentage, message)
"""
 
import terminal
import sys
 
class ProgressBar(object):
	"""Terminal progress bar class"""
	TEMPLATE = (
	 '%(percent)-2s%% %(color)s%(progress)s%(normal)s%(empty)s %(message)s\n'
	)
	PADDING = 7
 
	def __init__(self, color=None, width=None, block='X', empty=' '):
		"""
		color -- color name (BLUE GREEN CYAN RED MAGENTA YELLOW WHITE BLACK)
		width -- bar width (optinal)
		block -- progress display character (default 'X')
		empty -- bar display character (default ' ')
		"""
		if color:
			self.color = getattr(terminal, color.upper())
		else:
			self.color = ''
		if width and width < terminal.COLUMNS - self.PADDING:
			self.width = width
		else:
			# Adjust to the width of the terminal
			self.width = terminal.COLUMNS - self.PADDING
		self.block = block
		self.empty = empty
		self.progress = None
		self.lines = 0
 
	def render(self, percent, message = ''):
		"""Print the progress bar
		percent -- the progress percentage %
		message -- message string (optional)
		"""
		inline_msg_len = 0
		if message:
			# The length of the first line in the message
			inline_msg_len = len(message.splitlines()[0])
		if inline_msg_len + self.width + self.PADDING > terminal.COLUMNS:
			# The message is too long to fit in one line.
			# Adjust the bar width to fit.
			bar_width = terminal.COLUMNS - inline_msg_len -self.PADDING
		else:
			bar_width = self.width
 
		# Check if render is called for the first time
		if self.progress != None:
			self.clear()
		self.progress = (bar_width * percent) / 100
		data = self.TEMPLATE % {
			'percent': percent,
			'color': self.color,
			'progress': self.block * self.progress,
			'normal': terminal.NORMAL,
			'empty': self.empty * (bar_width - self.progress),
			'message': message
		}
		sys.stdout.write(data)
		sys.stdout.flush()
		# The number of lines printed
		self.lines = len(data.splitlines())
 
	def clear(self):
		"""Clear all printed lines"""
		sys.stdout.write(
			self.lines * (terminal.UP + terminal.BOL + terminal.CLEAR_EOL)
		)
		
import os, urllib2
from cStringIO import StringIO
from sys import stdout

class Progress(object):
	def __init__(self):
		self._seen = 0.0

	def update(self, total, size, name):
		self._seen += size
		#pct = (self._seen / total) * 100.0
		#print '%s progress: %.2f' % (name, pct)
		status = r"%10d  [%3.2f%%]" % (self._seen, self._seen * 100 / total)
		status = status + chr(8)*(len(status)+1)
		stdout.write("\r%s" % status)
		#stdout.flush()
		
class file_with_callback(file):
	def __init__(self, path, mode, callback, *args):
		file.__init__(self, path, mode)
		self.seek(0, os.SEEK_END)
		self._total = self.tell()
		self.seek(0)
		self._callback = callback
		self._args = args

	def __len__(self):
		return self._total

	def read(self, size):
		data = file.read(self, size)
		self._callback(self._total, len(data), *self._args)
		return data

progress = Progress()
path = r"C:\Users\ragupta4\Desktop\Rough\a.txt"
stream = file_with_callback(path, 'rb', progress.update, path)
print stream
print stream.read(8192)

