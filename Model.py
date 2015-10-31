"""Models and database functions for Food Planner project."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


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
    description = db.Column(db.String(300), nullable=True)
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

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    step_description = db.Column(db.Text, nullable=True) 
    step_num = db.Column(db.Integer, nullable=True)


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

    def __repr__(self):
        """ Ingredients information"""

        return "<Ingredients ingredient_id= %s name=%s>" % ( self.ingredient,
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
    date_planned = db.Column(db.Date, nullable=False)
    week_planned = db.Column(db.Integer, nullable=True)
    list_fk = db.Column(db.String(50), nullable=True)

    @classmethod
    def plan_meal(cls, recipe_id, meal_type, servings, user_id, date):

        new_meal = Meals(user_fk = user_id, recipe_fk = recipe_id,
                        meal_type = meal_type, portions = servings,
                        date_planned = date)
        print new_meal
        db.session.add(new_meal)
        db.session.commit()


    def __repr__(self):
        """ Meals list"""

        return "<Meals meal= %s recipe=%s date=%s>" % ( self.meal_id,
                                       self.recipe_fk, date_planned )


##############################################################################
#
### SHOPPING LIST ###

# class ShoppingList(db.Model):
#     """Shopping list"""

#     __tablename__ = "shop_lists"

#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     name = db.Column(db.String(50), nullable=true)
#     ingredient_fk = db.Column(db.Integer, db.ForeignKey('ingredients.id'))
#     user_fk = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     date = db.Column(db.Timestamp, nullable=False)
#     qty = db.Column(db.String(20), nullable=True)

#     def __repr__(self):
#         """ Shopping list"""

#         return "<Shopping list name=%s ingredient=%s date=%s>" % ( self.name,
#                                             self.ingredient_fk, date_planned )

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


    def __repr__(self):
        """ User Ingredient Association"""

        return "<RecipeIngredient ingredient_id= %s name=%s>" % ( self.id,
                                                             self.ingredient_name )

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."