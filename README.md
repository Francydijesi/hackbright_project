# Meal Planner

Wouldn't be great if we could go shopping for food just once a week and have the whole week's worth of meals planned ahead of time? This would save a great amount of time, money and stress.

This web application was designed with the goal of solving this simple but common problem and making cooking and shopping for food easy.

![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Homepage.png "Homepage")
This app has three main sections:
* Recipes, where you can store your own recipes or import new ones from the web
* Planner, a useful tool that allows you to upload the recipes you would like to cook during the week for each day and each meal.
* Grocery. In this section you can view the shopping list automatically generated, with the ingredients necessary for the weekly meals which were uploaded in the planner. You can also keep track of the grocery expenses and analyze your shopping habits.  


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


## <a name="run"></a>Recipes 
![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe_Form.png "Recipe form")
Write down your family recipes or import new ones from the web by using beautiful soup (a Python web scraping library). 


![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe%20List.png "Recipe View")
Use the filters or the search function to quickly find your recipe. Click on the picture or the view button to go to the recipe page for more details.


![alt text](https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Recipe%20Page.png "Recipe Page")
Follow all the instructions to cook the meal now or save it for a future meal and upload it to the planner.


## <a name="run"></a>Planner
![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Add%20meal%20to%20planner.png "Planner").
Planner is a seven day calendar where you can view the recipes already uploaded in the recipe page, or you can add new ones.
Once you are done planning for the week, you can generate your shopping list with all the ingredients necessary for your recipes.


## <a name="run"></a>Grocery
![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Shopping%20List.png "Shopping list")
This list was generated with the ingredients of all the recipes in the planner.
It can be printed or sent as an SMS, using the Twilio API.


![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Grocery%20Expenses.png,"Grocery expenses graphs")
If you are interested in keeping track of your grocery budget, here is a tool for recording your expenses and visualizing them.

View the expenses by week or grouped by store, for this month or the past two or three months.


![alt text]
(https://github.com/Francydijesi/hackbright_project/blob/master/static/img/Readme/Ingredient%20Analysis.png "Ingredient Analysis")
This bubble chart shows all of the ingredients saved in all the shopping lists, color coded by category. The bigger the bubble, the higher its frequency. 
