from bs4 import BeautifulSoup, NavigableString, Tag

from model import Recipe, RecipeIngredient, RecipeStep, Ingredient

from flask import session

import helpFunctions

import requests



def url_scraper(url, user):


########    SCRAP DATA FROM URL   #########


    r = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, 'html.parser')

    title = soup.header.h1.contents[0].strip()

    description = ''

    if soup.find('div', 'topnote'):

        description = soup.find('div', 'topnote').p.contents[0]

    time = ''

    servings = ''

    img_url = ''

    cat_code = ''

    cuisine = ''

    skillLevel = ''

    if soup.find('span', 'icon icon-clock'):

        time = soup.find('span', 'icon icon-clock').next_sibling

    if soup.find('span', 'icon icon-person'):

        servings = soup.find('span', 'icon icon-person').next_sibling.contents[0]

    if soup.find('div', 'media-container '):

        if soup.find('div', 'media-container ').find('img'):

            img_url = soup.find('div', 'media-container ').find('img')['src']

    elif soup.find('div', 'video-container'):

        img_url = soup.find('div', 'video-container').\
                find_all(attrs={"itemprop" : "image"})[0]['content']

    elif soup.find('div', 'media-container vertical'):   

        if soup.find('div', 'media-container vertical').find('img'): 

            img_url = soup.find('div', 'media-container vertical').find('img')['src']                   
    

    text = soup.find('div', 'recipe grid-wrap').get_text(strip=True)

    text = set(text.split())

    cat_code = calculateCategory(text)

    cuisine = calculateCuisine(text)

    print "CAT", cat_code

    ingredients = []

    passi = []

    unit = ''

    # FIND ALL THE INGREDIENTS

    for ingr_item in soup.find_all('ul', 'recipe-ingredients'):

        for li in ingr_item.find_all('li'):

            quantity = li.find('span', 'quantity')

            if quantity:

                qty = quantity.next

            print "QUANTITY ", qty

            more_info = li.find('span','ingredient-name')

            ingredient = ''

            if more_info:

                info = more_info.text

                print "INFO", info

                unit = getUnit(info)

                if more_info.span:

                    ingredient = more_info.span.next

                    print "INGREDIENT", ingredient
            if ingredient:

                ingredient = cleanIngredient(ingredient)

                ingredients.append( {'name': ingredient,
                                 'qty': qty,
                                 'unit': unit})

    # FIND ALL THE STEPS

    for steps in soup.find_all('ol', 'recipe-steps'):

        for li in steps.find_all('li'):

            step = li.text

            passi.append(step)

            print "STEP", step


########    ADD TO DATABASE   #########

    # Missing info: CUISINE

    title = title.strip()
    time = time.strip()
    print "IMAGE_URL", img_url

    message = helpFunctions.addRecipe(img_url, title, description, cat_code, servings,
             time, skillLevel, cuisine, ingredients, passi, user)


    print "MESSAGE", message
    return message


########    UTILITY FUNCTIONS   #########

def cleanIngredient(ingredient):

    ingredient = ingredient.strip()

    lemonSet = set(ingredient.split()) & set(['lemon', 'Lemon'])

    flourSet = set(['all-purpose flour', 'all purpose flour', 'flour'])

    eggSet = set(['egg', 'eggs', 'egg white', 'egg yolk'])

    unnecessaryWords = set(['finely','chopped','minced','crushed','grated','flaky',
                            'medium thickness', 'no-boil', 'leaves',  'sprigs',
                            'wedges','skinless','cheese'])

    ingredient = ingredient.split(' or ')[0]

    ingredient = ingredient.split(',')[0]

    ingredient = ''.join(set(ingredient.split()) - unnecessaryWords)

    if ingredient in eggSet:

        ingredient = 'eggs'

    if lemonSet:

        ingredient = lemonSet

    if ingredient.find('butter') != -1:

        ingredient = 'butter'

    if ingredient in flourSet:

        ingredient = 'all-purpose flour'

    if ingredient.find('olive oil') != -1:

        ingredient = 'extra virgin olive oil'

    if ingredient.find('salt') != -1:

        ingredient = 'salt'

    if ingredient.find('chicken thighs') != -1:

        ingredient = 'chicken thighs'

    if ingredient.find('cayenn') != -1:

        ingredient = 'cayenne pepper'

    if ingredient.find('chile') != -1:

        ingredient = 'chile'

    # if ingredient.find('garlic') != -1:

    #     ingredient = 'garlic'
    
    if ingredient.find('scallion') != -1:

        ingredient = 'scallions'

    # if ingredient.find('cilantro') != -1:

    #     ingredient = 'cilantro'

    return ingredient.strip().lower()

    

