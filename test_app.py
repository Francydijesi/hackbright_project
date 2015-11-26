import os
import unittest
import doctest
from server import app, index
from flask import session, request
from model import (Recipe, User, Ingredient, RecipeStep, Category, RecipeUser,
            Expence, ShoppingList, RecipeIngredient, Meals, connect_to_db, db)
# -*- coding: utf-8 -*-

    ############################   DOCTESTS ##########################

def load_tests(loader, tests, ignore):
    """ It runs the doctest"""

    # tests.addTests(doctest.DocTestSuite(server))
    # tests.addTests(doctest.DocFileSuite("tests.txt"))
    return tests

class MealPlannerTests(unittest.TestCase):

    ############################   UNIT TESTS ##########################

    """Test for functions that don't require sessions."""

    def setUp(self):
        # set up fake test browser
        self.client = app.test_client()

        # connect to a test database
        connect_to_db(app, "sqlite:///test.db")

        # This line makes a 500 error in a route raise an error in a test
        app.config['TESTING'] = True

        app.secret_key = "ABC"
        # coding: utf-8

        # create tables and add sample data
        # db.create_all()
        

    ########################   INTEGRATION TESTS  #############################
    # LOGIN/LOGOUT

    def test_load_homepage(self):
        """Tests to see if the homepage comes up"""

        result = self.client.get('/')
        # print dir(result) to see what methods are available for result

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Store Recipes', result.data)

    def test_signup_old_user(self):
        """Tests signup function when the user has already an account"""

        result = self.client.post('/register-confirm',
            data={"email":"francescagraham2000@yahoo.com","password":"semagna"})

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('You already have an account', result.data)

    def test_signup_new_user(self):
        """Tests signup function when the user is new"""

        result = self.client.post('/register-confirm',
           data={"email":"sofiagraham@yahoo.com","password":"muntobe", "name":"Sofia"})

        self.assertEqual(result.status_code, 302)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Redirecting', result.data)

    def test_signin_old_user(self):
        """Tests to see if the signup function works."""

        result = self.client.post('/login_confirm',
           data={"email":"francescagraham2000@yahoo.com","password":"semagna"})

        self.assertEqual(result.status_code, 302)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Redirecting', result.data)

    
    def test_log_out(self):
        """ Test the log out function"""

        with self.client as c:
            
            with c.session_transaction() as sess:
                sess['User'] = '1'
            
            c.set_cookie('localhost', 'MYCOOKIE', 'cookie_value')
                # sess['_fresh'] = True 

        result = self.client.get('/logout')

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Log In', result.data)

    # RECIPE

    def test_search_recipe_load_by_user(self):
        """Tests search recipe list"""

        with self.client as c:
            
            with c.session_transaction() as sess:
                sess['User'] = '1'
            
            c.set_cookie('localhost', 'MYCOOKIE', 'cookie_value')
                # sess['_fresh'] = True 

        result = self.client.get('/recipes')

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Cuisine', result.data)

    # def test_search_recipe_data(self):
    #     """ Tests search recipe list by filters"""
        
    #     with self.client as c:
    #         resp = c.post('/changeFilters.json',
    #             data={"title":"Roasted Veggie Tarts","cuisine":"",
    #             "level":"","cat":"","source":""})
    #         data = json.loads(resp.data)
    #         self.assert_equal(data['titles'], 'Roasted Veggie Tarts')

    # IMPORT RECIPE FORM

    def test_import_recipe_form(self):
        """ Tests import form """
        result = self.client.get('/addRecipesForm')

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('New York Times', result.data)

    def test_scrape_old_recipe(self):
        """ Test the scraping function when recipe is already in DB """

        Recipe.deleteRecipeById(recipe_id=39)
        db.session.commit()

        result = self.client.post('/importRecipe',
        data={"url":"http://cooking.nytimes.com/recipes/1015348-spicy-red-pepper-cranberry-relish"},
        follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Error: This recipe has already been loaded', result.data)

    # def test_scrape_new_recipe(self):
    #     """ Test the scraping function when recipe is not in DB """

    #     result = self.client.post('/importRecipe',
    #     data={"url":"http://cooking.nytimes.com/recipes/1017780-whole-roasted-stuffed-delicata-squash"},
    #     follow_redirects=True)

    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('text/html', result.headers['Content-Type'])
    #     self.assertIn('Whole-Roasted', result.data)
    
    # RECIPE PAGE

    def test_recipe_page(self):
        """ Tests if recipe page comes up """
        
        result = self.client.get('/recipe_page/28')

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Preparation', result.data)

    # def test_delete_recipe(self):
    #     """ Test recipe delete function """

    #     result = self.client.get('/deleteRecipe/39', follow_redirects=True)

    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('text/html', result.headers['Content-Type'])
    #     self.assertNotIn('Whole-Roasted Stuffed Delicata Squash', result.data)


    def tearDown(self):# It runs after each test
        print 'doing my teardown'
        User.query.filter_by(user_id=2).delete()
        Recipe.deleteRecipeById(recipe_id=39)
        
        db.session.commit()

    # MEAL PLANNER
    
    def test_planner_page(self):
        """ Tests if planner comes up """

        with self.client as c:
            
            with c.session_transaction() as sess:
                sess['User'] = '1'

        result = self.client.get('/planner')

        self.assertEqual(result.status_code, 200)
        self.assertIn('text/html', result.headers['Content-Type'])
        self.assertIn('Breakfast', result.data)    

if __name__ == "__main__":
    unittest.main()
