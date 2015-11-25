from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
            Expence, ShoppingList, RecipeIngredient, Meals, connect_to_db, db)

from werkzeug import secure_filename

from sqlalchemy import func

from datetime import datetime, timedelta

from validate_email import validate_email

import math, helpFunctions, scraper, os, json, re


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

# To validate email format
EMAIL_RE = re.compile("(\w+)\@(\w+\.com)")

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

############################## HOMEPAGE ########################################

@app.route('/')
def index():

    """Homepage."""

    return render_template("homepage.html")


############################## RECIPE VIEW #####################################

@app.route("/recipes")
def recipe_list():

    """ It searches all the Recipes:

        Returns: list of recipes (list of objects)
                 list of cuisine (list of strings)
                 list of sources (list of strings)
                 list of categories (list of strings)
                 list of levels (list of strings)
    """  

    # If user is logged in, search user's recipes.
    if 'User' in session:

        recipes = Recipe.getRecipesByUser(session['User'])
 
        cuisine = Recipe.getCuisineForRecipesByUser(session['User'])
        
        sources = Recipe.getSourceForRecipesByUser(session['User'])
        
        categories = Recipe.getCatForRecipesByUser(session['User'])

        levels = Recipe.getLevelsForRecipesByUser(session['User'])

    # If user is not logged in, return all recipes
    else:

        recipes = Recipe.getAllRecipes()
 
        cuisine = Recipe.getCuisineForRecipesByUser()
        
        sources = Recipe.getSourceForRecipesByUser()
        
        categories = Recipe.getCatForRecipesByUser()

        levels = Recipe.getLevelsForRecipesByUser()
        

    return render_template("recipe_list.html", recipes=recipes, levels=levels,
                            cuisine=cuisine, sources=sources, categories=categories)



@app.route("/changeFilters.json", methods=['POST'])
def change_filters():

    """ It searches recipes by filters.

        Gets a lists of filters.

        Returns: list of recipes (list of objects)
                 list of cuisine (list of strings)
                 list of sources (list of strings)
                 list of categories (list of strings)
                 list of levels (list of strings
    """
    # Saves the parameters
    title = request.form("title")
    cuisine = request.form("cuisine")
    level = request.form("level")
    cat = request.form("cat")
    source = request.form("source")


    # Checks if the fields have a value and save them in a dictionary
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
   
    # Calls the db functions to get lists of cuisine, sources, categories, titles
    cuisine = Recipe.getCuisineByFilter(**args)

    sources = Recipe.getSourcesByFilter(**args)

    categories = Recipe.getCatByFilter(**args)

    levels = Recipe.getLevelsByFilter(**args)

    titles = Recipe.getTitlesByFilter(**args)

    # Puts the data in a json format
    filters = {

       "cuisine": cuisine,
       "source" : sources,
       "categories": categories,
       "levels" : levels,
       "titles" : titles
    }

    return jsonify(filters)


@app.route("/search_by_ingr.json")
def search_by_ingr():

    """ Search recipes by ingredients """

    # Gets the values of the ingredient
    ingredient = request.args.get("ingredient")

    if 'User' in session:

        recipes = Recipe.getRecipeByIngrByUser(ingredient, session['User'])

    else:

        recipes = Recipe.getRecipeByIngrByUser(ingredient)

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


############################## RECIPE IMPORT ##################################

@app.route("/importForm")
def getImportForm():

    return render_template("/import_form.html")


@app.route("/importRecipe", methods=['POST'])
def import_rec():

    """ It scrapes recipe from a url 

        If successfull redirects to recipe_page

        If not successfull redirects to form with an error message

    """

    url = request.form.get("url")
    user = ''

    if 'User' in session:
        user = session['User']

    message = scraper.url_scraper(url, user)

    if type(message)== int:

        return redirect('/recipe_page/'+ str(message))

    else:

        flash = "Your recipe could not be loaded"
        return redirect('/addRecipesForm/'+message)


@app.route("/addRecipesForm/<message>")
@app.route("/addRecipesForm")
def add_recipes(message=None):

    """ Get list of categories for recipe form """

    # ingredients = Ingredient.query.order_by("name").all()
    categories = Category.query.distinct().order_by("cat_name")
    
    return render_template("recipe_form.html", categories=categories, msg=message)


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
    steps = [step1, step2, step3]

    # json.loads(request.form.get("listIngr"))
    ingredients = json.loads(request.form.get("listIngr"))


    img_file = ''
    user = ''

    if 'User' in session:

        user = session['User']

    if 'Image' in request.files:

        img_file = request.files['Image']

    value = helpFunctions.addRecipe(img_file, title, description, cat_code, servings,
             cooktime, skillLevel, cuisine, ingredients, steps, user)

    
    if  type(value) == int:

        message = {

            'msg': "Recipe successfully added",
            'recipeid': value
        }

    else:

        message = {

            'msg': value
        }

    return jsonify(message)

############################ RECIPE PAGE #####################################

@app.route("/recipe_page/<int:recipeid>")
def recipe_page(recipeid):

    """ Show recipe details """

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

