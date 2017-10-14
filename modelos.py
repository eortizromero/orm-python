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
		print module_p
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

from collections import Mapping

class Reg(Mapping):
	def load(self, cr, mod):
		model_names = []
		for cls in OrmMetaModel\
			.mod_2_models.get(mod.name,[]):
			model = cls._buildmodel(self, cr)
			model_names.append(model._name)
	
	@classmethod
	def new(cls, db_name):
		registry = object.__new__(cls)
		registry.init(db_name)
		return registry

	def __len__(self):
		return len(self.models)

	def __getitem__(self, model_name):
		return self.models[model_name]

	def __iter__(self):
		return iter(self.models)

	def __call__(self, model_name):
		return self.models[model_name]

	def __setitem__(self, model_name, model):
		self.models[model_name] = model

	def init(self, db_name):
		self.models = {}
		self.db_name = db_name

cr = connect_db()

r = Reg()
r.new('ormdatabase')
r.load(cr, ['sale',])


# def load_mod_graph(cr, graph, status=None, per_checks\
# 	=True, skip_mod=None, report=None):
# 	r = Reg()
# 	for index, pack in enumerate(graph, 1):	
# 		model_names = r.load(cr, pack)
# 		print model_names

# def load_mod(db, force_demo=False, status=None, \
# 	update_modules=False):
	