def calculateCuisine(text):

    cuisine = ''

    italian = set(['italian', 'oregano', 'parsley', 'basil', 'pasta', 'lasagna', 'ragu',
                    'besciamella', 'pizza', 'gnocchi'])

    asian = set(['asian', 'ginger', 'soy sauce', 'mirin', 'stir-fry', 'sushi', 'cantonese',
                'rice wine', 'rice vinegar', 'asian rice', 'hoisin sauce',
                'japanese' ])

    indian = set(['indian', 'curry', 'garam masala', 'cardamom'])

    mexican = set(['mexican', 'tortilla', 'chipotle', 'burrito', 'enchilada'])

    american = set(['american', 'stew', 'muffin', 'pancake', 'hamburger'])

    north_african = set(['couscous', 'dates','tagin','moroccan', 'mediterranean',
        'lebanese', 'north african'])

    if text & italian:
        cuisine = 'Italian'

    elif text & asian:
        cuisine = 'Asian'

    elif text & indian:
        cuisine = 'Indian'

    elif text & mexican:
        cuisine = 'Mexican'

    elif text & north_african:
        cuisine = 'North African'           

    else:
        cuisine = 'International'

    return cuisine



def calculateCategory(text):

    cat_code = ''

    cat_pasta_PS = set(['pasta', 'lasagna', 'fettuccine', 'noodle'])
    cat_soup_SP = set(['soup'])
    cat_salad_SL = set(['salad', 'insalata'])
    cat_vegetable_VG = []
    cat_beansGrain_BG = set(['beans', 'lentils', 'cheakpeas', 'barley', 'rice', 'arborio',
                     'risotto', 'quinoa', 'spelt', 'farro', 'wheat', 'corn'])
    cat_holiday_HL = set(['Christmas', 'Thanksgiving', 'Easter', 'Halloween'])
    cat_party_PR = set(['birthday', 'anniversary', 'party'])
    cat_meat_MT = set(['meat', 'chicken', 'veal', 'beef', 'chicken', 'lamb', 'venison',
                'rabbit', 'pheasant', 'duck', 'pork', 'turkey', 'quail', 'bufalo',
                'mutton'])
    cat_vegan_VG = []
    cat_fish_FS = set(['shrimps', 'cod', 'salmon', 'tilapia', ''])
    cat_dessert_DS = set(['sugar', 'brown sugar', 'flour', 'eggs', 'dessert', 'cookies', 'cake', 'tart',
                'icecream', 'panettone', 'pudding'])
    cat_pizzaBread_BK = set(['pizza', 'loaf', 'calzone', 'ciabatta', 'sandwich'])

    cat_vegan_VE = set(['vegan'])

    words_set = text

    # is_pasta = words_set & cat_pasta_PS

    if words_set & cat_pasta_PS:
        cat_code = 'PS'

    elif words_set & cat_party_PR:
        cat_code = 'PR'

    elif words_set & cat_holiday_HL:
        cat_code = 'HL'

    elif words_set & cat_pizzaBread_BK:
        cat_code = 'BP'

    elif words_set & cat_meat_MT:
        cat_code = 'MT'

    elif words_set & cat_fish_FS:
        cat_code = 'FS'

    elif words_set & cat_dessert_DS:
        cat_code = 'DS'

    elif words_set & cat_soup_SP:
        cat_code = 'SP'

    elif words_set & cat_vegan_VE:
        cat_code = 'VE'

    else:
        cat_code = 'VG'

    # if any(word in text for word in pasta_PS):
        
    return cat_code


def getUnit(text):

    m_unit =''

    measuresUnit = ['ounce', 'ounces', 'cup', 'cups','tablespoon', 'pound', 'pounds', 'tablespoons','teaspoon',
                 'teaspoons', 'pinch', 'clove', 'cloves']

    print "TEXT" , text
    if text and text.split()[0] in measuresUnit:

        m_unit= text.split()[0]

    return m_unit
