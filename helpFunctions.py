
import math
from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
                    ShoppingList, RecipeIngredient, Meals, connect_to_db, db)
from flask import session
from sqlalchemy import func
from datetime import datetime
from werkzeug import secure_filename

import os



################################################################################
#                               RECIPES                                        #
# Used to save recipes from form or from scraping                              #
################################################################################

# This is the path to the upload directory
UPLOAD_FOLDER = 'static/img/recipes/'

# These are the extension that we are accepting to be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def addRecipe(img_file, title, description, cat_code, servings,
             cooktime, skillLevel, cuisine, ingredients, steps, user):

    """ It adds a recipe, ingredients, recipe steps, recipe_user"""

    try:
        # Saves the img file in the directory
        filename = img_file

        print "IMG_FILE" ,img_file

        # If img is not from a website
        # if img_file and allowed_file(img_file.filename) and 'http' not in img_file:

        #     filename = secure_filename(img_file.filename)
            # print "FILENAME" , filename
            # img_file.save(os.path.join(UPLOAD_FOLDER, filename))

        # Add recipe in 'recipes' Table
        Recipe.addRecipe(title, description, filename, cat_code,
                 servings, cooktime, skillLevel,cuisine)

        # Finds the recipe_id
        recipeIds= db.session.query(func.max(Recipe.recipe_id)).one()
        recipeFk = recipeIds[0]
        print "RECIPE ID:  ",recipeFk

        # ingredients = ingredients
        print "INGREDIENTS LIST", ingredients

        for ingredient in ingredients:
            name = ingredient["name"]
            qty = ingredient["qty"]
            unit = ingredient["unit"]
            print "INGREDIENT UNICODE", ingredient

            # Add ingredients in 'RecipeIngredient'
            RecipeIngredient.addIngredients(recipeFk, name, qty, unit)
            # Add ingredients in 'Ingredients'
            Ingredient.addIngredients(name)


        for i in range(len(steps)):
            print "STEP%d" % i
            print "step value: ", steps[i]
            # Add steps in 'recipe_step'
            RecipeStep.addRecipeStep(recipeFk,i+1,steps[i])

        if 'User' in session:
            RecipeUser.addRecipeForUser(recipeFk,session['User'])

        db.session.commit()

        # Recipe.updateRecipeImg(title=title, cat_code=cat_code)

        message = {

            'msg': "Recipe successfully added",
            'recipeid': recipeFk
        }

        return recipeFk

    except Exception, error:
        return "Error: %s" % error

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


###############################################################################
#                         SHOPPING LIST 
# Used to diplay the shopping list already saved
###############################################################################

def makeShoppingList(list_ingr):

    """ For each ingredient of the list_ingr it adds them to the shopping list
        if it is not in there already. It doesn't add up the quantities

        INPUT: list of ingredients names
        OUTPUT: dictionary of ingredients: {'aisle1':[ingr1, ingr2,...],
                                            'aisle2':[ingr1, ingr2,...],
                                              ...
                                            }
    """

    i_list = {}

    unnecessary_items = ['water','salt']

    aisle = ''

    if list_ingr:


        for ingr in list_ingr:

            aisle = ingr.aisle


            if aisle is None:

                aisle = "Miscellaneous"

            if aisle not in i_list.keys():

                if ingr.name not in unnecessary_items:

                    i_list[aisle] = [ingr.name]

            else:

                if ingr.name not in i_list[aisle] and\
                    ingr.name not in unnecessary_items:

                    i_list[aisle].append(ingr.name)


    print "FINAL LIST:", i_list

    return i_list

###############################################################################
#                  SHOPPING LIST WITH NO QUANTITY 
# Used at the moment to generate a shopping list out of the meals in the planner
###############################################################################
 

