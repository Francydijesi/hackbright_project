# Meal Planner

Wouldn't be great if we could go shopping for food just once a week and have the whole week's worth of meals planned ahead of time? This would save a great amount of time, money and stress.

This web application was designed with the goal of solving this simple but common problem and making cooking and shopping for food easy.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Homepage.png "Homepage")
This app has three main sections:
* __Recipes__, where you can store your own recipes or import new ones from the web
* __Planner__, a useful tool that allows you to upload the recipes you would like to cook during the week for each day and each meal.
* __Grocery__, where you can view the shopping list automatically generated, with the ingredients necessary for the weekly meals which were uploaded in the planner. You can also keep track of the grocery expenses and analyze your shopping habits.  


## Table of Contents
* [Technologies Used](#technologiesused)
* [How to use Meal Planner](#use)
* [How to locally run Meal Planner](#run)
* [About the author](#author)


## <a name="technologiesused"></a>Technologies Used

* Python
* Sqlite
* Sqlalchemy
* Flask
* Beautiful soup library
* Javascript/jQuery
* AJAX/JSON
* Jinja2
* Chart.js
* D3
* Bootstrap
* Twilio API

(dependencies are listed in requirements.txt)


## <a name="use"></a>How to use Meal Planner


###Recipes 


#### Recipe Import

Write down your family recipes or import new ones from the web by using beautiful soup (a Python web scraping library). 

![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe_Form.png "Recipe form")

___


#### Recipes list

Use the filters or the search function to quickly find your recipe. Click on the picture or the view button to go to the recipe page for more details.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe%20List.png "Recipe View")

___


#### Recipe page

Follow all the instructions to cook the meal now or save it for a future meal and upload it to the planner.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe%20Page.png "Recipe Page")

___


### <a name="run"></a>Planner

Planner is a seven day calendar where you can view the recipes already uploaded in the recipe page, or you can add new ones.
Once you are done planning for the week, you can generate your shopping list with all the ingredients necessary for your recipes.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Add%20meal%20to%20planner.png "Planner")

___


### <a name="run"></a>Grocery

#### List

This list was generated with the ingredients of all the recipes in the planner.
It can be printed or sent as an SMS, using the Twilio API.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Shopping%20List.png "Shopping list")

___


#### Expenses

If you are interested in keeping track of your grocery budget, here is a tool for recording your expenses and visualizing them.

View the expenses by week or grouped by store, for this month or the past two or three months.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Grocery%20Expenses.png "Grocery expenses graphs")

___


#### Ingredient analysis

This bubble chart shows all of the ingredients saved in all the shopping lists, color coded by category. The bigger the bubble, the higher its frequency. 

![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Ingredient%20Analysis.png "Ingredient Analysis")


## <a name="run"></a>How to locally run Meal Planner

* Set up and activate a python virtualenv, and install all dependencies:
    * `pip install -r requirements.txt`
  
* Create the tables in your database:
    * `python -i model.py`
    * While in interactive mode, create tables: `db.create_all()`
    
* Now, quit interactive mode. Start up the flask server:
    * `python server.py`

* Go to localhost:5000 to see the web app


## <a name="author"></a>About the author

Francesca Paoletti graduated from an italian university in Math with a final thesis in "Data Envelopment Analysis", in the operational research field. She took a course in "Credit Risk Analysis" at IMI Bank in Italy and in "Business Administration" at UC Berkeley. She worked for a number of years as a high school math teacher and a java back end developer. She is very passionate about data science. For more details see her [linkedin] (https://www.linkedin.com/in/francescapaoletti) profile.



