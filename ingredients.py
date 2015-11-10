
import math
from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
                    ShoppingList, RecipeIngredient, Meals, connect_to_db, db)
from flask import session
from sqlalchemy import func
from datetime import datetime

class Ingredients(object):

    @classmethod
    def getListIngr(cls):

        """ Creates a list of ingredients for the recipes in the meal planner that have 
            a planned date greater than today's date

        """

        # meals = Meals.getMealsByFutureDate(user=session['User'])
        list_ingr = db.session.query(RecipeIngredient).join(Recipe).join(Meals).\
            join(Ingredient).\
            filter(func.substr(Meals.date_planned,0,11) >= func.substr(datetime.today(),0,11)).\
            filter(Meals.recipe_fk==Recipe.recipe_id).\
            filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
            filter(RecipeIngredient.ingredient_name==Ingredient.name).\
            filter(Meals.user_fk==session['User']).\
            order_by(Meals.date_planned).all()

        return list_ingr

    @classmethod
    def getListIngrName(cls):

        """ Creates a dictionary of ingredients for the recipes in the meal planner that have 
            a planned date greater than today's date.

            list_ingr = {aisle: [ingr1, ingr2, ...], ...}

        """

        # meals = Meals.getMealsByFutureDate(user=session['User'])
        list_ingr = db.session.query(RecipeIngredient).join(Recipe).join(Meals).\
            join(Ingredient).\
            filter(func.substr(Meals.date_planned,0,11) >= func.substr(datetime.today(),0,11)).\
            filter(Meals.recipe_fk==Recipe.recipe_id).\
            filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
            filter(RecipeIngredient.ingredient_name==Ingredient.name).\
            filter(Meals.user_fk==session['User']).\
            order_by(Ingredient.aisle).all()
            # order_by(Meals.date_planned).all()
        print "LIST INGREDIENT", list_ingr
        return list_ingr
    

    @classmethod    
    def makeShoppingListNoQty(cls,list_ingr):

        """ For each ingredient of the list_ingr it adds them to the shopping list
            if it is not in there already. It doesn't add up the quantities

            INPUT: list of ingredients names

        """

        i_list = {}

        unnecessary_items = ['water','salt']

        # for ingr in list_ingr:

        #     if ingr.ingredient_name not in i_list:

        #         i_list.append(ingr.ingredient_name)

        #         print "INGREDIENT", ingr.ingredient_name

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

    @classmethod    
    def makeShoppingListWithQty(cls,list_ingr):

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

    @classmethod
    def calculateQuantity(cls, old_qty, add_qty, ingr):

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


    @classmethod
    def compare(self, unit1, unit2):

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


    @classmethod
    def convert(self, qty, old_unit, new_unit, ingr):

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

    @classmethod
    def checkUnit(self, t_qty, unit, ingr):

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


    @classmethod
    def convertToInt(self, stringNum):

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
