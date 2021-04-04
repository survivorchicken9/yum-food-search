from flask import Blueprint, render_template, request

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		return render_template("search_results.html")
		
	return render_template("home.html")
