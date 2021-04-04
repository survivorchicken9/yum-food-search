from dotenv import load_dotenv
import pymongo
import os


class Database:
	"""
	collection: name of collection in database to perform operations
	data: (new) document to insert or update in collection
	query: selection criteria for search or update in collection (if empty means search for all)
	pymongo.cursor: iterable object in Python
	"""
	load_dotenv()
	DATABASE = pymongo.MongoClient(os.environ.get("MONGO_CONN")).food

	@staticmethod
	def insert(collection: str, data: dict) -> None:
		Database.DATABASE[collection].insert(data)
	
	@staticmethod
	def find(collection: str, query: dict) -> pymongo.cursor:
		return Database.DATABASE[collection].find(query)
	
	@staticmethod
	def find_one(collection: str, query: dict) -> dict:
		return Database.DATABASE[collection].find_one(query)
	
	@staticmethod
	def upsert(collection: str, query: dict, data: dict) -> None:
		Database.DATABASE[collection].update(query, data, upsert=True)  # update or insert
	
	@staticmethod
	def remove(collection: str, query: dict) -> dict:
		return Database.DATABASE[collection].remove(query)