def makeShoppingListNoQty(list_ingr):

    """ For each ingredient of the list_ingr it adds them to the shopping list
        if it is not in there already. It doesn't add up the quantities

        INPUT: list of ingredients names

        OUTPUT: dictionary of ingredients: {'aisle':[ingr1, ingr2,...],...}

    """

    i_list = {}

    unnecessary_items = ['water','salt']

    aisle = ''

    for ingr in list_ingr:

        if ingr.ingredient.aisle is None:

                ingr.ingredient.aisle = "Miscellaneous"

        if ingr.ingredient.aisle not in i_list.keys():

            if ingr.ingredient_name not in unnecessary_items:

                i_list[ingr.ingredient.aisle] = [ingr.ingredient_name]

        else:

            if ingr.ingredient_name not in i_list[ingr.ingredient.aisle] and\
                ingr.ingredient_name not in unnecessary_items:

                i_list[ingr.ingredient.aisle].append(ingr.ingredient_name)

    print "FINAL LIST:", i_list

    return i_list    

###############################################################################
#           SHOPPING LIST WITH QUANTITY - This functions are not used at the moment
###############################################################################
   
def makeShoppingListWithQty(list_ingr):

    """ For each ingredient of the list_ingr it adds them to the shopping list
        if it is not in there already. It adds their quantities.

        Input: list of ingredients

        Output: dictionary of ingredients: {ingredient1:{qty: , unit: },
                                            ...
                                            ingredient2:{qty: , unit: } }
    """

    i_list = {}

    notComparableUnits = ['pinch', 'clove']

    for ingr in list_ingr:

        # Converts string qty into int qty
        qty = convertToInt(ingr.quantity)

        # Creates a new ingredient element if it is not in the i_list dict.
        if ingr.ingredient_name not in i_list.keys():

            i_list[ingr.ingredient_name] = {"qty": qty,"unit":ingr.measure}

        # If ingredient is already in i_list, it updates its {qty, unit} value
        else:

            to_add = { "qty": qty,"unit": ingr.measure }


            #  If the ingredient has measure unit, compare and eventually
            # transforms the measure unit before adding the quantities

            if ingr.measure and ingr.measure!='' \
                or i_list[ingr.ingredient_name]['unit']!=''\
                or ingr.measure in notComparableUnits\
                or i_list[ingr.ingredient_name]['unit'] in notComparableUnits:

                new_value = calculateQuantity(i_list[ingr.ingredient_name],
                                            to_add, ingr.ingredient_name)

                i_list[ingr.ingredient_name] = new_value

            # If the ingredients don't have a measure units, it adds
            # the quantities

            else:

                i_list[ingr.ingredient_name]['qty'] += qty

    # ShoppingList.addItem(ingredient.id, recipeIngredient.qty, user, name)

    return i_list


def calculateQuantity(old_qty, add_qty, ingr):

    """ It gets two quantity with their measurement units.
        It compares the two measurement units:
        1. If they are the same, it adds the quantities
        2. If they are different, it converts the biggest to the lowest,
           transforms the quantities accordantly and adds them up.

        INPUT: two dictionaries like {qty: , unit:} associated to the same ingredient
        OUTPUT: a dictionari like new_value = {qty:, unit: } that represents the
        final qty and measure unit of the ingredient

        if old_qty = {'qty': 3, 'unit': tablespoon}  and
           add_qty = {'qty': 4, 'unit': tablespoon}

        return new_value = {'qty':7, 'unit': tablespoon}

        if old_qty = {'qty': 3, 'unit': tablespoon}  and
           add_qty = {'qty': 1, 'unit': cup}

        return new_value = {'qty': 19, 'unit': tablespoon}

    """


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

    """ It compares two measure units and returns the one that is smaller
        Example:

        If unit1='cup' and unit2='tablespoon'
        returns new_unit = 'tablespoon'

    """

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

    """ It converts the old measure units to the new measure units and
        converts the quantity in accordance, based on the type of ingredient

        It returns the quantity in the new measure unit

        Example:

            if qty = 2 and old_unit = cup and new_unit = tablespoon

            then new_qty = 32

    """

    new_qty = qty

    # Unit of baking

    if old_unit == 'flounce':

        if new_qty == 'cup':
            new_qty == qty * 8

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

    """ If the qty reaches the highest of its measure unit,
        it divides the qty by the highest value and changes the measure unit
        to the next higher one.

        example:

            if t_qty = 9 and unit = teaspoon

            then return {qty:3, unit:tablespoon}
    """

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

    """ It converts a string containing numeric information into a number

        Returns a number:

        Example:

            if stringNum = '3 1/2'

            returns 3.5

    """

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


