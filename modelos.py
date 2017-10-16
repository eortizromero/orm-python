# -*- coding: utf-8 -*-

from sql.db import connect_db
import api
from collections import defaultdict

class OrmMetaModel(api.Meta):
	mod_2_models = defaultdict(list)
	def __init__(self, name, bases, attrs):
		if not hasattr(self, '_module'):
			self._module = \
				self._get_addon_name(self.__module__)
		self.mod_2_models[self._module].append(self)

		for k, v in attrs.iteritems():
			# print 'key: %s, \t\tvalue: %s ' %(k, v)
			pass

	def _get_addon_name(self, fullname):
		module_p = fullname.split('.')
		if len(module_p) > 2 and module_p[:2] == \
			['orm', 'plugins']:
			addon_name = fullname.split('.')[2]
		else:
			addon_name = fullname.split('.')[0]
		return addon_name

class OrmBaseModel(object):
	
	__metaclass__ = OrmMetaModel

	_name = None
	_description = None

	@classmethod
	def _buildmodel(cls, pool, cr):
		name = cls._name 
		description = cls._description

	@classmethod
	def _buildmodel_checkbase(model_class, cls):
		# print model_class._name
		pass

	def __new__(cls):
		return None

	def __init__(self, pool, cr):
		pass

OrmAbstractModel = OrmBaseModel


class Model(OrmAbstractModel):
	_auto = True


class usuario(Model):
	_name = 'usuario.model'
	_description = 'description model'


