from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
                    ShoppingList, RecipeIngredient, Meals, connect_to_db, db)
from werkzeug import secure_filename

from sqlalchemy import func

import math

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
    print "SEARCH RECIPES"
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

@app.route("/importForm")
def getImportForm():

    return render_template("/import_form.html")

@app.route("/importRecipe")
def import_rec():


    pass

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

    print "PARAMS",date, meal_type, servings, recipe_id
    # import pdb;
    if 'User' in session:

        if not Meals.getMealByDateByRecipe(date, session['User'],recipe_id):
            print "Meal is not in planner"
            Meals.plan_meal(recipe_id, meal_type, servings, session["User"], date)
            db.session.commit()
        if request.args.get('flag') == 'planner':
            return redirect("/planner")  
        else:     
            return redirect("/recipes")
    else:
        flash = []
        flash = "You need to login"
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

    recipes = (db.session.query(Recipe).join(RecipeUser).\
            filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
            filter(RecipeUser.user_fk == session['User']).all())

    cuisine = (db.session.query(Recipe.cuisine).join(RecipeUser).\
            filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
            filter(RecipeUser.user_fk == session['User']).\
            filter(Recipe.cuisine != None).\
            distinct(Recipe.cuisine).order_by(Recipe.cuisine))

    categories = (db.session.query(Category).join(Recipe).join(RecipeUser).\
            filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
            filter(Recipe.cat_code == Category.cat_code).\
            filter(RecipeUser.user_fk == session['User']).\
            filter(Recipe.cat_code != None).\
            distinct().order_by(Recipe.cat_code))

    for i in range(7):
        week_days.append(int(start_date.strftime("%w")) + i)

    if 'User' in session:

        for i in range(7):
            mealsPlanned=''
            date = start_date + timedelta(days=i)
            # mealsPlanned = Meals.getMealsByDate(date, session['User'])
            b_meals = Meals.getMealsByDateByType(date, session['User'], 'breakfast')
            l_meals = Meals.getMealsByDateByType(date, session['User'], 'lunch')
            d_meals = Meals.getMealsByDateByType(date, session['User'], 'dinner')
            s_meals = Meals.getMealsByDateByType(date, session['User'], 'snack')
            # print "BREAKFAST",b_meals
            meal_list.append({"date": date,
                              "b_meals":b_meals,
                              "l_meals":l_meals,
                              "d_meals":d_meals,
                              "s_meals":s_meals})

        return render_template("planner.html", meals_list=meal_list,
            week_days=week_days, start_date=start_date, end_date=end_date,
            recipes=recipes, cuisine=cuisine, categories=categories)

    else:

        flash("You need to sign in")
        return render_template("planner.html")

@app.route("/getRecipeImg.json")
def getImg():

    recipe_id=request.args.get('recipeid')
    print "ID RICETTA",recipe_id
    rec = db.session.query(Recipe.image_url, Recipe.title).filter_by(recipe_id=recipe_id).all()
    print "IMG ", rec[0][0]
    
    recipe_info={
          
        'img_url': rec[0][0],
        'title' : rec[0][1]

        }

    return jsonify(recipe_info)

@app.route("/deleteMeal")
def deleteMeal():

    print "Delete MEAL"
    recipe_fk = request.args.get("recipeid")
    meal_type = request.args.get("mealtype")
    date_planned = request.args.get("dateplanned")

    print "RECIPE",recipe_fk, meal_type, date_planned


    Meals.deleteMeal(date=date_planned, user=session['User'], meal_type=meal_type,
             recipe=recipe_fk)

    db.session.commit()

    # except Exception, error:

    #     flash("Meal couldn't be deleted: error %s" % error)

    return redirect("/planner")

@app.route("/grocery")
def create_shopping_list():

    i_list = {}

    if 'User' in session:

        # meals = Meals.getMealsByFutureDate(user=session['User'])
        list_ingr = db.session.query(RecipeIngredient).join(Recipe).join(Meals).\
            join(Ingredient).\
            filter(func.substr(Meals.date_planned,0,11) >= func.substr(datetime.today(),0,11)).\
            filter(Meals.recipe_fk==Recipe.recipe_id).\
            filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
            filter(RecipeIngredient.ingredient_name==Ingredient.name).\
            filter(Meals.user_fk==session['User']).\
            order_by(Meals.date_planned).all()

        print "MEALS", list_ingr

        for ingr in list_ingr:

            qty = convertToInt(ingr.quantity)

            if ingr.ingredient_name not in i_list.keys():

                
                i_list[ingr.ingredient_name] = {"qty": qty,
                                                "unit":ingr.measure}

            else:

                to_add = { "qty": qty,"unit": ingr.measure }

                if ingr.measure and ingr.measure!='' \
                    and i_list[ingr.ingredient_name]['unit']!='':

                    new_value = calculateQuantity(i_list[ingr.ingredient_name],
                                                to_add, ingr.ingredient_name)
                    i_list[ingr.ingredient_name] = new_value

                else:

                    i_list[ingr.ingredient_name]['qty'] += qty

    print "LIST", i_list
    # ShoppingList.addItem(ingredient.id, recipeIngredient.qty, user, name)

    return render_template("grocery_list.html", list=i_list)

