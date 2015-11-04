from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
                    RecipeIngredient, Meals, connect_to_db, db)
from werkzeug import secure_filename

from sqlalchemy import func
import os
import json

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'static/img/recipes/'

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():

    """Homepage."""

    return render_template("homepage.html")

@app.route("/recipes")
def recipe_list():

    """Show list of users."""

    # If user is logged in, search user's recipes.
    if 'user' in session:
        recipes = u.Recipe.query.all()

    # If user is not logged in, return all recipes
    else:
        recipes = Recipe.query.all()
        groupedrecipe = Recipe.query.group_by(Recipe.cat_code).group_by(Recipe.cuisine).all()
    print "GROUPED RECIPES :{}".format(groupedrecipe)
    # for cat in categories:    
    #     categories = (recipe.category.cat_name)
    categories = Category.query.distinct()

    print categories

    return render_template("recipe_list.html", recipes=groupedrecipe, categories=categories)

@app.route("/addRecipesForm")
def add_recipes():

    """ Get list of ingredients and return recipe form """

    ingredients = Ingredient.query.order_by("name").all()
    categories = Category.query.distinct()
    return render_template("recipe_form.html", ingredients=ingredients, categories=categories)

@app.route("/addRecipe.json", methods=['POST'])
def enter_recipe():
    """ Add a new recipe in DB """
    
    title = request.form.get("title")
    description = request.form.get("description")
    source = request.form.get("source")
    cat_code = request.form.get("category")
    cuisine = request.form.get("cuisine")
    servings = request.form.get("servings")
    cooktime = request.form.get("cookTime")
    skillLevel = request.form.get("level")
    step1 = request.form.get("step1")
    step2 = request.form.get("step2")
    step3 = request.form.get("step3")

    print "Title", title
    print "Description ", description
    print "Source ", source
    print "Category ", cat_code
    print "Cuisine ", cuisine
    print "Servings ", servings
    print "SkillLevel ", skillLevel

    # # Checks if the fields have a value and save it in a dictionary
    # args = {}

    # if title:
    #     args['title'] = title

    # if description:
    #     args['description'] = description

    # if source:
    #     args['source'] = source

    # if cat_code:
    #     args['cat_code'] = cat_code

    # if cuisine:
    #     args['cuisine'] = cuisine

    # if Servings:
    #     args['Servings'] = Servings

    # if skillLevel:
    #     args['skill_level'] = skillLevel

    try:
        # Saves the img file in the directory
        filename=""

        if 'Image' in request.files:
            img_file = request.files['Image']
            if img_file and allowed_file(img_file.filename):
                filename = secure_filename(img_file.filename)
                print filename
                img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Add recipe in 'recipes' Table 
        Recipe.addRecipe(title, description, filename, cat_code,
                 servings, cooktime, skillLevel)
        
        # Finds the recipe_id
        recipeIds= db.session.query(func.max(Recipe.recipe_id)).one()
        recipeFk = recipeIds[0]
        print "RECIPE ID:  ",recipeFk
     
        
        ingredients = json.loads(request.form.get("listIngr"))

        for ingredient in ingredients:
            name = ingredient["name"]
            qty = ingredient["qty"]
            unit = ingredient["unit"]
            
            # Add ingredients in 'RecipeIngredient'
            RecipeIngredient.addIngredients(recipeFk, name, qty, unit)
            # Add ingredients in 'Ingredients'
            Ingredient.addIngredients(name)
           
        # Add steps in 'recipe_step'
        RecipeStep.addRecipeStep(recipeFk,1,step1)
        RecipeStep.addRecipeStep(recipeFk,2,step2)
        RecipeStep.addRecipeStep(recipeFk,3,step3)

        db.session.commit()

        Recipe.updateRecipeImg(title=title, cat_code=cat_code)
        
        message = {

            'msg': "Recipe successfully added",
            'recipeid': recipeFk
        }

        return jsonify(message)

    except Exception, error:
        return "Error: %s" % error

# Enter the recipe in the recipes table


    # print("INGREDIENT: {}".format(type(ingredients)))
    # print("INGREDIENT NAME: {}".format(ingredients.name))


    # return jsonify({"data": "pluto"})
    

@app.route("/filtered_recipe.json")
def filteres_recipe():

    """ Search recipes by filters """

    # Gets the values of the filter
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    cat = request.args.get("cat")
    level = request.args.get("level")

    # Checks if the fields have a value and save it in a dictionary
    args = {}

    if title:
        args['title'] = title

    if cuisine:
        args['title'] = title

    if cat:
        args['cat_code'] = cat

    if level:
        args['skill_level'] = level

    # Execute the query and passes the values in the dictionary
    recipes = Recipe.query.filter_by(**args).all()

    # Creates a list of recipe in a json format
    list_of_recipe_dictionaries = [r.json() for r in recipes]

    # Creates a dictionary of jsonified recipes
    recipe_info = {
        'recipes': list_of_recipe_dictionaries
    }

    return jsonify(recipe_info)

@app.route("/recipe_page/<int:recipeid>")
def recipe_page(recipeid):

    """ Show recipe details """
    # print "RECIPE TYPE {}".format(type(recipeid))

    recipe = Recipe.query.filter_by(recipe_id=recipeid).first()

    ingredients = RecipeIngredient.query.filter_by(recipe_fk=recipeid)

    steps = RecipeStep.query.filter_by(recipe_fk=recipeid)

    return render_template("recipe_page.html", recipe=recipe,
                      ingredients=ingredients, steps=steps)


@app.route("/plan-meal")
def plan():

    """ Add a recipe to Meals """

    date = request.args.get("date")
    meal_type = request.args.get("type")
    servings = request.args.get("servings")
    recipe_id = request.args.get("recipeid")

    if 'user' in session:
        Meals.plan_meal(recipe_id, meal_type, servings, session["user"], date)
    else:
        Meals.plan_meal(recipe_id, meal_type, servings, None, date)

    db.session.commit()
    return redirect("/recipes")

# @app.route("/grocery")

# ##############################################################################
# # REGISTER - LOGIN - LOGOUT
# ##############################################################################
@app.route("/register")
def register_user():
    """Allows the user to sign up for an account"""

    return render_template("signup_form.html")

# @app.route("/register-confirm", methods=["POST"])
# def confirm_new_user():
#     """Create new user"""

#     user_email = request.form.get("email")
#     user_password = request.form.get("password") 
    
#     confirmed_user = User.get_user_by_email(user_email)
    
#     if not confirmed_user:
#         User.create_user_by_email_password(user_email, user_password)
#         flash("You successfully created an account!")
#     else:
#         flash("You already have an account")

#     return redirect("/")

# @app.route("/login")
# def login_user():
#     """Logs the user in"""

#     return render_template("login_form.html")

# @app.route("/logout")
# def logout_user():
#     """Logs out the user"""
#     del session['User']
    
#     flash("You are logged out","loggedout")

#     return redirect("/")    


# @app.route('/login_confirm', methods=["POST"])
# def get_login():
#     """Get user info"""
#     user_email = request.form.get("email")
#     user_password = request.form.get("password")
    
#     confirmed_user = User.get_user_by_email_password(user_email, user_password)
    
#     if confirmed_user:
#         flash("You're logged in!","loggedin")
#         userid = confirmed_user.user_id
#         session["User"] = userid

#         print session["User"]
#         return redirect("/")
#     else:
#         flash("Your email and password combination are not correct.")
#         return redirect("/login")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True)