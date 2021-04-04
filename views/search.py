from flask import Blueprint, render_template, request, session
from models.ingredient import Ingredient

search_blueprint = Blueprint("search", __name__)


@search_blueprint.route("/", methods=["GET", "POST"])
def search_recipes():
	result_recipes = []
	
	# adding in null in case it's not there
	if "ingredients" not in session:
		session["ingredients"] = []
	
	# search initiated with button OR clearing previous searched ingredients
	if request.method == "POST":
		if "search" in request.form.values():
			ingredients_str = request.form["ingredients"]
			next_ingredients = list(set(ingredients_str.split(", ")))
			session["ingredients"] += next_ingredients
			result_recipes = Ingredient.find_matching_recipes(session["ingredients"])
			
		# clear session ingredients if click button
		elif "clear" in request.form.values():
			session["ingredients"] = []

	return render_template("search.html", result_recipes=result_recipes, searched_ingredients=session["ingredients"])
