# -*- coding: utf-8 -*-

class Meta(type):
	def __new__(meta, name, bases, attrs):
		parent = type.__new__(meta, name , bases, {})
		for k, v in attrs.items():
			# print 'key: %s, \t\tvalue: %s ' %(k, v)
			if not k.startswith('__') and callable(v):
				print 'Not startswith __ and is callable'

		return type.__new__(meta, name, bases, attrs)