from common.database import Database
from models.model import Model
from dataclasses import dataclass, field
import uuid


@dataclass(eq=False)
class Ingredient(Model):
	collection: str = field(init=False, default="ingredients")
	name: str
	category: str
	description: str
	_id: str = field(default_factory=lambda: uuid.uuid4().hex)  # unique string for MongoDB id (easy to use str)
	
	def json(self) -> dict:
		return {
			"_id": self._id,
			"name": self.name,
			"category": self.category,
			"description": self.description
		}
	
	@staticmethod
	def find_matching_recipes(ingredients_to_match: list) -> list:
		"""
		Look for recipes that include this ingredient
		:return: matching_recipes -> list of dictionaries of each found recipe
		"""
		matching_recipes = Database.find(collection="recipes", query={"ingredients": {"$all": ingredients_to_match}})
		return matching_recipes
