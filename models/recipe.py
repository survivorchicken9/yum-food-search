from models.model import Model
from dataclasses import dataclass, field
import uuid


@dataclass(eq=False)
class Recipe(Model):
	collection: str = field(init=False, default="recipes")
	name: str
	category: str
	description: str
	ingredients: list
	_id: str = field(default_factory=lambda: uuid.uuid4().hex)  # unique string for MongoDB id (easy to use str)
	
	def json(self) -> dict:
		return {
			"_id": self._id,
			"name": self.name,
			"category": self.category,
			"description": self.description,
			"ingredients": self.ingredients
		}
