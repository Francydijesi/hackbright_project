from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
            Expence, ShoppingList, RecipeIngredient, Meals, connect_to_db, db)
from werkzeug import secure_filename

from sqlalchemy import func

import math

import helpFunctions

import scraper

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


@app.route("/importRecipe", methods=['POST'])
def import_rec():

    url = request.form.get("url")
    user = ''

    print "URL ", url

    if 'User' in session:
        user = session['User']

    message = scraper.url_scraper(url, user)

    if message!= "Error":

        return redirect('/recipe_page/'+ str(message))

    else:

        flash = []
        flash = "Your recipe could not be loaded"
        return redirect('/addRecipesForm')

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

    json.loads(request.form.get("listIngr"))

    if 'Image' in request.files:

        img_file = request.files['Image']

    try:
        # Saves the img file in the directory
        filename=""

        if 'Image' in request.files:
            img_file = request.files['Image']

            print 'IMAGE' , img_file
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

@app.route("/search_by_ingr.json")
def search_by_ingr():

    """ Search recipes by ingredients """

    # Gets the values of the ingredient
    ingredient = request.args.get("ingredient")

    if 'User' in session:

        recipes = Recipe.getRecipeByIngrByUser(ingredient, session['User'])

    else:

        recipes = Recipe.getRecipeByIngrByUser(ingredient)

    print "RECIPES" , recipes
    # Creates a list of recipe in a json format
    list_of_recipe_dictionaries = [r.json() for r in recipes]

    # Creates a dictionary of jsonified recipes
    recipe_info = {
        'recipes': list_of_recipe_dictionaries
    }

    return jsonify(recipe_info)
   

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

@app.route("/create")
def create():

    ingredients = Ingredient.getAllIngredient()

    # return render_template('/create_recipe.html', ingredients=ingredients)
    return render_template("ingredients_graph.html")

@app.route('/miserables.json')
def createGraph():

    graph = helpFunctions.createGraph()       


    return jsonify(graph) 



@app.route("/createRecipe")
def generateRecipe():

    """ Generate a new recipe """

    ingredient = request.args.get("ingredient")

    print "INGREDIENT", ingredient

    # List of ingredients list, one for each recipe

    # recipe_lists = helpFunctions.getListIngredient()

    recipe_lists = RecipeIngredient.getAllMatchingRecipe(ingredient)


    # Gets a dictionary of matched ingredients for i 

    ingr_dict = helpFunctions.makeDict(ingredient, recipe_lists)

     


###############################################################################    
#                   MEAL PLANNER
###############################################################################

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

@app.route("/planner/<date>/<num>")
@app.route("/planner")
def getPlanner(date=None, num=None):

    """ Gets the list of meals planned """

    start_date = ''  

    # date = request.args.get('date')
    # num = request.args.get('operation') 

    print "Date", date


    if date and num =='-':


        start_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f') - timedelta(days=7)
        print "DATE", date, start_date

    elif date and num == '+':
        
        start_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f') + timedelta(days=7)

        print "DATE", date, start_date

    if not start_date:
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

# ##############################################################################
# # SHOPPING LIST : make a list - save a list
# ##############################################################################
# Make a list
@app.route("/grocery")
def create_shopping_list():

    i_ingr = []

    if 'User' in session:

        list_ingr = ShoppingList.getListIngrName(session['User'])

        i_ingr = helpFunctions.makeShoppingListNoQty(list_ingr)

    return render_template("grocery_list.html", list=i_ingr)

    # ShoppingList.addItem(ingredient.id, recipeIngredient.qty, user, name)

@app.route("/saveShoppingList", methods=["POST"])
def saveShoppingList():

    list_name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    ingr_aisles = request.form.get('list')

    list_ingredients = ingredients.split(",")

    print "TO SAVE ", list_name, ingredients, ingr_aisles

# Saves each ingredient in the shop_lists table
    for ingr in list_ingredients:

        ShoppingList.addItem(ingr, session['User'], list_name)

    db.session.commit    


    return redirect("/getShoppingLists/"+list_name)