def calculateQuantity(old_qty, add_qty, ingr):
    print "CALCULATE QUANTITY", old_qty, add_qty, ingr
    new_value = {}

    qty1 = old_qty['qty']
    unit1 = old_qty['unit']

    qty2 = add_qty['qty']
    unit2 = add_qty['unit']

    new_qty = 0

# If the measure units are the same, it adds up the qty
    if unit1==unit2:

        new_qty = qty1 + qty2

        new_unit = unit1

#  If the measure units are not the same, it converts them to the lowest
#  unit and then it adds them up
    else:
        new_unit = compare(unit1, unit2)

        if unit1 != new_unit:

            qty1 = convert(qty1 , unit1, new_unit, ingr)
        else:
            qty2 = convert(qty2, unit2, new_unit, ingr)

        new_qty = qty1 + qty2

# Checks if the measure unit needs to be converted to the next greater one
    new_value = checkUnit(new_qty, new_unit, ingr)

    return new_value

def compare(unit1, unit2):

    new_unit = ''

    volume_measures = ['gallon', 'flounce', 'cup', 'tablespoon', 'teaspoon']
    weight_measures = ['pound', 'ounce', 'cup', 'tablespoon', 'teaspoon']

    if volume_measures.index(unit1) > volume_measures.index(unit2) or \
       weight_measures.index(unit1) > weight_measures.index(unit2):

       new_unit = unit2

    else:
        new_unit = unit1

    return new_unit 

def convert(qty, old_unit, new_unit, ingr):

    new_qty = qty

    # Unit of baking

    if old_unit == 'flounce':

        if new_qty == 'cup':
            new_qty == qty * 8

    # if old_unit == 'ounce':
    #     if new_qty == 'cup':
    #         new_qty == qty * 8

    if old_unit == 'cup':

        if new_unit == 'tablespoon':
            new_qty = qty * 16
        elif new_unit == 'teaspoon':
            new_qty = qty * 48

    elif old_unit == 'tablespoon' and new_unit == 'teaspoon':
        new_qty = qty * 3

    # Unit of volume
    if old_unit == 'gallon':

        if new_unit == 'cup':
            new_qty = qty * 16
        elif new_unit == 'tablespoon':
            new_qty = qty * 256
        elif new_qty == 'teaspoon':
            new_qty = qty * 768

    elif old_unit == 'cup':
        if new_unit == 'tablespoon':
            new_qty = qty * 16
        elif new_unit == 'teaspoon':
            new_qty = qty * 48

    elif old_unit == 'tablespoon':
        if new_unit == 'teaspoon':
            new_qty = qty * 3  

    # Unit of weight
    if old_unit == 'pound':
        if new_unit == 'ounce':
           new_qty = qty * 16  

        elif new_unit == 'cup' and ('flour') in ingr:
            new_qty = qty * 3.63  

    return new_qty

def checkUnit(t_qty, unit, ingr):

    max_n_tsp = 3
    max_n_tbls = 16
    max_n_ounces = 16
    max_n_flounces = 128
    max_n_flcup = 8
    max_n_cup_flour = 3.63
    max_n_cup_sugar = 3.75

    liquid = ['water', 'milk', 'extra-virgin olive oil']
    
    qty = t_qty
    unit = unit

    print "QUANTITY ", qty, t_qty, ingr, unit

    if unit == 'teaspoon' and qty > max_n_tsp:
        qty = math.ceil(qty / max_n_tsp)
        unit = 'tablespoon'

    elif unit == 'tablespoon' and qty > max_n_tbls:
        qty = math.ceil(qty / max_n_tbls)
        unit = 'cup'

    elif unit == 'ounce' and qty > max_n_ounces:
        qty = math.ceil(qty / max_n_ounces)
        unit = 'pound'

    elif unit == 'cup' and qty > max_n_flcup and ingr in liquid:
        qty = math.ceil(qty / max_n_flcup)
        unit = 'flounce'

    elif unit == 'flounce' and qty > max_n_flounces and ingr in liquid:
        qty = math.ceil(qty / max_n_flcup)
        unit = 'gallon'

    elif unit == 'cup' and qty > max_n_cup_flour and ingr.find('flour')!= -1 :
        qty = math.ceil(qty / max_n_cup_flour)
        unit = 'pound'

    elif unit == 'cup' and qty > max_n_cup_flour and ingr.find('sugar')!= -1 :
        qty = math.ceil(qty / max_n_cup_sugar)
        unit = 'pound'

    return {'qty': qty, 'unit':unit}

def convertToInt(stringNum):

    new_num = 0

    " ".join(stringNum.split())

    if stringNum.find('to')!= -1:

        l_range = stringNum.split('to')

        new_num = (int(l_range[0]) + int(l_range[1]))/2

    l_num = stringNum.split()

    for num in l_num:

        if num.find('/') != -1 :

            num_parts = num.split('/')

            new_num += int(num_parts[0])/int(num_parts[1])

        else: 
            print "NUM ", num
            print "NEW NUM ", new_num
            new_num += int(num)

    return  new_num

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