# @app.route("/create")
# def create():

#     ingredients = Ingredient.getAllIngredient()

#     # return render_template('/create_recipe.html', ingredients=ingredients)
#     return render_template("ingredients_graph.html")

# @app.route('/miserables.json')
# def createGraph():

#     graph = helpFunctions.createGraph()       


#     return jsonify(graph) 



# @app.route("/createRecipe")
# def generateRecipe():

#     """ Generate a new recipe """

#     ingredient = request.args.get("ingredient")

#     print "INGREDIENT", ingredient

#     # List of ingredients list, one for each recipe

#     # recipe_lists = helpFunctions.getListIngredient()

#     recipe_lists = RecipeIngredient.getAllMatchingRecipe(ingredient)


#     # Gets a dictionary of matched ingredients for i 

#     ingr_dict = helpFunctions.makeDict(ingredient, recipe_lists)

     


###############################################################################    
#                                MEAL PLANNER
###############################################################################

@app.route("/plan-meal")
def plan():

    """ Add a recipe to Meals """

    date = request.args.get("date")
    meal_type = request.args.get("type")
    servings = request.args.get("servings")
    recipe_id = request.args.get("recipeid")

    # import pdb;
    if 'User' in session:

        if not Meals.getMealByDateByRecipe(date, session['User'],recipe_id):
            
            Meals.plan_meal(recipe_id, meal_type, servings, session["User"], date)
            db.session.commit()
        
        if request.args.get('flag') == 'planner':           
            return redirect("/planner")         
        else:                 
            return redirect("/recipes")
    else:
        
        flash = []
        flash = "You need to login"
        return redirect("/error.html",url="/planner")


@app.route("/planner/<date>/<num>")
@app.route("/planner")
def getPlanner(date=None, num=None):

    """ Gets the list of meals planned """

    start_date = ''  

    # It sets the START DATE. 
    if date and num =='-':

        start_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f') - timedelta(days=7)

    elif date and num == '+':
        
        start_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f') + timedelta(days=7)

    if not start_date:
        start_date = datetime.today()

    # It sets the END DATE 
    end_date = start_date + timedelta(days=7)
    currentWeek = start_date.strftime("%W")
    
    week_days = []
    meal_list = []
    meal_days = []

    if 'User' in session:

        recipes = Recipe.getRecipesByUser(session['User'])

        cuisine = Recipe.getCuisineForRecipesByUser(session['User'])

        categories = Recipe.getCatForRecipesByUser(session['User'])

        for i in range(7):
            week_days.append(int(start_date.strftime("%w")) + i)

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

        print 'DATA', date
        return render_template("planner.html", meals_list=meal_list,
            week_days=week_days, start_date=start_date, end_date=end_date,
            recipes=recipes, cuisine=cuisine, categories=categories)

    else:

        flash("You need to sign in")
        return render_template("error.html",url="/planner")

@app.route("/getRecipeImg.json")
def getImg():

    recipe_id=request.args.get('recipeid')
    
    rec = db.session.query(Recipe.image_url, Recipe.title).filter_by(recipe_id=recipe_id).all()
    
    recipe_info={
          
        'img_url': rec[0][0],
        'title' : rec[0][1]

        }

    return jsonify(recipe_info)

@app.route("/deleteMeal")
def deleteMeal():
    
    recipe_fk = request.args.get("recipeid")
    meal_type = request.args.get("mealtype")
    date_planned = request.args.get("dateplanned")

    Meals.deleteMeal(date=date_planned, user=session['User'], meal_type=meal_type,
             recipe=recipe_fk)

    db.session.commit()


    return redirect("/planner")

# ##############################################################################
# #                        SHOPPING LIST : make a list - save a list
# ##############################################################################
# Make a list
@app.route("/grocery/<name>")
def create_shopping_list(name):
    """ 
        It creates a shopping list with the ingredients for the recipes
        in the meal planner and returns it in a dictionary  :
        {'aisle':[ingr1, ingr2,...],...}

    """
    print name
 
    i_ingr = []

    if 'User' in session:

        list_ingr = ShoppingList.getListIngrName(session['User'])

        dict_ingr = helpFunctions.makeShoppingListNoQty(list_ingr)

    return render_template("grocery_list.html", list=dict_ingr, name=name)


@app.route("/saveShoppingList", methods=["POST"])
def saveShoppingList():

    """ 
        It saves the shopping list with the ingredients for the recipes in the planner

    """

    list_name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    ingr_aisles = request.form.get('list')

    list_ingredients = ingredients.split(",")


    # Saves each ingredient in the shop_lists table
    for ingr in list_ingredients:

        ShoppingList.addItem(ingr, session['User'], list_name)

    db.session.commit    

    return redirect("/getShoppingLists/"+list_name)