@app.route("/getShoppingLists/<name>")
@app.route("/getShoppingLists")
def getShoppingList(name=None):

    print "VIEW SHOPPING LISTS"

    shop_list = ''
    all_names = ''
    i_list = {}
    date_created = ''

    if 'User' in session:

        if name:

            shop_list = ShoppingList.getShoppingListByName(name, session['User'])
            
        else:

            shop_list = ShoppingList.getLatestShoppingList(session['User'])
            if shop_list:
                name = shop_list[0].list_name
        
        print 'SHOP_LIST', shop_list

        if len(shop_list) > 0:

            date_created = shop_list[0].date_created

            all_names = ShoppingList.getShoppingListNames(session['User'])

            i_list = helpFunctions.makeShoppingList(shop_list)

            print "SHOPPING LIST",shop_list, date_created ,all_names  

        return render_template("view_shopping_list.html", list=i_list,
                    names=all_names, date_created=date_created, name=name )

    else:

        flash = []
        flash = "You need to login"
        return redirect("/login")

@app.route("/deleteShoppingList/")
def deleteShopList():

    name = request.args.get("lname")
    date_created = request.args.get("date")
    all_names = ''

    print "PARAMS", name, date_created

    if 'User' in session:

        if name is not None:

            ShoppingList.deleteShoppingList(name, session['User'], date_created)

        else:
            ShoppingList.deleteShoppingListByDate(session['User'], date_created)

        all_names = ShoppingList.getShoppingListNames(session['User'])

        print "NAMES", all_names

        # return render_template('display_shopping_list.html', names=all_names)
        return redirect ('/getShoppingLists')

    else:

        flash = []
        flash = "You need to login"
        return redirect("/login")

@app.route("/sendShoppingList", methods=['POST'])
def sendShoppingList():

    from twilio.rest import TwilioRestClient
 
    # Find these values at https://twilio.com/user/account
    # account_sid = "ACXXXXXXXXXXXXXXXXX"
    # auth_token = "YYYYYYYYYYYYYYYYYY"
    # client = TwilioRestClient(account_sid, auth_token)
    client = TwilioRestClient()

    name = request.form.get('listIng')

    if 'User' in session:
    
        shop_list = ShoppingList.getShoppingListByName(name, session['User'])
        i_list = helpFunctions.makeShoppingList(shop_list)

        print "SHOPP", shop_list

    else:

        flash = []
        flash = "You need to login"
        return redirect("/login")
    
    message = ''

    for aisle in i_list:
        
        message += '\n'+aisle.upper() + ':\n'

        message += '\n'.join(i_list[aisle])

    print "MESSAGE", message

    message = client.messages.create(to="+14156018298", from_="+16506810994",
                                     body=message)    

    return  redirect("/getShoppingLists")  

@app.route("/save-expence", methods=['POST'])
def saveExpence():

    date = request.form.get('date')
    store = request.form.get('store')
    total = request.form.get('sum')

    date_of_purchase = datetime.strptime(date,"%m/%d/%Y")

    Expence.addExpence(date=date_of_purchase, store=store, total=total, user=session['User'])  

    return redirect('/viewExpences')     

@app.route("/viewExpences")
def viewExpences():

    return render_template('/display_expences.html')

@app.route("/getExpences")

def getExpences():

    month = request.args.get('month')

    print "SET MONTH ", month
    current_month = datetime.today().strftime('%m')

    if not month:

        month = current_month

    else:

        month = int(current_month) - int(month)

        print "MONTH", month

    if 'User' in session:
        
        expences = Expence.getExpencesGroupedByDate(session['User'], month)

        expences_by_store = Expence.getExpencesByStore(session['User'], month)

        print 'EXPENCES', expences

        data_expences = helpFunctions.setDisplayData(expences, expences_by_store)

        print "DATA", data_expences

        return jsonify(data_expences)

    else:

        flash = []
        flash = "You need to login"
        return redirect("/login")

@app.route("/createBubbleGraph")
def createBubbleGraph():

    return render_template("ingredients_bubble_graph.html")


@app.route("/flare.json")
def createDataForGraph():

    """  It creates data in a json format for a Bubble graph """

    if 'User' in session:

        print "CREATE BUBBLE GRAPH"
    
        graph = helpFunctions.getAllShopListIngredients(session['User'])

        flare = { "name": "flare", "children": graph }

        print "GRAPH", flare
    
    return jsonify(flare)


   

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
    flash=[]
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

    # flash = []

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