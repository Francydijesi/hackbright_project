from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
                    RecipeIngredient, Meals, connect_to_db, db)
from werkzeug import secure_filename

from sqlalchemy import func

from datetime import datetime
from datetime import timedelta

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
    print "BACK IN TOWN"
    # If user is logged in, search user's recipes.
    if 'User' in session:
        # u_recipes = RecipeUser.query.filter_by(session['User']).all()
        recipes = (db.session.query(Recipe).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(RecipeUser.user_fk == session['User']).all())
 
        cuisine = (db.session.query(Recipe.cuisine).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(RecipeUser.user_fk == session['User']).\
                    filter(Recipe.cuisine != None).\
                    distinct(Recipe.cuisine).order_by(Recipe.cuisine))

        sources = (db.session.query(Recipe.source).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(RecipeUser.user_fk == session['User']).\
                    filter(Recipe.source != None).\
                    distinct().order_by(Recipe.source))
        
        categories = (db.session.query(Category).join(Recipe).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(Recipe.cat_code == Category.cat_code).\
                    filter(RecipeUser.user_fk == session['User']).\
                    filter(Recipe.cat_code != None).\
                    distinct().order_by(Recipe.cat_code))

        levels = (db.session.query(Recipe.skill_level).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(RecipeUser.user_fk == session['User']).\
                    filter(Recipe.skill_level != None).\
                    distinct(Recipe.skill_level))

    # If user is not logged in, return all recipes
    else:
        # recipes = Recipe.query.all()
        recipes = Recipe.query.group_by(Recipe.cat_code).order_by(Recipe.cat_code).all()

        cuisine = (db.session.query(Recipe.cuisine).\
                    filter(Recipe.cuisine != None).\
                    distinct().order_by(Recipe.cuisine))

        sources = (db.session.query(Recipe.source).\
                    filter(Recipe.source != None).\
                    distinct().order_by(Recipe.source))

        categories = db.session.query(Category).join(Recipe).\
                    filter(Category.cat_code == Recipe.cat_code).\
                    filter(Recipe.cat_code != None).distinct().order_by(Recipe.cat_code)  

        levels = (db.session.query(Recipe.skill_level).\
                    filter(Recipe.skill_level != None).\
                    distinct())

    return render_template("recipe_list.html", recipes=recipes, levels=levels,
                            cuisine=cuisine, sources=sources, categories=categories)

@app.route("/changeFilters.json", methods=['POST'])
def change_filters():

    title = request.form("title")
    cuisine = request.form("cuisine")
    level = request.form("level")
    cat = request.form("cat")
    source = request.form("source")


    # Checks if the fields have a value and save it in a dictionary
    args = {}

    if title:
        args['title'] = title

    if cuisine:
        args['cuisine'] = cuisine

    if cat:
        args['cat_code'] = cat

    if level:
        args['skill_level'] = level

    if source:
        args['source'] = source

    cuisine = db.session.query(Recipe.cuisine).\
                filter_by(**args).\
                filter(Recipe.cuisine != None).\
                distinct().order_by(Recipe.cuisine)

    sources = (db.session.query(Recipe.source).\
                filter_by(**args).\
                filter(Recipe.source != None).\
                distinct().order_by(Recipe.source))

    categories = db.session.query(Category).join(Recipe).\
                filter_by(**args).\
                filter(Category.cat_code == Recipe.cat_code).\
                filter(Recipe.cat_code != None).distinct().order_by(Recipe.cat_code)  

    levels = (db.session.query(Recipe.skill_level).\
                filter_by(**args).\
                filter(Recipe.skill_level != None).\
                distinct())

    titles = db.session.query(Recipe.title).\
                filter_by(**args).\
                filter(Recipe.title != None).\
                distinct().order_by(Recipe.title)

    filters = {

       "cuisine": cuisine,
       "source" : sources,
       "categories": categories,
       "levels" : levels,
       "titles" : titles
    }

    return jsonify(filters)