@app.route("/getShoppingLists/<name>")
@app.route("/getShoppingLists")
def getShoppingList(name=None):

    """ It searches a shopping list by name or finds the latest saved"""

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
        

        if len(shop_list) > 0:

            date_created = shop_list[0].date_created

            all_names = ShoppingList.getShoppingListNames(session['User'])

            i_list = helpFunctions.makeShoppingList(shop_list)


        return render_template("view_shopping_list.html", list=i_list,
                    names=all_names, date_created=date_created, name=name )

    else:

        flash = []
        flash = "You need to login"
        return render_template("/error.html", url="/getShoppingLists")


@app.route("/deleteShoppingList/")
def deleteShopList():

    """ It deletes the shopping list by name """

    name = request.args.get("lname")
    date_created = request.args.get("date")
    all_names = ''

    if 'User' in session:

        if name is not None:

            ShoppingList.deleteShoppingList(name, session['User'], date_created)

        else:
            
            ShoppingList.deleteShoppingListByDate(session['User'], date_created)

        
        all_names = ShoppingList.getShoppingListNames(session['User'])

        return redirect ('/getShoppingLists')

    else:

        flash = []
        flash = "You need to login"
        return render_template("/error.html",url="homepage.html")


@app.route("/sendShoppingList", methods=['POST'])
def sendShoppingList():

    """ It sends the shopping list by SMS with Twilio API """

    from twilio.rest import TwilioRestClient
 
    client = TwilioRestClient()

    name = request.form.get('listIng')

    # It finds the shopping list by name and creates a dictionary of ingredients
    #  and aisle
    if 'User' in session:
    
        shop_list = ShoppingList.getShoppingListByName(name, session['User'])
        i_list = helpFunctions.makeShoppingList(shop_list)

    else:

        flash = []
        flash = "You need to login"
        return render_template("/error.html", url="homepage.html")
    
    message = ''

    # It creates a string message with all the ingredients and aisles

    for aisle in i_list:
        
        message += '\n'+aisle.upper() + ':\n'

        message += '\n'.join(i_list[aisle])


    message = client.messages.create(to="+14156018298", from_="+16506810994",
                                     body=message)    

    return  redirect("/getShoppingLists")  



################################################################################
#                          EXPENSES
################################################################################    

@app.route("/save-expence", methods=['POST'])
def saveExpence():

    """ It saves the expenses added in a form """

    date = request.form.get('date')
    store = request.form.get('store')
    total = request.form.get('sum')

    date_of_purchase = datetime.strptime(date,"%m/%d/%Y")

    Expence.addExpence(date=date_of_purchase, store=store, total=total, user=session['User'])  

    return redirect('/viewExpences')     

@app.route("/viewExpences")
def viewExpences():

    if 'User' in session:

        return render_template('/display_expences.html')

    else:

        return render_template('error.html', url='/display_expences.html')


@app.route("/getExpences")
def getExpences():

    """ 
        It gets all the expenses by week and by store for the current month
        or for the past 2 or 3 months if the parameter 'month' is passed
    """

    month = request.args.get('month')

    current_month = datetime.today().strftime('%m')

    print "MONTH PARAM", month

    if not month:

        month = current_month

    else:

        month = int(current_month) - int(month)

    print "MONTH", month
    if 'User' in session:
        
        expences = Expence.getExpencesGroupedByDate(session['User'], month)

        expences_by_store = Expence.getExpencesByStore(session['User'], month)

        data_expences = helpFunctions.setDisplayData(expences, expences_by_store)

        return jsonify(data_expences)

    else:

        flash = []
        flash = "You need to login"
        return render_template("error.html")

################################################################################
#                   INGREDIENT BUBBLE GRAPH
###############################################################################        

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

    else:
        return render_template("error.html")
    
    return jsonify(flare)
   

# ##############################################################################
#   REGISTER - LOGIN - LOGOUT
# ##############################################################################

# @app.route("/register")
# def register_user():
#     """Allows the user to sign up for an account"""

#     return render_template("signup.html")

@app.route("/register-confirm", methods=["POST"])
def confirm_new_user():
    """Creates new user"""

    # flash=[]
    # It gets email and password from the POST param
    user_email = request.form.get("email")

    user_password = request.form.get("password")

    #It checks if user already exists or email is invalid
    confirmed_user = User.get_user_by_email(user_email)

    # is_valid = validate_email(user_email,verify=True)

    # EMAIL_RE.search(user_email)
    if True:

        if not confirmed_user:
            User.create_user_by_email_password(user_email, user_password)
            flash("You successfully created an account!")
        else:
            flash("You already have an account")
            return render_template('error.html',url='homepage.html')

    else:
        flash("The email that you entered is invalid")
        # return render_template('error.html',url='homepage.html')

    return render_template('error.html',url='homepage.html')

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

    user_email = request.form.get("email")
    user_password = request.form.get("password")

    confirmed_user = User.get_user_by_email_password(user_email, user_password)

    flash = []

    if confirmed_user:
        # flash("You're logged in!","loggedin")
        userid = confirmed_user.user_id
        session["User"] = confirmed_user.user_id

        print session["User"]
        return redirect("/")
    else:
        flash = "Your email and password combination are not correct."
        return render_template("error.html",url='homepage.html')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True)