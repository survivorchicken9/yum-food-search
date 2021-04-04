from abc import ABCMeta, abstractmethod
from common.database import Database


class Model(metaclass=ABCMeta):
	"""
	Abstract class is defining a class that doesn't exist yet (template)
	i.e. can make it so that classes that inherit this model need to implement the abstract methods defined here
	"""
	# class properties - placeholders to force sub classes to implement as well
	collection: str
	_id: str
	
	def __init__(self, *args, **kwargs):
		pass
	
	def save_to_mongo(self):
		Database.upsert(collection=self.collection, query={"_id": self._id}, data=self.json())
		
	def remove_from_mongo(self):
		Database.remove(collection=self.collection, query={"_id": self._id})
	
	@abstractmethod
	def json(self):
		raise NotImplementedError

	@classmethod
	def all(cls):
		docs_in_db = Database.find(collection=cls.collection, query={})
		return [cls(**doc) for doc in docs_in_db]  # returns list of model objects

	@classmethod
	def find_one_by(cls, attribute, value):
		return cls(**Database.find_one(collection=cls.collection, query={attribute: value}))

	@classmethod
	def get_by_id(cls, _id: str):
		cls.find_one_by(attribute="id", value=_id)

	@classmethod
	def find_many_by(cls, attribute, value):
		return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