@app.route("/addRecipesForm")
def add_recipes():

    """ Get list of ingredients and return recipe form """

    ingredients = Ingredient.query.order_by("name").all()
    categories = Category.query.distinct().order_by("cat_name")
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
                 servings, cooktime, skillLevel,cuisine)
        
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

        if 'User' in session:
            RecipeUser.addRecipeForUser(recipeFk,session['User'])

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
    source = request.args.get("source")

    print "Title", title
    print "Source ", source
    print "Category ", cat
    print "Cuisine ", cuisine
    print "SkillLevel ", level

    # Checks if the fields have a value and save it in a dictionary
    args = {}

    if title:
        args['title'] = title

    if cuisine:
        args['cuisine'] = cuisine

    if cat:
        args['cat_code'] = cat

    if level:
        args['skill_level'] = level

    if source:
        args['source'] = source

    print "CUISINE", cuisine

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

@app.route("/deleteRecipe/<int:recipeid>")
def delete_recipe(recipeid):

    Recipe.deleteRecipeById(recipeid)
    db.session.commit()

    return redirect ("/recipes")

@app.route("/plan-meal")
def plan():

    """ Add a recipe to Meals """

    date = request.args.get("date")
    meal_type = request.args.get("type")
    servings = request.args.get("servings")
    recipe_id = request.args.get("recipeid")

    if 'User' in session:
        Meals.plan_meal(recipe_id, meal_type, servings, session["User"], date)
        db.session.commit()
        return redirect("/recipes")
    else:
        # Meals.plan_meal(recipe_id, meal_type, servings, None, date)
        flash=[]
        flash="You need to login"
        return redirect("/login")
    
    

@app.route("/planner")
def getPlanner():

    """ Gets the list of meals planned """

    start_date = datetime.today()
    end_date = start_date + timedelta(days=7)
    currentWeek = start_date.strftime("%W")
    week_days = []
    meal_list = []
    meal_days = []

    for i in range(7):
        week_days.append(int(start_date.strftime("%w")) + i)

    if 'User' in session:

        for i in range(7):

            date = start_date + timedelta(days=i)
            mealsPlanned = Meals.getMealsByDate(date, session['User'])
            meal_list.append({"date": date, "meals":mealsPlanned})


        return render_template("planner.html", meals_list=meal_list,
            week_days=week_days, start_date=start_date, end_date=end_date)

    else:

        flash("You need to sign in")
        return render_template("planner.html")



# @app.route("/grocery")

# ##############################################################################
# # REGISTER - LOGIN - LOGOUT
# ##############################################################################
@app.route("/register")
def register_user():
    """Allows the user to sign up for an account"""

    return render_template("signup.html")

@app.route("/register-confirm", methods=["POST"])
def confirm_new_user():
    """Create new user"""
    print("\n\n\n\n\nUSER CONFIRM\n\n\n\n")
    user_email = request.form.get("email")
    user_password = request.form.get("password") 

    confirmed_user = User.get_user_by_email(user_email)
    
    print "USER",confirmed_user
    if not confirmed_user:
        User.create_user_by_email_password(user_email, user_password)
        flash("You successfully created an account!")
    else:
        flash("You already have an account")

    return redirect("/")

@app.route("/login")
def login_user():
    """Logs the user in"""

    return render_template("login.html")

@app.route("/logout")
def logout_user():
    """Logs out the user"""
    del session['User']
    
    flash("You are logged out","loggedout")

    return redirect("/")    


@app.route('/login_confirm', methods=["POST"])
def get_login():
    """Get user info"""
    print "LOGIN CONFIRM"
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    
    confirmed_user = User.get_user_by_email_password(user_email, user_password)
    print "USER: ", confirmed_user

    if confirmed_user:
        flash("You're logged in!","loggedin")
        userid = confirmed_user.user_id
        session["User"] = confirmed_user.user_id

        print session["User"]
        return redirect("/")
    else:
        flash("Your email and password combination are not correct.")
        return redirect("/login")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True)