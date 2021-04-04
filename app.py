import os
from flask import Flask
from views.home import home_blueprint
from views.recipes import recipe_blueprint
from views.search import search_blueprint
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(64)  # for cookies
# load_dotenv()

app.register_blueprint(home_blueprint)
app.register_blueprint(recipe_blueprint, url_prefix="/recipes")
app.register_blueprint(search_blueprint, url_prefix="/search")


if __name__ == "__main__":
    app.run(debug=True)
