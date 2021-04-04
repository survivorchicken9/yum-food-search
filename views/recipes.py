from flask import Blueprint, render_template, request
from models.recipe import Recipe

recipe_blueprint = Blueprint("recipes", __name__)


@recipe_blueprint.route("/")
def index():
	recipes = Recipe.all()
	return render_template("recipes/index.html", recipes=recipes)


@recipe_blueprint.route("/new", methods=["GET", "POST"])
def new_recipe():
	if request.method == "POST":
		# getting form data
		name = request.form["name"]
		category = request.form["category"]
		description = request.form["description"]
		ingredients_str = request.form["ingredients"]
		ingredients = list(set(ingredients_str.split(", ")))
		
		# adding new recipe to database
		Recipe(name=name, category=category, description=description, ingredients=ingredients).save_to_mongo()
		
		# going back to all recipes page
		recipes = Recipe.all()
		return render_template("recipes/index.html", recipes=recipes)
		
	return render_template("recipes/new_recipe.html")