##############################################################################
#          CREATE YOUR OWN RECIPE - This section has been removed from the APP
##############################################################################

def getListIngredient():

    all_ingr_list = []
    ingr_list = []

    ingredients = RecipeIngredient.getAllIngredients()

    recipe = ingredients[0].recipe_fk

    for ingr in ingredients:

        if ingr.recipe_fk == recipe:

            ingr_list.append(ingr.ingredient_name)

        else:    

            recipe = ingr.recipe_fk

            all_ingr_list.append(ingr_list)  

            ingr_list = [ingr.ingredient_name]

    print "ALL_LIST", all_ingr_list

    return all_ingr_list        


def makeDict(ingredient, recipe_lists, counter=0, seen=None):

    """
        It takes an ingredient and a list of recipe ingredients (recipe_lists)

        It returns a dictionary with all the ingredients (keys) that match the 

        given ingredient across all of the recipes in the recipe_lists and 

        their weight (value), sorted by value.

        The weight measure the number of times that ingredient is in combination

        with the given ingredient.

        OUTPUT: dictionary like { ingredient A: 5, ingredient B: 4, ... }

    """

    chains = {}

    counter += 1

    if not seen:
        seen= set()

    if ingredient not in seen:

        seen.add(ingredient)

    chains['name'] = ingredient
    chains['children']=[]

    for rec in recipe_lists:

        ingrs = RecipeIngredient.getAllIngredientsNamesByRecipe(rec.recipe_fk)

        for ingr in ingrs:

            if ingr[0] not in seen:
            # children = [s for s in ingrs if s not in seen]
                seen.add(ingr[0])

                chains['children'].append(ingr[0])

    print "chains",chains

    return chains


def makeDictMoreWords(ingredient_list, recipe_lists):

    """
        It takes an ingredient and a list of recipe ingredients (recipe_lists)

        It returns a dictionary with all the ingredients (keys) that match the 

        given ingredient across all of the recipes in the recipe_lists and 

        their weight (value), sorted by value.

        The weight measure the number of times that ingredient is in combination

        with the given ingredient.

        OUTPUT: dictionary like { ingredient A: 5, ingredient B: 4, ... }

    """

    chains = {}

    print "Ingredient", ingredient_list

    # Each ingrs is the set of ingredients of a single recipe

    for ingrs in recipe_lists: # for each set of ingredients for each recipe

        print "INGR. in LIST", ingrs

        # if ingredient in ingrs:

        for ingredient in ingredient_list:

            ingr_similar_words.append([s for s in ingrs if ingredient in s])

            if ingr_similar_words: # if the ingredient is in the recipe

                print "YES"

                for ingr in ingrs:  # its add all of ingr to the dict.

                    # for ingredient in ingr:

                    if ingr not in ingr_similar_words:

                        if ingr not in chains.keys():

                            chains[ingr] = 1

                        else:
                        
                            chains[ingr] += 1

    print "CHAINS", sorted(chains, key=chains.get, reverse=True)

    return sorted(chains, key=chains.get, reverse=True)  
 

################################################################################
#                   EXPENCES
###############################################################################

