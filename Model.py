"""Models and database functions for Food Planner project."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from sqlalchemy import func, Numeric
from sqlalchemy.sql.expression import cast

db = SQLAlchemy()


##############################################################################
##################### Model definitions ######################################

### USER ###

class User(db.Model):
    """ List of Users """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    name =db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(15), nullable=True)
    name =db.Column(db.String(50), nullable=True)
    zipcode =db.Column(db.Integer, nullable=True)


    @classmethod
    def get_user_by_email_password(cls, user_email, user_password):

        try:
            user_login_info = cls.query.filter_by(email=user_email, password=user_password).one()
            return user_login_info

        except Exception, error:
            print error

    @classmethod
    def get_user_by_email(cls, user_email):
        
        try:
            user_login_info = cls.query.filter_by(email=user_email).one()
            print "LOGIN", user_login_info
            return user_login_info
        
        except Exception, error:
            print error

    @classmethod
    def create_user_by_email_password(cls, user_email, user_password):

        user = User(email = user_email, password = user_password)
        print user
        db.session.add(user)
        db.session.commit()

    def __repr__(self):
        """ User profile """

        return "<User user_id= %s name=%s email=%s >" % ( self.user_id, self.name, self.email)    


##############################################################################
#
### RECIPES ###

class Recipe(db.Model):
    """ Recipes list """

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)
    cat_code = db.Column(db.String(50), db.ForeignKey('categories.cat_code'))
    cuisine = db.Column(db.String(50), nullable=True)
    calories = db.Column(db.Integer, nullable=True)
    source = db.Column(db.String(50), nullable=True)
    rate = db.Column(db.String(20), nullable=True)
    servings = db.Column(db.Integer, nullable=True)
    cook_time = db.Column(db.String(50), nullable=True)
    skill_level = db.Column(db.String(2), nullable=True)
    
    # Define relationship to categorie
    category = db.relationship("Category",
                           backref=db.backref("recipes", order_by=cat_code))

    def json(self):
        print "METHOD json"
        rec_dict = {
                "recipe_id" : self.recipe_id,
                "title" : self.title,
                "description" : self.description,
                "image_url" : self.image_url,
                "cat_code" : self.cat_code,
                "cuisine" : self.cuisine,
                "calories" : self.calories,
                "source" : self.source,
                "rate" : self.rate,
                "servings" : self.servings,
                "cook_time" : self.cook_time,
                "skill_level" : self.skill_level

        }

        return rec_dict

    @classmethod
    def getRecipeByTitle(cls, title):

        recipe = Recipe.query.filter(func.lower(Recipe.title) == func.lower(title)).all()
        return recipe

    @classmethod
    def addRecipe(cls, title, description, image, cat_code, servings, cooktime,
                  skillLevel, cuisine):

        if image:
            imageName = image.split(".")
            img_extension = imageName[1]

        new_recipe = Recipe(title=title,description=description,image_url=image,
                            cat_code=cat_code, servings=servings, cook_time=cooktime,
                            skill_level=skillLevel, cuisine=cuisine)
        
        if Recipe.getRecipeByTitle(title):
            raise Exception("This recipe has already been loaded")
        else:
            db.session.add(new_recipe)

        # print db.session.query(max(recipes.recipe_id))
        # print db.session.query(func.max(Recipe.recipe_id))

        # return id
    

    @classmethod
    def deleteRecipeById(cls, recipe_id):

        db.session.query(RecipeUser).filter(RecipeUser.recipe_fk==recipe_id).\
                        delete(synchronize_session=False)

        db.session.query(RecipeStep).filter(RecipeStep.recipe_fk==recipe_id).\
                        delete(synchronize_session=False)

        db.session.query(RecipeIngredient).filter(RecipeIngredient.recipe_fk==recipe_id).\
                        delete(synchronize_session=False)

        db.session.query(Meals).filter(Meals.recipe_fk==recipe_id).\
                        delete(synchronize_session=False)

        db.session.query(Recipe).filter(Recipe.recipe_id == recipe_id).\
                        delete(synchronize_session=False)
        
    

    @classmethod
    def updateRecipeImg(cls, title, cat_code):

        rec = Recipe.query.filter_by(title=title).first()

        # Update img name in the form: CAT_ID.jpg
        if rec.image_url:
            extension = rec.image_url.split(".")[1]
            rec.image_url = rec.cat_code + "_" + str(rec.recipe_id) + extension

    

    @classmethod
    def getRecipeByIngrByUser(cls, ingredient, user=None):

        if user:
            recipes = db.session.query(Recipe).join(RecipeIngredient).join(RecipeUser).\
                        filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
                        filter(RecipeUser.recipe_fk==Recipe.recipe_id).\
                        filter(RecipeUser.user_fk==user).\
                        filter(RecipeIngredient.ingredient_name.like('%'+ingredient+'%')).\
                        all()
        else:
            recipes = db.session.query(Recipe).join(RecipeIngredient).\
                        filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
                        filter(RecipeIngredient.ingredient_name.like('%'+ingredient+'%')).\
                        all()

        return recipes

    ##################### View Recipes #########################################

    @classmethod
    def getAllRecipes(cls):
        """ Returns all the recipes ordered by categories code """

        rec = db.session.query(Recipe).order_by(Recipe.cat_code).all()      

        return rec

    @classmethod
    def getRecipesByUser(cls, user=None):
        """ Returns all the recipes associated to the user """

        recipes = (db.session.query(Recipe).join(RecipeUser).\
                    filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                    filter(RecipeUser.user_fk == user).all())

        return recipes

    @classmethod
    def getCuisineForRecipesByUser(cls, user=None):
        """ Returns a list of cuisine for the recipes associated to the user """

        if user:
            cuisine = (db.session.query(Recipe.cuisine).join(RecipeUser).\
                        filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                        filter(RecipeUser.user_fk == user).\
                        filter(Recipe.cuisine != None).\
                        distinct(Recipe.cuisine).order_by(Recipe.cuisine))
        else:
            cuisine = (db.session.query(Recipe.cuisine).\
                        filter(Recipe.cuisine != None).\
                        distinct().order_by(Recipe.cuisine))    

        return cuisine

    @classmethod
    def getSourceForRecipesByUser(cls, user=None):
        """ Returns a list of Sources for the recipes associated to the user """    

        if user:
            sources = (db.session.query(Recipe.source).join(RecipeUser).\
                        filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                        filter(RecipeUser.user_fk == user).\
                        filter(Recipe.source != None).\
                        distinct().order_by(Recipe.source))
        else:
            sources = (db.session.query(Recipe.source).\
                        filter(Recipe.source != None).\
                        distinct().order_by(Recipe.source))

            
        return sources

    @classmethod
    def getCatForRecipesByUser(cls, user=None):
        """ Returns a list of Categories for the recipes associated to the user """

        if user:
            categories = (db.session.query(Category).join(Recipe).join(RecipeUser).\
                        filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                        filter(Recipe.cat_code == Category.cat_code).\
                        filter(RecipeUser.user_fk == user).\
                        filter(Recipe.cat_code != None).\
                        distinct().order_by(Recipe.cat_code))
        else:
            categories = db.session.query(Category).join(Recipe).\
                        filter(Category.cat_code == Recipe.cat_code).\
                        filter(Recipe.cat_code != None).distinct().order_by(Recipe.cat_code)  


        return categories

    @classmethod
    def getLevelsForRecipesByUser(cls, user=None):
        """ Returns a list of Levels for the recipes associated to the user """

        if user:
            levels = (db.session.query(Recipe.skill_level).join(RecipeUser).\
                        filter(Recipe.recipe_id == RecipeUser.recipe_fk).\
                        filter(RecipeUser.user_fk == user).\
                        filter(Recipe.skill_level != None).\
                        distinct(Recipe.skill_level))
        else:
            levels = (db.session.query(Recipe.skill_level).\
                        filter(Recipe.skill_level != None).\
                        distinct())

        return levels

    #########################Search by Filters##################################

    @classmethod
    def getCuisineByFilter(cls, args):

        cuisine = db.session.query(Recipe.cuisine).\
                filter_by(args).\
                filter(Recipe.cuisine != None).\
                distinct().order_by(Recipe.cuisine)

        return cuisine

    @classmethod
    def getSourcesByFilter(cls, args):

        sources = (db.session.query(Recipe.source).\
                    filter_by(args).\
                    filter(Recipe.source != None).\
                    distinct().order_by(Recipe.source))

        return sources

    @classmethod
    def getCatByFilter(cls, args):

        categories = db.session.query(Category).join(Recipe).\
                    filter_by(args).\
                    filter(Category.cat_code == Recipe.cat_code).\
                    filter(Recipe.cat_code != None).distinct().order_by(Recipe.cat_code)

        return categories  

    @classmethod
    def getLevelsByFilter(cls, args):

        levels = (db.session.query(Recipe.skill_level).\
                    filter_by(**args).\
                    filter(Recipe.skill_level != None).\
                    distinct())
        return levels        

    @classmethod
    def getTitlesByFilter(cls, args):
        titles = db.session.query(Recipe.title).\
                    filter_by(args).\
                    filter(Recipe.title != None).\
                    distinct().order_by(Recipe.title)

        return titles


    def __repr__(self):
        """ Recipe information"""

        return "<Recipe recipe_id= %s title=%s category=%s >" % ( self.recipe_id,
                                   self.title, self.cat_code )

##############################################################################
#
### RECIPES PREPARATION###

class RecipeStep(db.Model):
    """ List of steps for each recipe """

    __tablename__ = "recipe_steps"

    print " RECIPE STEPS"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    step_description = db.Column(db.Text, nullable=True)
    step_num = db.Column(db.Integer, nullable=True)

    
    # Define relationship to recipe
    recipe = db.relationship("Recipe",
                           backref=db.backref("recipe_steps", order_by=recipe_fk))

    @classmethod
    def addRecipeStep(cls,recipe_fk, step_num, step_description):

        """ Enter Steps for recipe """
        print "ENTER RECIPE STEPS"

        new_recStep = RecipeStep(recipe_fk=recipe_fk, step_num=step_num,
                                 step_description=step_description)

        db.session.add(new_recStep)



    def __repr__(self):
        """ Recipe Step """

        return "<RecipeSteps recipe= %s step_num=%s >" % ( self.recipe_fk,
                                                           self.step_num )

##############################################################################
#
### RECIPES CATEGORIES ###

class Category(db.Model):
    """ List of recipe categories """

    __tablename__ = "categories"

    cat_code = db.Column(db.String(5), primary_key=True)
    cat_name = db.Column(db.String(50))


    def __repr__(self):
        """ Category """

        return "<Category code= %s name=%s >" % ( self.cat_code, self.cat_name ) 

##############################################################################
#
### INGREDIENTS ###

class Ingredient(db.Model):
    """Ingredients list"""

    __tablename__ = "ingredients"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    pkg_weight = db.Column(db.Integer, nullable=True)
    pkg_measure = db.Column(db.Integer, nullable=True)
    cost = db.Column(db.String(100), nullable=True)
    aisle = db.Column(db.String(50), nullable=True)

    @classmethod
    def getIngredientByName(cls, name):   
        ingr = Ingredient.query.filter(func.lower(Ingredient.name) == name).all()
        print "INGREDIENTS", ingr
        return ingr


    @classmethod
    def addIngredients(cls, name):
        print "ADD INGREDIENTS in Ingredients"
        if not cls.getIngredientByName(name.lower()):
            new_ingredient = Ingredient(name=name.lower())
            print "NEW_INGRIDIENT", new_ingredient
            db.session.add(new_ingredient)

    @classmethod
    def getAllIngredient(cls):

        ingredients = db.session.query(Ingredient.name).\
                    order_by(Ingredient.name).all()

        return ingredients


    def __repr__(self):
        """ Ingredients information"""

        return "<Ingredients ingredient_id= %s name=%s>" % ( self.id,
                                                             self.name )
##############################################################################
#
### MEALS ###

class Meals(db.Model):
    """Meals list"""

    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    meal_type = db.Column(db.String(20))
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    user_fk = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    portions = db.Column(db.Integer, nullable=True)
    date_planned = db.Column(db.DateTime, nullable=False)
    week_planned = db.Column(db.Integer, nullable=True)
    list_fk = db.Column(db.String(50), nullable=True)


    recipe = db.relationship("Recipe",backref=db.backref("meals"))


    @classmethod
    def plan_meal(cls, recipe_id, meal_type, servings, user_id, date):

        date_planned = datetime.strptime(date,"%m/%d/%Y")
        print "\n\n\n\nDate Planned: {}".format(date_planned)

        weekNum = date_planned.strftime("%W")

        new_meal = Meals(user_fk=user_id, recipe_fk=recipe_id,
                        meal_type=meal_type, portions=servings,
                        date_planned=date_planned, week_planned=weekNum)

        print "NEW MEAL",new_meal
        db.session.add(new_meal)
        db.session.commit()

    @classmethod
    def deleteMeal(cls, date, user, meal_type, recipe):

        db.session.query(Meals).\
            filter(func.substr(Meals.date_planned,0,11)==func.substr(date,0,11)).\
            filter(Meals.user_fk==user).\
            filter(Meals.meal_type==meal_type).\
            filter(Meals.recipe_fk==recipe).\
            delete(synchronize_session=False)


    @classmethod
    def getMealByDateByRecipe(cls, date, user, recipe):

        meal = db.session.query(Meals).filter(Meals.user_fk==user).\
            filter(Meals.recipe_fk==recipe).\
            filter(func.substr(Meals.date_planned,0,11)==func.substr(date,0,11)).\
            all()
        print "\n\n\n\nELEMENT ALREADY EXISTS:", meal


    @classmethod
    def getMealsByDate(cls, date, user):

        mealsPlanned = db.session.query(Meals).filter(Meals.user_fk==user).\
            filter(func.substr(Meals.date_planned,0,11)==func.substr(date,0,11)).\
            all()

        return mealsPlanned

    @classmethod
    def getMealsByDateByType(cls, date, user, type):

        mealsPlanned = db.session.query(Meals).filter(Meals.user_fk==user).\
            filter(Meals.meal_type==type).\
            filter(func.substr(Meals.date_planned,0,11)==func.substr(date,0,11)).\
            all()

        return mealsPlanned    

    @classmethod
    def getMealsByFutureDate(cls, user):
        print "TODAY", datetime.today()
        meals_list = db.session.query(Meals).join(Recipe).join(RecipeIngredient).\
            join(Ingredient).\
            filter(func.substr(Meals.date_planned,0,11) >= func.substr(datetime.today(),0,11)).\
            filter(Meals.recipe_fk==Recipe.recipe_id).\
            filter(Recipe.recipe_id==RecipeIngredient.recipe_fk).\
            filter(RecipeIngredient.ingredient_name==Ingredient.name).\
            filter(Meals.user_fk==user).\
            order_by(Meals.date_planned).all()

        return meals_list

    def __repr__(self):
        """ Meals list"""

        return "<Meals meal= %s recipe=%s date=%s>" % ( self.meal_id,
                                       self.recipe_fk, self.date_planned )


##############################################################################
#
### SHOPPING LIST ###

class ShoppingList(db.Model):
    """Shopping list"""

    __tablename__ = "shop_lists"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    ingredient_fk = db.Column(db.Integer, db.ForeignKey('ingredients.name'))
    qty = db.Column(db.String(20), nullable=True)
    user_fk = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)


    @classmethod
    def addItem(cls, ingredient_fk, user, name):

        shopping_item = ShoppingList(name=name, ingredient_fk=ingredient_fk, user_fk=user)

        db.session.add(shopping_item)
        db.session.commit()


    # @classmethod
    # def getShoppingListByName(cls, name):

    #     s_list = ShoppingList.query.filter_by(name).all()

    #     return s_list

    @classmethod
    def getLatestShoppingList(cls, user):

        t = db.session.query(ShoppingList.user_fk,\
                             func.max(ShoppingList.date_created).label('max_date')).\
            group_by(ShoppingList.name).subquery('t')
    

        s_list = db.session.query(Ingredient.aisle,Ingredient.name,ShoppingList.date_created,
                                    ShoppingList.name.label('list_name')).\
                    join(ShoppingList).\
                    filter(ShoppingList.ingredient_fk == Ingredient.name).\
                    filter(ShoppingList.user_fk == user).\
                    filter(ShoppingList.date_created == t.c.max_date).\
                    filter(ShoppingList.user_fk == t.c.user_fk).all()

        # s_list =  ShoppingList.query.filter_by(user_fk=user).\
        #         group_by(ShoppingList.date_created).having(max(ShoppingList.date_created)).all()

        return s_list

    # @classmethod
    # def deleteItemByDate(cls, ingredient_fk, user, date_created):

    #     db.session.query(ShoppingList).\
    #                     filter(ShoppingList.ingredient_fk==ingredient_fk).\
    #                     filter(ShoppingList.user==user).\
    #                     filter(ShoppingList.date_created==date_created).\
    #                     delete(synchronize_session=False)

    @classmethod
    def getShoppingListNames(cls, user):

        shop_list_names = db.session.query(ShoppingList.name).\
                            filter_by(user_fk=user).\
                            group_by(ShoppingList.name).all()

        return shop_list_names

    @classmethod
    def getAllIngredientsInShopList(cls, user):

        ingredients = db.session.query(Ingredient.aisle, Ingredient.name).\
                      join(ShoppingList).\
                      filter(ShoppingList.ingredient_fk == Ingredient.name).\
                      filter(ShoppingList.user_fk == user).\
                      order_by(Ingredient.aisle, Ingredient.name).all()  

        return ingredients

    @classmethod
    def getShoppingListByName(cls, name, user):
        
        """ Gets the shopping list saved in shop_lists with that name """

        shop_list = db.session.query(Ingredient.aisle,Ingredient.name,ShoppingList.date_created).\
                    join(ShoppingList).\
                    filter(ShoppingList.ingredient_fk == Ingredient.name).\
                    filter(ShoppingList.name == name).\
                    filter(ShoppingList.user_fk == user).all()

        return shop_list

    # @classmethod
    # def getLatestShoppingList(cls, user):

    #     """ Gets the most recent shopping list """

    #     shop_list = db.session.query(Ingredient.aisle,Ingredient.name,ShoppingList.date_created)\
    #                 .join(ShoppingList).\
    #                 filter(ShoppingList.ingredient_fk == Ingredient.name).\
    #                 filter(ShoppingList.user_fk == user).\
    #                 group_by(date_created).having(max(date_created)).all()


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
    def getListIngrName(cls, user):

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
            filter(Meals.user_fk==user).\
            order_by(Ingredient.aisle).all()
            # order_by(Meals.date_planned).all()
        print "LIST INGREDIENT", list_ingr
        return list_ingr

    @classmethod
    def deleteShoppingListByDate(cls, name, user, date_created):

        db.session.query(ShoppingList).\
                filter(ShoppingList.user_fk == user).\
                filter(ShoppingList.date_created == date_created).\
                delete(synchronize_session=False)

        db.session.commit()    



    @classmethod
    def deleteShoppingList(cls, name, user, date_created):

        db.session.query(ShoppingList).\
                    filter(ShoppingList.name == name).\
                    filter(ShoppingList.user_fk == user).\
                    filter(ShoppingList.date_created == date_created).\
                    delete(synchronize_session=False)

        db.session.commit()            
                    

    def __repr__(self):
        """ Shopping list"""

        return "<Shopping list name=%s ingredient=%s date=%s>" % ( self.name,
                                            self.ingredient_fk, date_planned )


##############################################################################
#
### Expenses ###


class Expence(db.Model):
    """ User Expenses """

    __tablename__ = "expences"


    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_fk = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    total = db.Column(db.Float)
    store = db.Column(db.String(50))
    date_of_purchase = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    # Define relationship to user
    # user = db.relationship("User",
    #                        backref=db.backref("expences", order_by=user_fk))

    @classmethod
    def addExpence (cls, date, store, total, user):

        expence = Expence(date_of_purchase=date, store=store, total=total, user_fk=user)

        db.session.add(expence)

        db.session.commit()

    @classmethod
    def getExpencesGroupedByDate(cls, user, month):

        expences = db.session.query(Expence).\
                    filter(cast(func.substr(Expence.date_of_purchase,6,2),Numeric(10,4))>=month).\
                    filter(Expence.user_fk==user).\
                    order_by(Expence.date_of_purchase).all()
                    # %m month num. 

        return expences

    @classmethod
    def getExpencesByStore(cls, user, month):

        expences = db.session.query(Expence.store, func.sum(Expence.total)).\
                    filter(func.substr(Expence.date_of_purchase,6,2)>=month).\
                    filter(Expence.user_fk==user).group_by(Expence.store).all() 

        print "Expences by store", expences

        return expences  


    def __repr__(self):

        """ Expence """

        return "<Expence total=%s  user=%d>" % ( self.total, self.user_fk )


###############################################################################
#
### ASSOCIATION TABLE RECIPES-USERS ###

class RecipeUser(db.Model):
    """ User Recipe Association """

    __tablename__ = "x_recipe_user"


    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_fk = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("x_recipe_user", order_by=user_fk))

    # Define relationship to recipe
    recipe = db.relationship("Recipe",
                           backref=db.backref("x_recipe_user", order_by=recipe_fk))
   

    @classmethod
    def addRecipeForUser(cls, recipe_fk, user_fk):

        print "ADD RECIPE USER"

        recRecipeUser = RecipeUser(recipe_fk=recipe_fk, user_fk=user_fk)
        db.session.add(recRecipeUser)  

    def __repr__(self):
        """ Recipe User Association """

        return "<RecipeUser id= %s user= %s recipe=%s>" % ( self.id,
                                                self.user_fk, self.recipe_fk )

##############################################################################
#
### ASSOCIATION TABLE RECIPE-INGREDIENT ###

class RecipeIngredient(db.Model):
    """User Ingredient Association"""

    __tablename__ = "x_recipe_ingredient"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    ingredient_name = db.Column(db.String(50), db.ForeignKey('ingredients.name'))
    ingredient_info = db.Column(db.String(50), nullable=True)
    quantity = db.Column(db.String(20), nullable=True)
    measure = db.Column(db.String(20), nullable=True)

    # Define relationship to Recipe
    recipe = db.relationship("Recipe",
                           backref=db.backref("x_recipe_ingredient",
                                                       order_by=recipe_fk))
    # Define relationship to Ingredient
    ingredient = db.relationship("Ingredient",
                           backref=db.backref("x_recipe_ingredient", order_by=ingredient_name))

    @classmethod
    def addIngredients(cls, recipe_fk, ingredient_name, quantity, measure):
        print "ADD INGREDIENTS in RecipeIngredient"

        recipeIngr = RecipeIngredient(recipe_fk=recipe_fk,ingredient_name=ingredient_name.lower(),
                     quantity=quantity, measure=measure)

        db.session.add(recipeIngr)
        # db.session.commit()

    @classmethod
    def getAllIngredients(cls):

        recipeIngr = db.session.query(RecipeIngredient).\
                     order_by(RecipeIngredient.recipe_fk).\
                     distinct(RecipeIngredient.ingredient_name).all() 

        return recipeIngr   

    @classmethod
    def getAllMatchingRecipes(cls, ingredient1, ingredient2):

        recipes = db.session.query(RecipeIngredient).\
                      filter(RecipeIngredient.ingredient_name.like('%'+ingredient1+'%')).\
                      filter(RecipeIngredient.ingredient_name.like('%'+ingredient2+'%')).\
                      all()

        return recipes

    @classmethod
    def getAllMatchingRecipe(cls, ingredient):

        recipes = db.session.query(RecipeIngredient).\
                      filter(RecipeIngredient.ingredient_name.like('%'+ingredient+'%')).\
                      all()

        return recipes

    @classmethod
    def getAllIngredientsByRecipe(cls, recipe_fk):

        ingredients = db.session.query(RecipeIngredient).\
                        filter(RecipeIngredient.recipe_fk == recipe_fk).all()

        return ingredients

    @classmethod
    def getAllIngredientsNamesByRecipe(cls, recipe_fk):

        ingredients = db.session.query(RecipeIngredient.ingredient_name).\
                        filter(RecipeIngredient.recipe_fk == recipe_fk).all()

        return ingredients                    

    def __repr__(self):
        """ User Ingredient Association"""

        return "<RecipeIngredient ingredient_id= %s name=%s>" % ( self.id,
                                                             self.ingredient_name )


##############################################################################
# Helper functions

def connect_to_db(app, db_uri='sqlite:///recipes.db'):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/Ricette'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."