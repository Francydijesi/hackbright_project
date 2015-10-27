"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from correlation import pearson

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

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
    zipcode =db.Column(db.IntegerString(50), nullable=True)

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

class Recipes(db.Model):
    """ Recipes list """

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    image_url = db.Column(db.String(100), nullable=True)
    cat_code = db.Column(db.String(50), db.foreignKey('categories.cat_code'))
    cuisine = db.Column(db.String(50), nullable=True)
    calories = db.Column(db.Integer, nullable=True)
    rate = db.Column(db.String(50), nullable=True)
    servings = db.Column(db.Integer, nullable=True)
    cook_time = db.Column(db.String(50), nullable=True)
    skill_level = db.Column(db.String(2), nullable=True)

    def __repr__(self):
        """ Recipe information"""

        return "<Recipe recipe_id= %s title=%s category=%s >" % ( self.recipe_id,
                                   self.title, self.cat_code )

##############################################################################
#
### RECIPES PREPARATION###

class RecipeSteps(db.Model):
    """ List of steps for each recipe """

    __tablename__ = "recipe_steps"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    step_description = db.Column(db.String(500), nullable=true) 
    step_num = db.Column(db.Integer, nullable=true)

    def __repr__(self):
        """ Recipe Step """

        return "<RecipeSteps recipe= %s step_num=%s >" % ( self.recipe_fk,
                                                           self.step_num ) 

##############################################################################
#
### RECIPES CATEGORIES ###

class Categories(db.Model):
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

class Ingredients(db.Model):
    """Ingredients list"""

    __tablename__ = "ingredients"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
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

# class Meals(db.Model):
#     """Meals list"""

#     __tablename__ = "meals"

#     meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     recipe_fk = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
#     user_fk = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     portions = db.Column(db.Integer, nullable=True)
#     date_planned = db.Column(db.Date, nullable=False)
#     week_planned = db.Column(db.Integer, nullable=True)
#     list_fk = db.Column(db.String(50), nullable=True)

#     def __repr__(self):
#         """ Meals list"""

#         return "<Meals meal= %s recipe=%s date=%s>" % ( self.meal_id,
#                                             self.recipe_fk, date_planned )

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
    recipe_fk = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    ingredient_fk = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))
    quantity = db.Column(db.Integer, nullable=True)
    measure = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        """ User Ingredient Association"""

        return "<RecipeIngredient ingredient_id= %s name=%s>" % ( self.ingredient,
                                                             self.name )

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."