def setDisplayData(expences, expencesByStore):

    """ It takes two lists of expenses objects grouped by date and by stores.

        It returns a dictionary with data structured in a json format for 

        line graph and donut graph, and the month expenses are related to:

        {"data_by_week": data_by_week, "data_by_store": data_by_store, "month": month}

        where data_by_week = {'labels': label,'datasets': [ {graph_options}]}

        and data_by_store =[ { graph_options store 1}, ..., { graph_options store n}]
                    
    """

    label = []

    totals = []

    total_by_store = []

    stores = []

    somma = 0

    data_by_store = []

    data = {}

    month = []

    if expences:

        print "EXP", expences[0]

        current_week = expences[0].date_of_purchase.strftime('%W')
        current_month = expences[0].date_of_purchase.strftime('%B')
        month.append(current_month)


        for exp in expences:

            week = exp.date_of_purchase.strftime('%W')

            current_total = round(exp.total)

            if exp.date_of_purchase.strftime('%B') != current_month:

                month.append(exp.date_of_purchase.strftime('%B'))
                current_month = exp.date_of_purchase.strftime('%B')

            if week == current_week:

                somma += current_total

            else:

                label.append('week '+current_week)

                totals.append(somma)

                current_week = week

                somma = current_total

        label.append('week '+current_week)

        totals.append(somma)
      
        # Data structure for file chart

        data_by_week = {
            'labels': label,
            'datasets': [
                {
                    'label': "Weekly expenses",
                    'fillColor': "rgba(220,220,220,0.2)",
                    'strokeColor': "rgba(220,220,220,1)",
                    'pointColor': "rgba(220,220,220,1)",
                    'pointStrokeColor': "#fff",
                    'pointHighlightFill': "#fff",
                    'pointHighlightStroke': "rgba(220,220,220,1)",
                    'data': totals
                }
            ]
        }

        colors = ['#F7464A','#46BFBD', '#FDB45C']
        highlight = ['#FF5A5E', '#5AD3D1', '#FFC870']

        # Data structure for donut chart

        for i in range(len(expencesByStore)):

            data_by_store.append({
                    'value': round(expencesByStore[i][1]),
                    'color':colors[i],
                    'fillColor': colors[i],
                    'highlight': highlight[i],
                    'label': expencesByStore[i][0]
                })

        data = {"data_by_week": data_by_week, "data_by_store": data_by_store,
                "month": month}

    return data

################################################################################
#       BUBBLE GRAPH
################################################################################

def getAllShopListIngredients(user):

    """ It gets all the ingredients in the shopping lists saved """

    ingredients = ShoppingList.getAllIngredientsInShopList(user)

    graphData = makeJson(ingredients)

    return graphData  


def makeJson(ingredients):

    """ It gets a list of ingredients and returns a dictionary like :

    graphData = [
                    {
                       "name": "baking",
                       "children": [
                          {"name": "flour", "size": 3},
                          {"name": "tapioca", "size": 1},
                          {"name": "sugar", "size": 1},
                          {"name": "brown sugar", "size": 1}
                        ]
                    },
                    {
                        "name": "produce",
                        "children": [
                            {"name": "spinach", "size": 3},
                            {"name": "lettuce", "size": 2},
                            {"name": "potatoes", "size": 4},
                            {"name": "kale", "size": 5},
                            {"name": "apple", "size": 2}
                        ]
                    }
                ]  
    """

    graphData = []

    aisleDict = {}

    children = []

    childDic = {}

    unnecessary_items = ['water','salt']

    aisle = ''

    if ingredients:

        for ingr in ingredients:

            aisle = ingr[0]

            print "AISLE", aisle

            if aisle is None:

                aisle = "Miscellaneous"

            print "KEYS", aisleDict.keys()

            # If first time or aisle is new
            if not aisleDict.keys() or aisle != aisleDict['name']:

                # it appends the aisleDict to the list of dictionaries
                if childDic:

                    children.append(childDic)

                    aisleDict['children'] = children

                    graphData.append(aisleDict)

                    aisleDict = {}

                    children = []

                    childDic = {}

                aisleDict['name'] = aisle

            # It creates a new aisleDict
            if ingr[1] not in unnecessary_items:

                # aisleDict['name'] = aisle

                if not childDic or ingr[1] != childDic['name']:

                    if childDic:
                        children.append(childDic)
                        childDic = {}

                    childDic['name'] = ingr[1]
                    childDic['size'] = 1

                else:

                    childDic['size']+=1
        if childDic:

            children.append(childDic)

            aisleDict['children'] = children

            graphData.append(aisleDict)

    print "FINAL LIST:", graphData

    return graphData
