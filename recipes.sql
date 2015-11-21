PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	user_id INTEGER NOT NULL, 
	email VARCHAR(64) NOT NULL, 
	password VARCHAR(64) NOT NULL, 
	age INTEGER, 
	gender VARCHAR(15), 
	name VARCHAR(50), 
	zipcode INTEGER, 
	PRIMARY KEY (user_id)
);
INSERT INTO "users" VALUES(1,'francescagraham2000@yahoo.com','semagna',NULL,NULL,NULL,NULL);
CREATE TABLE ingredients (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	pkg_weight INTEGER, 
	pkg_measure INTEGER, 
	cost VARCHAR(100), 
	aisle VARCHAR(50), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "ingredients" VALUES(1,'baby spinach leaves',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(2,'eggs',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(3,'salt',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(4,'nutmeg',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(5,'pepper',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(6,'flour',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(7,'butter',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(8,'bacon',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(9,'sage',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(10,'Parmesan',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(11,'vegetable oil',NULL,NULL,NULL,'Condiments');
INSERT INTO "ingredients" VALUES(12,'chile',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(13,'snow peas',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(14,'scallion',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(15,'garlic',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(16,'ginger',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(17,'toasted sesame oil',NULL,NULL,NULL,'Condiments');
INSERT INTO "ingredients" VALUES(18,'roasted peanuts',NULL,NULL,NULL,'Dry fruits');
INSERT INTO "ingredients" VALUES(19,'cilantro',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(20,'lamb shanks',NULL,NULL,NULL,'Meat&Fish&Poultry');
INSERT INTO "ingredients" VALUES(21,'cumin',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(22,'paprika',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(23,'onion',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(24,'saffron',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(25,'cayenn pepper',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(26,'tomato paste',NULL,NULL,NULL,'Condiments');
INSERT INTO "ingredients" VALUES(27,'cinnamon stick',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(28,'dates',NULL,NULL,NULL,'Dry fruits');
INSERT INTO "ingredients" VALUES(29,'golden raisins',NULL,NULL,NULL,'Dry fruits');
INSERT INTO "ingredients" VALUES(30,'pomegranate seeds',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(31,'yellow fleshed potatoes',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(32,'extra-virgin olive oil ',NULL,NULL,NULL,'Condiments');
INSERT INTO "ingredients" VALUES(33,'butternut squash',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(34,'zucchini',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(35,'red bell pepper',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(36,'fresh oregano',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(37,'ground cumin',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(38,'ground origano',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(39,'vegan margarine',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(40,'organic sugar',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(41,'whole wheat flour',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(42,'quinoa',NULL,NULL,NULL,'Pasta & Grains');
INSERT INTO "ingredients" VALUES(43,'water',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(44,'celeriac',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(45,'ground sage',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(46,'ground thyme',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(47,'parsley',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(48,'hazelnuts',NULL,NULL,NULL,'Dry fruits');
INSERT INTO "ingredients" VALUES(49,'bosc pears',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(50,'anjou pears',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(51,'pomegranate molasses',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(52,'unsalted butter',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(53,'tapioca',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(54,'light brown sugar',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(55,'ground ginger',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(56,'all-purpose flour',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(57,'pasta',NULL,NULL,NULL,'Pasta & Grains');
INSERT INTO "ingredients" VALUES(59,'half-and-half',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(60,'cayenne',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(61,'dry lasagna noodles',NULL,NULL,NULL,'Pasta & Grains');
INSERT INTO "ingredients" VALUES(62,'broccoli rabe',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(63,'ricotta',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(64,'lemon',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(65,'dried red chiles',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(66,'chuck steak',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(67,'olive oil',NULL,NULL,NULL,'Condiments');
INSERT INTO "ingredients" VALUES(68,'onions',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(69,'dry red wine',NULL,NULL,NULL,'Drinks');
INSERT INTO "ingredients" VALUES(70,'cloves',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(71,'bay leaf',NULL,NULL,NULL,'Spices');
INSERT INTO "ingredients" VALUES(72,'thyme',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(73,'carrots',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(74,'chickpea flour',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(75,'fine cornmeal',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(76,'kosher salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(77,'baking powder',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(78,'turmeric powder',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(79,'fresh corn kernels',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(80,'cumin seeds',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(81,'fennel seeds',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(82,'mustard seeds',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(83,'chopped fresh red or green chile',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(84,'chopped scallions',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(85,'chopped cilantro',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(86,'grated ginger',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(87,'vegetable oil, for frying',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(88,'lime wedges',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(89,'mango-tamarind chutney',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(90,'fresh asparagus, medium thickness',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(91,'minced shallots',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(92,'heavy cream',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(93,'fresh lemon juice',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(94,'minced fresh dill',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(95,'cherry tomatoes',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(96,'eggplants',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(97,'ricotta salata',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(98,'basil',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(99,'porcini or shiitake mushrooms',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(100,'extra virgin olive oil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(101,'shallots',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(102,'cremini mushrooms',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(103,'fruity red wine',NULL,NULL,NULL,'Drinks');
INSERT INTO "ingredients" VALUES(104,'thyme leaves',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(105,'shallot or onion',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(106,'milk',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(107,'no-boil lasagna noodles',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(108,'parmesan cheese',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(109,'egg',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(110,'bittersweet chocolate',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(111,'vanilla extract',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(112,'whole milk',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(113,'brown sugar',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(114,'unsweetened cocoa powder',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(115,'cornstarch',NULL,NULL,NULL,'Baking');
INSERT INTO "ingredients" VALUES(116,'fine sea salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(117,'whipped cream',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(118,'chocolate shavings',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(119,'flaky sea salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(120,'skinless chicken breast',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(121,'egg white',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(122,'rice wine',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(123,'sugar',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(124,'hoisin sauce',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(125,'soy sauce',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(126,'peanut oil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(127,'green peppers',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(128,'cashew',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(129,'dried hominy',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(130,'dried red new mexico chiles',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(131,'fresh pork belly',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(132,'pork shoulder',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(133,'salt and pepper',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(134,'chopped garlic',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(135,'finely diced white onion',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(136,'pork chops',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(137,'dijon mustard',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(138,'black pepper',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(139,'canola oil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(140,'pork loin',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(141,'red onion',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(142,'rosemary sprigs',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(143,'plum tomatoes',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(144,'anchovy fillets',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(145,'polenta, noodles or rice',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(146,'pine nuts',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(147,'pea shoots',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(148,'cilantro leaves',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(149,'bone-in pork chops',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(150,'arugula',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(151,'shallot',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(152,'lemon juice',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(153,'coarse sea salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(154,'extra-virgin olive oil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(155,'yellow onion',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(156,'ground lamb',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(157,'cinnamon',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(158,'tomato sauce',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(159,'mozzarella',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(160,'sea salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(161,'chicken',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(162,'couscous',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(163,'almonds',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(164,'orange blossom water',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(165,'honey',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(166,'mint',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(167,'cauliflower',NULL,NULL,NULL,'Produce');
INSERT INTO "ingredients" VALUES(168,'anchovies',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(169,'rosemary leaves',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(170,'tomatoes',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(171,'white wine',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(172,'pequin chiles',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(173,'flaky salt',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(174,'chervil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(175,'salmon',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(176,'lemon wedges',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(177,'boneless chicken thighs',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(178,'bread crumbs',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(179,'dry white wine',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(180,'chicken or vegetable stock',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(181,'granulated sugar',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(182,'pineapple juice',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(183,'chicken thighs',NULL,NULL,NULL,'Meat Fish Poultry');
INSERT INTO "ingredients" VALUES(184,'parsley leaves',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(185,'fresh ginger',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(186,'cayenne pepper',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(187,'plain whole-milk yogurt',NULL,NULL,NULL,'Dairy');
INSERT INTO "ingredients" VALUES(188,'oil',NULL,NULL,NULL,NULL);
INSERT INTO "ingredients" VALUES(189,'walnut',NULL,NULL,NULL,NULL);
CREATE TABLE categories (
	cat_code VARCHAR(5) NOT NULL, 
	cat_name VARCHAR(50), 
	PRIMARY KEY (cat_code)
);
INSERT INTO "categories" VALUES('AP','Appetizer');
INSERT INTO "categories" VALUES('SP','Soup');
INSERT INTO "categories" VALUES('SL','Salad');
INSERT INTO "categories" VALUES('VG','Vegetable');
INSERT INTO "categories" VALUES('BG','Bean&Grain');
INSERT INTO "categories" VALUES('PS','Pasta');
INSERT INTO "categories" VALUES('HL','Holiday');
INSERT INTO "categories" VALUES('PR','Party');
INSERT INTO "categories" VALUES('MT','Meat');
INSERT INTO "categories" VALUES('VE','Vegan');
INSERT INTO "categories" VALUES('FS','Fish');
INSERT INTO "categories" VALUES('DS','Dessert');
INSERT INTO "categories" VALUES('BP','Bread&Pizza');
CREATE TABLE recipes (
	recipe_id INTEGER NOT NULL, 
	title VARCHAR(64) NOT NULL, 
	description TEXT, 
	image_url VARCHAR(100), 
	cat_code VARCHAR(50), 
	cuisine VARCHAR(50), 
	calories INTEGER, 
	source VARCHAR(50), 
	rate VARCHAR(20), 
	servings INTEGER, 
	cook_time VARCHAR(50), 
	skill_level VARCHAR(2), 
	PRIMARY KEY (recipe_id), 
	FOREIGN KEY(cat_code) REFERENCES categories (cat_code)
);
INSERT INTO "recipes" VALUES(4,'Olive Oil Mashed Potatoes','These mashed potatoes are extremely easy to make, and have the added benefit of being vegan. A hefty dose of garlic lends a bite to the creaminess. Make sure to use good olive oil.','VG_4.jpg','VG','Italian',NULL,NULL,NULL,6,'20 minutes','E');
INSERT INTO "recipes" VALUES(5,'Roasted Veggie Tarts','You can use a mini-muffin tray to form the shells of her crowd-pleasing butternut squash and zucchini mini-tarts. The vegetable filling is made quick and easy by using a wok to cook the vegetables.','VG_3.jpg','AP','International',NULL,NULL,NULL,4,'45 minutes','M');
INSERT INTO "recipes" VALUES(6,'Squash and Celeriac Quinoa Stuffing','Vegans and non-vegans will enjoy this twist on a traditional stuffing, where quinoa replaces the bread and butternut squash, celeriac and hazelnuts add the flavors of fall.
','VG.jpg','VE','International',NULL,NULL,NULL,6,'45 minutes','E');
INSERT INTO "recipes" VALUES(7,'Pear-Pomegranate Pie ','In this welcome departure from the traditional apple pie, a combination of Anjou and Bosc pears are caramelized in a mixture of pomegranate molasses and butter, then combined with a smaller portion of fresh, uncooked pears. The whole glorious mess is then dumped into an all-butter crust and baked until tender. The happy result is a pie that''s soft and sweet, tangy and toothsome, and oh so good.','DS_2.jpg','DS','International',NULL,NULL,NULL,8,'1 hour 30 minutes','M');
INSERT INTO "recipes" VALUES(8,'Broccoli Rabe Lasagna','Broccoli rabe (sometimes spelled raab, or known as rapini greens) is one of the most delicious members of the mustard green family. The leaves, tender stems and broccoli-like buds have a distinctive pleasant bitterness when cooked. For this vegetarian lasagna, some of the cooked greens are puréed to make a garlicky pesto and the rest is coarsely chopped and added to the layers.','PT_2.jpg','PS','Italian',NULL,NULL,NULL,6,'1 hour 30 minutes','D');
INSERT INTO "recipes" VALUES(9,'Spinach Spaetzle With Bacon and Sage','Spaetzle, the delicious little German dumplings (sometimes called batter noodles).These are green spaetzle, made with spinach purée, sizzled with bacon and sage leaves. (Instead of spinach, you could add chopped herbs, but plain spaetzle are divine, too.) Spaetzle take only moments to cook and can be prepared in advance, then sautéed in butter to serve.','PS_1.jpg','PS','German','','NYT','Delicious',6,'1 hour','M');
INSERT INTO "recipes" VALUES(10,'Spicy Wok-Charred Snow Peas','High-heat stir-fries are ideal for peas — either snow peas or the sugar snap variety. Assertive seasoning and the slight charring from the wok complement the peas’ sweetness wonderfully. The method works well for other spring vegetables, too, like asparagus or baby bok choy clusters. Use a wide cast -iron pan if you don’t have a wok. Take care to avoid overcooking; the peas should be a vibrant green color and firm to the bite.','VG_2.jpg','VG','American','','NYT','Delicious',6,'15 minutes','E');
INSERT INTO "recipes" VALUES(13,'Craig Claiborne''s Beef Stew','It would be hard to find a simpler meal than Mr. Claiborne’s hearty beef stew, which goes beautifully with buttered noodles and a stout glass of red wine. (Or, for the children, a glass of milk.) A small scattering of cloves adds a floral note to the gravy, augmented by just a little thyme, and the combination pairs beautifully with the carrots you add near the end of the cooking process, to prevent them from going mushy in the heat. Sprinkle chopped parsley over the finished dish, of course, a nod to the past that rewards in beauty and flavor alike.','http://graphics8.nytimes.com/images/2014/04/11/dining/beefstew/beefstew-articleLarge.jpg','MT','American',NULL,NULL,NULL,'8 servings','About 1 hour 30 minutes
            ','');
INSERT INTO "recipes" VALUES(14,'Spicy Corn Pakoras With Mango-Tamarind Chutney','Crisp and deeply seasoned, pakoras are Indian fritters that can be made from almost any vegetable. To emphasize the corn flavor here, fine cornmeal joins the more traditional chickpea flour — along with fresh corn. A ridiculously flavorful chutney, which is sweet, hot and a little sour, accompanies the dish. But a jarred version from the supermarket would certainly work in a pinch.','http://graphics8.nytimes.com/images/2014/03/07/dining/07pakoras/07pakoras-articleLarge.jpg','VG','Indian',NULL,NULL,NULL,'16-18 pieces (about 4-6 servings)','About 1 hour','');
INSERT INTO "recipes" VALUES(15,'Fettuccine With Asparagus And Smoked Salmon','Fresh pasta, asparagus and smoked salmon are tossed with shallot cream sauce in this elegant weeknight dinner that can be prepared in well under an hour.','http://graphics8.nytimes.com/images/2014/05/12/dining/Fettuccine-With-Asparagus-And-Smoked-Salmon/Fettuccine-With-Asparagus-And-Smoked-Salmon-articleLarge.jpg','PS','Italian',NULL,NULL,NULL,'4 servings','35 minutes','');
INSERT INTO "recipes" VALUES(16,'Pasta Alla Norma, My Way','I make pasta alla Norma all the time; you will find more than one recipe from me on the classic tomato and eggplant sauce. But this is my favorite version, created on the spur of the moment and at the suggestion from a friend.','http://graphics8.nytimes.com/images/2014/10/08/dining/08BITTMAN/08BITTMAN-articleLarge.jpg','PS','Italian',NULL,NULL,NULL,'2 sizable or 4 smaller portions','','');
INSERT INTO "recipes" VALUES(17,'Mushroom Lasagna','This lasagna tastes very rich, even though it really isn’t. It combines an olive oil béchamel with a simple mushroom ragout and Parmesan cheese. I prefer no-boil lasagna noodles because they’re lighter than regular lasagna noodles. But I still boil them because I think the results are better if they’re cooked until they’re flexible (a couple of minutes) first.   ','http://graphics8.nytimes.com/images/2011/10/11/science/12recipehealth/12recipehealth-articleLarge-v2.jpg','PS','Italian',NULL,NULL,NULL,'','90 minutes','');
INSERT INTO "recipes" VALUES(18,'Dark Chocolate Pudding','This rich, creamy confection crosses a classic, American, cornstarch-thickened chocolate pudding with a luxurious French egg-yolk-laden chocolate custard called pot de crème. It has a dense, satiny texture and a fudgelike flavor from the combination of bittersweet chocolate, cocoa powder and brown sugar. Make sure to serve it with either whipped cream or crème fraîche for a cool contrast; crème fraîche has the advantage of also adding tang.','http://graphics8.nytimes.com/images/2015/02/03/multimedia/clark-choc-pudding/clark-choc-pudding-mediumThreeByTwo440.jpg','DS','Italian',NULL,NULL,NULL,'8 servings','','');
INSERT INTO "recipes" VALUES(19,'Chicken Stir-Fry With Mixed Peppers','I used green peppers only for this stir-fry. Try to use a mix of hot and sweet peppers, and feel free to use red, yellow or orange ones if you want to introduce some color. The chicken is “velveted” before stir-frying; a good name for this technique as the texture of the chicken remains velvety and moist after stir-frying.','http://graphics8.nytimes.com/images/2013/07/16/science/18recipehealth/18recipehealth-articleLarge.jpg','MT','Asian',NULL,NULL,NULL,'Serves 4','','');
INSERT INTO "recipes" VALUES(20,'New Mexican Pozole','In New Mexico, there is abundance and generosity and plenty of comfort food at holiday parties. Posole, the savory and hearty, rather soupy stew made from dried large white corn kernels simmered for hours, is traditional and easy to prepare. Stir in a ruddy red purée of dried New Mexico chiles to give the stew its requisite kick. This is satisfying, nourishing, fortifying fare. The corn stays a little bit chewy in a wonderful way (canned hominy never does), and the spicy broth is beguiling.','http://graphics8.nytimes.com/images/2013/12/04/dining/04KITCH_SPAN/04KITCH_SPAN-articleLarge.jpg','MT','Mexican',NULL,NULL,NULL,'10 to 12 servings','3 to 4 hours','');
INSERT INTO "recipes" VALUES(21,'Cumin-Baked Pork Chops','Cumin infuses food with a soft, round, gentle warmth. It is like a winter sun that is all the more precious because it''s unexpected. Its warmth is not dissimilar to pepper''s -- in fact, the ancients used it as a substitute -- but cumin has a sweetness and a hint of pale lemon flavor as well. And perhaps because cumin is widely used in sausage, I find a natural affinity between it and all things pork. These delightful baked pork chops underscore the kinship.','http://graphics8.nytimes.com/images/2015/04/29/dining/cumin-baked-pork-chops/cumin-baked-pork-chops-articleLarge.jpg','MT','International',NULL,NULL,NULL,'4 servings','25 minutes','');
INSERT INTO "recipes" VALUES(22,'Braised Pork Chops With Tomatoes, Anchovies and Rosemary','','http://graphics8.nytimes.com/images/2014/04/17/dining/-Braised-Pork-Chops/-Braised-Pork-Chops-articleLarge.jpg','MT','International',NULL,NULL,NULL,'2 servings','35 minutes','');
INSERT INTO "recipes" VALUES(23,'Pan Roasted Pork Chops With Pea Shoot Pesto','','http://graphics8.nytimes.com/images/2014/05/30/dining/Pan-Roasted-Pork-Chops-With-Pea-Shoot-Pesto/Pan-Roasted-Pork-Chops-With-Pea-Shoot-Pesto--articleLarge.jpg','MT','International',NULL,NULL,NULL,'4 servings','1 hour','');
INSERT INTO "recipes" VALUES(24,'Eggplant With Lamb, Tomato and Pine Nuts','With its layers of golden eggplant, cinnamon-scented lamb, and sweet tomato sauce topped with melted cheese, this traditional Lebanese dish is made for celebratory meals and gatherings. Even better, it’s just as good served warm or room temperature as it is hot from the oven. It also reheats well, meaning that you can bake it the day before, and reheat it before serving if you like. Pull it out of the refrigerator, let it come to room temperature for an hour, then reheat it covered for about 40 minutes at 350 degrees.','http://graphics8.nytimes.com/images/2015/05/27/dining/27COOKBOOK3/27COOKBOOK3-articleLarge.jpg','MT','North African',NULL,NULL,NULL,'8 servings','2 hours','');
INSERT INTO "recipes" VALUES(25,'Roast Chicken With Couscous, Dates and Buttered Almonds','Deglet Noors dates shine when they are cooked in chutneys, desserts or North African dishes like this whole roast chicken. The chicken is cooked with fluffy couscous that absorbs the sweetness of dates and the butteriness of toasted almonds. Supermarket Deglet Noors are often dark brown and hard, because they have been kept well past their natural point of ripeness; seek out soft, light-colored ones for the best flavor.','http://graphics8.nytimes.com/images/2015/06/17/dining/17JPRAMADAN3/17JPRAMADAN3-articleLarge.jpg','MT','North African',NULL,NULL,NULL,'4 to 6 servings','90 minutes','');
INSERT INTO "recipes" VALUES(26,'Whole Pot-Roasted Cauliflower With Tomatoes and Anchovies','The English chef April Bloomfield is known for her love of meat, but her vegetable-centric cookbook “A Girl and Her Greens” is stuffed with the produce she discovered while cooking in Mediterranean-influenced kitchens like Chez Panisse and London’s River Cafe. Often, she simply treats a vegetable as if it were meat, like this whole head of cauliflower. Braising it in tomato and anchovies, as if making an Italian pot roast, produces a richly satisfying entree.','http://graphics8.nytimes.com/images/2015/04/29/dining/29COOKBOOK4/29COOKBOOK4-articleLarge.jpg','VG','International',NULL,NULL,NULL,'6 servings as a side dish, 4 as an entree','About 1 hour 15 minutes','');
INSERT INTO "recipes" VALUES(27,'Salmon Roasted in Butter','This simple fish dish is best made with wild salmon, but it works equally well with the farmed sort. It''s astonishingly easy. In a hot oven, melt butter in a skillet until it sizzles, add the salmon, flip, remove the skin, then allow to roast a few minutes more. You''ll have an elegant fish dinner in about 15 minutes. Don''t be afraid to play with herb and fat combinations: parsley, chervil or dill work well with butter; thyme, basil or marjoram with olive oil; or peanut oil with cilantro or mint.','http://graphics8.nytimes.com/images/2015/08/14/dining/14ROASTEDSALMON/14ROASTEDSALMON-articleLarge.jpg','FS','Italian',NULL,NULL,NULL,'4 to 6 servings','15 minutes','');
INSERT INTO "recipes" VALUES(28,'Chicken Scaloppine al Limone','There are many benefits to making paillards (also known as cutlets or scallops). By broadening the meat’s surface area, you increase the amount of meat that browns and becomes crisp during cooking, plus it''s easy, fast and reliable. ','http://graphics8.nytimes.com/images/2014/04/04/dining/Chicken-Scaloppine-al-Limone/Chicken-Scaloppine-al-Limone-articleLarge.jpg','BK','Italian',NULL,NULL,NULL,'','20 minutes','');
INSERT INTO "recipes" VALUES(29,'Chicken Teriyaki','','http://graphics8.nytimes.com/images/2014/04/18/dining/Chicken-Teriyaki/Chicken-Teriyaki-articleLarge.jpg','MT','International',NULL,NULL,NULL,'8 servings','30 minutes','');
INSERT INTO "recipes" VALUES(30,'Chicken Meatballs, Italian Style','','http://graphics8.nytimes.com/images/2014/04/02/dining/chicken-meatballs/chicken-meatballs-articleLarge.jpg','MT','Italian',NULL,NULL,NULL,'8 servings','60 minutes','');
INSERT INTO "recipes" VALUES(31,'Lamb Shank Tagine With Dates','For the best stews, use lamb shanks simmered slowly on the bone. Here, Moroccan seasonings mingle for a bright balance of flavors: sweetness comes from dates and onions, and heat and spice from ginger and cumin. This tagine is traditionally accompanied only by warm whole wheat pita or Arab flatbread. But, if you wish, serve with buttered couscous or even mashed potatoes. Roasted parsnips or wilted mustard greens would harmonize well, too.','http://graphics8.nytimes.com/images/2014/01/07/dining/07KITCH_SPAN/07KITCH_SPAN-articleLarge.jpg','MT','Asian',NULL,NULL,NULL,'4 to 6 servings','3 1/2 hours','');
INSERT INTO "recipes" VALUES(32,'Persian Fried Chicken','Here is a fried chicken recipe that is the best kind of weeknight cooking, with ingredients found quickly at most local grocery stores, whirled in a food processor and then left overnight to turn into something delicious the next evening. A yogurt marinade helps tenderize the boneless, skinless chicken thighs, infusing them with saffron and paprika, and a quick frying lends the meat a crispy, minty coating. You can marinate the chicken for 3 hours or overnight, but you set the timetable depending on whatever else is going on. This chicken will adapt. Make one night, finish the next. That’s living.','http://graphics8.nytimes.com/images/2014/04/15/dining/Persian-Fried-Chicken/Persian-Fried-Chicken-articleLarge.jpg','BK','International',NULL,NULL,NULL,'8 servings','45 minutes','');
CREATE TABLE shop_lists (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	ingredient_fk INTEGER, 
	qty VARCHAR(20), 
	user_fk INTEGER, 
	date_created DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(ingredient_fk) REFERENCES ingredients (id), 
	FOREIGN KEY(user_fk) REFERENCES users (user_id)
);
INSERT INTO "shop_lists" VALUES(1,'all','remember-me',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(2,'all','flour',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(3,'all','all-purpose flour',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(4,'all','light brown sugar',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(5,'all','pomegranate molasses',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(6,'all','tapioca',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(7,'all','organic sugar',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(8,'all','whole wheat flour',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(9,'all','extra-virgin olive oil ',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(10,'all','black pepper',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(11,'all','chicken',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(12,'all','mint',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(13,'all','oil',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(14,'all','plain whole-milk yogurt',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(15,'all','walnut',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(16,'all','cremini mushrooms',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(17,'all','extra virgin olive oil',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(18,'all','fruity red wine',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(19,'all','milk',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(20,'all','no-boil lasagna noodles',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(21,'all','parmesan cheese',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(22,'all','porcini or shiitake mushrooms',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(23,'all','shallot or onion',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(24,'all','shallots',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(25,'all','thyme leaves',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(26,'all','garlic',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(27,'all','lemon',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(28,'all','sage',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(29,'all','anjou pears',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(30,'all','bosc pears',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(31,'all','ground ginger',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(32,'all','butternut squash',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(33,'all','fresh oregano',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(34,'all','onion',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(35,'all','red bell pepper',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(36,'all','zucchini',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(37,'all','unsalted butter',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(38,'all','vegan margarine',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(39,'all','paprika',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(40,'all','saffron',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(41,'all','pepper',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(42,'all','ground cumin',NULL,1,'2015-11-19 23:12:24.339613');
INSERT INTO "shop_lists" VALUES(43,'PROVA2','flour',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(44,'PROVA2','light brown sugar',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(45,'PROVA2','pomegranate molasses',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(46,'PROVA2','tapioca',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(47,'PROVA2','whole wheat flour',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(48,'PROVA2','unsalted butter',NULL,1,'2015-11-20 00:29:57.262691');
INSERT INTO "shop_lists" VALUES(49,'PROVA2','paprika',NULL,1,'2015-11-20 00:29:57.262691');
CREATE TABLE x_recipe_ingredient (
	id INTEGER NOT NULL, 
	recipe_fk INTEGER, 
	ingredient_name VARCHAR(50), 
	ingredient_info VARCHAR(50), 
	quantity VARCHAR(20), 
	measure VARCHAR(20), 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_fk) REFERENCES recipes (recipe_id), 
	FOREIGN KEY(ingredient_name) REFERENCES ingredients (name)
);
INSERT INTO "x_recipe_ingredient" VALUES(37,19,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(38,19,'cilantro',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(39,20,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(40,21,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(41,22,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(42,23,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(43,24,'Parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(46,4,'yellow fleshed potatoes',NULL,'2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(47,4,'garlic',NULL,'8','');
INSERT INTO "x_recipe_ingredient" VALUES(48,4,'salt',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(49,4,'extra-virgin olive oil ',NULL,'1/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(50,5,'extra-virgin olive oil ',NULL,'1 1/2','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(51,5,'onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(52,5,'garlic',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(53,5,'butternut squash',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(54,5,'zucchini',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(55,5,'red bell pepper',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(56,5,'fresh oregano',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(57,5,'ground cumin',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(58,5,'ground origin',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(59,5,'vegan margarine',NULL,'1/2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(60,5,'organic sugar',NULL,'3','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(61,5,'sage',NULL,'1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(62,5,'salt',NULL,'','pinch');
INSERT INTO "x_recipe_ingredient" VALUES(63,5,'whole wheat flour',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(64,6,'quinoa',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(65,6,'water',NULL,'2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(66,6,'celeriac',NULL,'3/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(67,6,'butternut squash',NULL,'3/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(68,6,'onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(69,6,'garlic',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(70,6,'ground sage',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(71,6,'ground thyme',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(72,6,'salt',NULL,'3/4','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(73,6,'pepper',NULL,'1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(74,6,'parsley',NULL,'1/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(75,6,'hazelnuts',NULL,'1/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(76,6,'extra-virgin olive oil ',NULL,'2','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(77,7,'bosc pears',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(78,7,'anjou pears',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(79,7,'pomegranate molasses',NULL,'6','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(80,7,'unsalted butter',NULL,'3','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(81,7,'tapioca',NULL,'3','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(82,7,'light brown sugar',NULL,'3/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(83,7,'ground ginger',NULL,'1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(84,7,'salt',NULL,'1/4','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(85,7,'all-purpose flour',NULL,'1 1/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(86,7,'salt',NULL,'1/4','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(87,7,'unsalted butter',NULL,'10','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(88,8,'butter',NULL,'4','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(89,8,'all-purpose flour',NULL,'1/4','cup');
INSERT INTO "x_recipe_ingredient" VALUES(90,8,'half-and-half',NULL,'2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(91,8,'salt',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(92,8,'pepper',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(93,8,'cayenne',NULL,'1','pinch');
INSERT INTO "x_recipe_ingredient" VALUES(94,8,'nutmeg',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(95,8,'dry lasagna noodles',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(96,8,'broccoli rabe',NULL,'2','pound');
INSERT INTO "x_recipe_ingredient" VALUES(97,8,'garlic',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(98,8,'extra-virgin olive oil ',NULL,'1/2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(99,8,'ricotta',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(100,8,'lemon',NULL,'1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(101,8,'butter',NULL,'4','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(102,8,'parmesan',NULL,'','');
INSERT INTO "x_recipe_ingredient" VALUES(114,2,'vegetable oil','','2','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(115,2,'dried red chiles','small','6 to 8','');
INSERT INTO "x_recipe_ingredient" VALUES(116,2,'snow peas',', trimmed','1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(117,2,'scallion',', trimmed, chopped in 1-inch lengths','1','bunch');
INSERT INTO "x_recipe_ingredient" VALUES(118,2,'garlic',', minced','4','cloves');
INSERT INTO "x_recipe_ingredient" VALUES(119,2,'ginger','grated','1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(120,2,'toasted sesame oil','','1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(121,2,'roasted peanuts','crushed','3','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(122,2,'cilantro','','','');
INSERT INTO "x_recipe_ingredient" VALUES(123,3,'lamb shanks','','3','');
INSERT INTO "x_recipe_ingredient" VALUES(124,3,'salt and pepper','','','');
INSERT INTO "x_recipe_ingredient" VALUES(125,3,'garlic',' cloves, minced','6','');
INSERT INTO "x_recipe_ingredient" VALUES(126,3,'paprika','','1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(127,3,'cumin','ground','','');
INSERT INTO "x_recipe_ingredient" VALUES(128,3,'butter','','2','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(129,3,'onion',', sliced, about 2 cups','1','');
INSERT INTO "x_recipe_ingredient" VALUES(130,3,'saffron','','1','small pinch');
INSERT INTO "x_recipe_ingredient" VALUES(131,3,'cayenne pepper','','1/2','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(132,3,'tomato paste','','1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(133,3,'cinnamon stick','','1','');
INSERT INTO "x_recipe_ingredient" VALUES(134,3,'dried ginger','','2','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(135,3,'dates',', chopped','1/2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(136,3,'golden raisins',', soaked in hot water to soften for 30 minutes and drained','1/2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(137,3,'pomegranate seeds','','1/2','cup');
INSERT INTO "x_recipe_ingredient" VALUES(138,3,' Cilantro sprigs, for garnish','','','');
INSERT INTO "x_recipe_ingredient" VALUES(139,13,'chuck steak',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(140,13,'olive oil',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(141,13,'garlic',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(142,13,'onions',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(143,13,'flour',NULL,'6','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(144,13,'dry red wine',NULL,'4','cups');
INSERT INTO "x_recipe_ingredient" VALUES(145,13,'water',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(146,13,'cloves',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(147,13,'bay leaf',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(148,13,'thyme',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(149,13,'parsley',NULL,'6','');
INSERT INTO "x_recipe_ingredient" VALUES(150,13,'carrots',NULL,'6','');
INSERT INTO "x_recipe_ingredient" VALUES(151,14,'chickpea flour',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(152,14,'flour',NULL,'¾','cup');
INSERT INTO "x_recipe_ingredient" VALUES(153,14,'fine cornmeal',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(154,14,'kosher salt',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(155,14,'baking powder',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(156,14,'turmeric powder',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(157,14,'fresh corn kernels',NULL,'2 ½','cups');
INSERT INTO "x_recipe_ingredient" VALUES(158,14,'cumin seeds',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(159,14,'fennel seeds',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(160,14,'mustard seeds',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(161,14,'chopped fresh red or green chile',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(162,14,'chopped scallions',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(163,14,'chopped cilantro',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(164,14,'grated ginger',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(165,14,'vegetable oil, for frying',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(166,14,'lime wedges',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(167,14,'mango-tamarind chutney',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(168,15,'fresh asparagus, medium thickness',NULL,'½','');
INSERT INTO "x_recipe_ingredient" VALUES(169,15,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(170,15,'butter',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(171,15,'minced shallots',NULL,'½','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(172,15,'heavy cream',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(173,15,'fresh lemon juice',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(174,15,'minced fresh dill',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(175,16,'cherry tomatoes',NULL,'20 to 30','');
INSERT INTO "x_recipe_ingredient" VALUES(176,16,'olive oil',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(177,16,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(178,16,'garlic',NULL,'2','cloves');
INSERT INTO "x_recipe_ingredient" VALUES(179,16,'eggplants',NULL,'12','');
INSERT INTO "x_recipe_ingredient" VALUES(180,16,'pasta',NULL,'300','');
INSERT INTO "x_recipe_ingredient" VALUES(181,16,'ricotta salata',NULL,'2 to 3','');
INSERT INTO "x_recipe_ingredient" VALUES(182,16,'basil',NULL,'20','');
INSERT INTO "x_recipe_ingredient" VALUES(183,17,'porcini or shiitake mushrooms',NULL,'1','ounce');
INSERT INTO "x_recipe_ingredient" VALUES(184,17,'extra virgin olive oil',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(185,17,'shallots',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(186,17,'garlic',NULL,'2 to 3','');
INSERT INTO "x_recipe_ingredient" VALUES(187,17,'cremini mushrooms',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(188,17,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(189,17,'fruity red wine',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(190,17,'thyme leaves',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(191,17,'pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(192,17,'extra virgin olive oil',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(193,17,'shallot or onion',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(194,17,'all-purpose flour',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(195,17,'milk',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(196,17,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(197,17,'pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(198,17,'no-boil lasagna noodles',NULL,'½','pound');
INSERT INTO "x_recipe_ingredient" VALUES(199,17,'parmesan cheese',NULL,'4','ounces');
INSERT INTO "x_recipe_ingredient" VALUES(200,17,'sage',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(201,18,'egg',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(202,18,'bittersweet chocolate',NULL,'6','');
INSERT INTO "x_recipe_ingredient" VALUES(203,18,'unsalted butter',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(204,18,'vanilla extract',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(205,18,'whole milk',NULL,'2 ½','');
INSERT INTO "x_recipe_ingredient" VALUES(206,18,'heavy cream',NULL,'½','');
INSERT INTO "x_recipe_ingredient" VALUES(207,18,'brown sugar',NULL,'⅓','');
INSERT INTO "x_recipe_ingredient" VALUES(208,18,'unsweetened cocoa powder',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(209,18,'cornstarch',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(210,18,'fine sea salt',NULL,'¼','');
INSERT INTO "x_recipe_ingredient" VALUES(211,18,'whipped cream',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(212,18,'chocolate shavings',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(213,18,'flaky sea salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(214,19,'skinless chicken breast',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(215,19,'egg white',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(216,19,'cornstarch',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(217,19,'rice wine',NULL,'1 ½','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(218,19,'sugar',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(219,19,'hoisin sauce',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(220,19,'soy sauce',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(221,19,'peanut oil',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(222,19,'ginger',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(223,19,'garlic',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(224,19,'green peppers',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(225,19,'cashew',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(226,20,'dried hominy',NULL,'1 ½','pounds');
INSERT INTO "x_recipe_ingredient" VALUES(227,20,'dried red new mexico chiles',NULL,'3','ounces');
INSERT INTO "x_recipe_ingredient" VALUES(228,20,'fresh pork belly',NULL,'2','pounds');
INSERT INTO "x_recipe_ingredient" VALUES(229,20,'pork shoulder',NULL,'2','pounds');
INSERT INTO "x_recipe_ingredient" VALUES(230,20,'salt and pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(231,20,'onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(232,20,'bay leaf',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(233,20,'chopped garlic',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(234,20,'cumin seeds',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(235,20,'finely diced white onion',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(236,20,'cilantro',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(237,21,'pork chops',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(238,21,'salt',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(239,21,'dijon mustard',NULL,'4','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(240,21,'cumin seeds',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(241,21,'black pepper',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(242,21,'canola oil',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(243,22,'pork loin',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(244,22,'kosher salt',NULL,'¾','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(245,22,'black pepper',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(246,22,'extra virgin olive oil',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(247,22,'red onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(248,22,'rosemary sprigs',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(249,22,'garlic',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(250,22,'plum tomatoes',NULL,'2','pounds');
INSERT INTO "x_recipe_ingredient" VALUES(251,22,'anchovy fillets',NULL,'6','');
INSERT INTO "x_recipe_ingredient" VALUES(252,22,'polenta, noodles or rice',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(253,23,'pine nuts',NULL,'¾','cup');
INSERT INTO "x_recipe_ingredient" VALUES(254,23,'pea shoots',NULL,'3','cups');
INSERT INTO "x_recipe_ingredient" VALUES(255,23,'cilantro leaves',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(256,23,'parmesan',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(257,23,'garlic',NULL,'2','cloves');
INSERT INTO "x_recipe_ingredient" VALUES(258,23,'kosher salt',NULL,'¾','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(259,23,'extra virgin olive oil',NULL,'⅓','cup');
INSERT INTO "x_recipe_ingredient" VALUES(260,23,'bone-in pork chops',NULL,'4','');
INSERT INTO "x_recipe_ingredient" VALUES(261,23,'garlic',NULL,'1','clove');
INSERT INTO "x_recipe_ingredient" VALUES(262,23,'kosher salt',NULL,'1 ½','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(263,23,'black pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(264,23,'extra virgin olive oil',NULL,'3','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(265,23,'pea shoots',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(266,23,'arugula',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(267,23,'cilantro leaves',NULL,'3','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(268,23,'shallot',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(269,23,'extra virgin olive oil',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(270,23,'lemon juice',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(271,23,'coarse sea salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(272,23,'black pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(273,24,'eggplants',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(274,24,'extra-virgin olive oil',NULL,'4','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(275,24,'kosher salt',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(276,24,'yellow onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(277,24,'garlic',NULL,'2','');
INSERT INTO "x_recipe_ingredient" VALUES(278,24,'ground lamb',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(279,24,'cinnamon',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(280,24,'black pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(281,24,'unsalted butter',NULL,'½','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(282,24,'pine nuts',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(283,24,'tomato sauce',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(284,24,'mozzarella',NULL,'12','ounces');
INSERT INTO "x_recipe_ingredient" VALUES(285,25,'extra-virgin olive oil',NULL,'4','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(286,25,'lemon juice',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(287,25,'ginger',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(288,25,'black pepper',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(289,25,'sea salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(290,25,'chicken',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(291,25,'couscous',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(292,25,'butter',NULL,'3','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(293,25,'almonds',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(294,25,'dates',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(295,25,'sugar',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(296,25,'cinnamon',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(297,25,'orange blossom water',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(298,25,'honey',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(299,25,'mint',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(300,26,'cauliflower',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(301,26,'olive oil',NULL,'5','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(302,26,'garlic',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(303,26,'anchovies',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(304,26,'rosemary leaves',NULL,'¾','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(305,26,'tomatoes',NULL,'1 ½','cups');
INSERT INTO "x_recipe_ingredient" VALUES(306,26,'white wine',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(307,26,'pequin chiles',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(308,26,'flaky salt',NULL,'1','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(309,27,'butter',NULL,'4','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(310,27,'chervil',NULL,'4','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(311,27,'salmon',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(312,27,'lemon wedges',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(313,28,'boneless chicken thighs',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(314,28,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(315,28,'black pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(316,28,'all-purpose flour',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(317,28,'bread crumbs',NULL,'1 ½','cups');
INSERT INTO "x_recipe_ingredient" VALUES(318,28,'eggs',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(319,28,'extra virgin olive oil',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(320,28,'butter',NULL,'3','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(321,28,'dry white wine',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(322,28,'chicken or vegetable stock',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(323,28,'lemon juice',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(324,28,'parsley',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(325,28,'lemon wedges',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(326,29,'soy sauce',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(327,29,'granulated sugar',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(328,29,'brown sugar',NULL,'1 ½','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(329,29,'garlic',NULL,'6','cloves');
INSERT INTO "x_recipe_ingredient" VALUES(330,29,'ginger',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(331,29,'black pepper',NULL,'¼','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(332,29,'cinnamon',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(333,29,'pineapple juice',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(334,29,'chicken thighs',NULL,'8','');
INSERT INTO "x_recipe_ingredient" VALUES(335,29,'cornstarch',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(336,30,'chicken thighs',NULL,'1','pound');
INSERT INTO "x_recipe_ingredient" VALUES(337,30,'parmesan cheese',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(338,30,'parsley leaves',NULL,'¼','cup');
INSERT INTO "x_recipe_ingredient" VALUES(339,30,'onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(340,30,'egg',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(341,30,'salt',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(342,30,'black pepper',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(343,30,'extra virgin olive oil',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(344,30,'all-purpose flour',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(345,30,'lemon wedges',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(346,31,'lamb shanks',NULL,'3','');
INSERT INTO "x_recipe_ingredient" VALUES(347,31,'garlic',NULL,'6','');
INSERT INTO "x_recipe_ingredient" VALUES(348,31,'fresh ginger',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(349,31,'paprika',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(350,31,'cumin',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(351,31,'butter',NULL,'2','tablespoons');
INSERT INTO "x_recipe_ingredient" VALUES(352,31,'onion',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(353,31,'saffron',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(354,31,'cayenne pepper',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(355,31,'tomato paste',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(356,31,'cinnamon stick',NULL,'1','');
INSERT INTO "x_recipe_ingredient" VALUES(357,31,'ginger',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(358,31,'dates',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(359,31,'golden raisins',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(360,31,'pomegranate seeds',NULL,'½','cup');
INSERT INTO "x_recipe_ingredient" VALUES(361,32,'saffron',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(362,32,'plain whole-milk yogurt',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(363,32,'garlic',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(364,32,'chicken',NULL,'2 ½','pounds');
INSERT INTO "x_recipe_ingredient" VALUES(365,32,'flour',NULL,'2','cups');
INSERT INTO "x_recipe_ingredient" VALUES(366,32,'paprika',NULL,'2','teaspoons');
INSERT INTO "x_recipe_ingredient" VALUES(367,32,'mint',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(368,32,'salt',NULL,'1','tablespoon');
INSERT INTO "x_recipe_ingredient" VALUES(369,32,'black pepper',NULL,'½','teaspoon');
INSERT INTO "x_recipe_ingredient" VALUES(370,32,'oil',NULL,'
','');
INSERT INTO "x_recipe_ingredient" VALUES(371,32,'walnut',NULL,'1','cup');
INSERT INTO "x_recipe_ingredient" VALUES(372,32,'lemon',NULL,'1','');
CREATE TABLE recipe_steps (
	id INTEGER NOT NULL, 
	recipe_fk INTEGER, 
	step_description TEXT, 
	step_num INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_fk) REFERENCES recipes (recipe_id)
);
INSERT INTO "recipe_steps" VALUES(10,4,'Bring water to a boil in a large saucepan. Add potatoes, garlic and 2 teaspoons salt and cook at a brisk simmer until potatoes are tender, about 15 minutes.',1);
INSERT INTO "recipe_steps" VALUES(11,4,'Drain potatoes and garlic, reserving 1 cup of cooking liquid. Mash potatoes and garlic, then thin to desired consistency with reserved cooking liquid. Check seasoning. Beat in olive oil and serve.',2);
INSERT INTO "recipe_steps" VALUES(12,4,'',3);
INSERT INTO "recipe_steps" VALUES(13,5,'Preheat oven to 325 degrees.
Heat oil in a wok over medium heat and add onion and garlic and sauté until soft. About 3 minutes.
Prepare the butternut squash by cutting it in half, peeling it, removing the seeds and cutting it into small chunks. Add to the wok and cook for about 4 minutes. Add chopped zucchini, bell pepper and spices. Cook on medium, continually stirring so vegetables don''t burn, for another 5 minutes.',1);
INSERT INTO "recipe_steps" VALUES(14,5,'In a large bowl, combine margarine, sugar, sage and sea salt. Stir in the flour with a fork or your hands and mix until the ingredients form a dough. Add more margarine if the dough does not come together one tablespoon at a time.',2);
INSERT INTO "recipe_steps" VALUES(15,5,'Grease a mini-muffin tray with vegan margarine or olive oil. With your hands, form small balls of dough and work the dough into the muffin tray cavities to form tart shells. Use muffin liners if you desire.
Scoop a small spoonful of vegetables into the tart shells. About a tablespoon full.
Bake for 20-25 minutes and serve immediately.',3);
INSERT INTO "recipe_steps" VALUES(16,6,'Rinse quinoa, pour in a saucepan with 2 cups of water and bring to a boil. Avoid stirring and let boil until the quinoa absorbs all the remaining water, about 10 to 15 minutes. Set aside in a large mixing bowl.',1);
INSERT INTO "recipe_steps" VALUES(17,6,'Heat about a tablespoon of oil in a pan. Add the garlic, onions, butternut squash and celeriac to the oil. Cook on medium, stirring frequently, until veggies are fork tender, about 20 minutes. Once the veggies are softened, add the thyme, sage, salt and pepper and stir coat evenly.',2);
INSERT INTO "recipe_steps" VALUES(18,6,'Add the veggies to the quinoa in a large mixing bowl and stir to combine. Mix in chopped parsley, hazelnuts and olive oil and toss until everything is evenly distributed.',3);
INSERT INTO "recipe_steps" VALUES(19,7,'Preheat oven to 425 degrees. Quarter 6 pears. In a large skillet over medium-high heat, bring 3 tablespoons molasses to a boil. Let simmer about 2 minutes, until molasses thickens. Arrange half the quartered pears in a single layer in skillet. Sprinkle 1 1/2 tablespoons butter over pears. Cook, turning occasionally, until pears are well caramelized on all sides (but not cooked through), about 5 minutes.',1);
INSERT INTO "recipe_steps" VALUES(20,7,'Scrape pears and molasses into a bowl. Add tapioca and toss to combine. Repeat cooking process with remaining molasses, butter and quartered pears. Add second batch of pears to bowl; combine.
Scrape pears and molasses into a bowl. Add tapioca and toss to combine. Repeat cooking process with remaining molasses, butter and quartered pears. Add second batch of pears to bowl; combine.',2);
INSERT INTO "recipe_steps" VALUES(21,7,'Cut remaining dough into strips about 1 inch thick. Top pie with strips, weaving them into a lattice. Crimp edges to seal. Place pie on a foil-lined, rimmed baking sheet.
Bake for 15 minutes; reduce heat to 350 degrees and continue baking until crust is dark golden and pears are tender when pricked with a fork, about 45 minutes more. Let cool for 30 minutes before slicing.',3);
INSERT INTO "recipe_steps" VALUES(22,8,'Make the béchamel: Melt butter in a small saucepan. Whisk in flour and cook for a minute over medium heat without browning. Gradually whisk in half-and-half, 1/2 cup at a time, to obtain a smooth, lightly thickened sauce. Turn heat to low. Add 1/2 teaspoon salt, some ground black pepper, the cayenne and nutmeg. Cook, whisking, for 4 to 5 minutes, then place saucepan in a hot-water bath to keep sauce warm. Thin if necessary with a little more half-and-half.',1);
INSERT INTO "recipe_steps" VALUES(23,8,'Bring a large pot of well-salted water to the boil. Add lasagna noodles and cook for 5 minutes. Lift noodles from water with a spider and rinse well in a bowl of cold water. Drain and lay noodles flat on a kitchen towel.
Using the same cooking water, blanch the greens for 1 minute, until just wilted. Rinse greens with cool water, squeeze dry and chop them roughly. Put 1 cup of chopped greens, the minced garlic and ?1/2 cup olive oil in a food processor or blender and purée to make a pesto. Season with salt and pepper to taste and transfer to a small bowl.',2);
INSERT INTO "recipe_steps" VALUES(24,8,'Mix the ricotta and lemon zest in a small bowl and season with salt and pepper to taste. Heat oven to 375 degrees. Organize to have all ingredients within easy reach for assembling lasagna. Use 2 tablespoons butter to grease an 8-by-10-inch baking dish.
Assemble the lasagna: Put a layer of cooked noodles on the bottom of the baking dish. Spoon a quarter of the béchamel over noodles, then dot with a third of the ricotta. Complete layer with chopped greens, a drizzle of pesto and some grated cheese. Continue layering, finishing with a layer of pasta. Spread the last of the béchamel on top and sprinkle with Parmesan. (There should be 4 layers of pasta and 3 layers of filling.)
Dot with remaining butter and bake, covered with foil, for 20 minutes. Uncover and bake for 20 minutes more, until nicely browned and bubbling. Let lasagna rest 10 minutes before serving.',3);
INSERT INTO "recipe_steps" VALUES(28,2,'Put vegetable oil in a wok over high heat. When oil looks wavy, add chiles and let sizzle for a few seconds.',1);
INSERT INTO "recipe_steps" VALUES(29,2,'Add snow peas and scallions and season well with salt and pepper. Cook vegetables over high heat, stirring constantly, until cooked through and lightly charred, 2 to 3 minutes. Peas should be bright green and crisp-tender.',2);
INSERT INTO "recipe_steps" VALUES(30,2,'Add garlic, ginger and sesame oil, toss well and cook 1 minute more. Transfer to a serving platter and sprinkle with peanuts and cilantro.',3);
INSERT INTO "recipe_steps" VALUES(31,3,'Trim shanks of excess fat, then season generously with salt and pepper. In a small bowl, combine garlic, fresh ginger, paprika and cumin, and smear over shanks. Leave shanks at room temperature to season for at least an hour. (Or you can wrap and refrigerate several hours, or overnight; return to room temperature before proceeding.)',1);
INSERT INTO "recipe_steps" VALUES(32,3,'In a Dutch oven or heavy-bottomed soup pot, melt butter over medium-high heat. Add onion, saffron and cayenne, and sprinkle with salt. Cook for 5 minutes, until somewhat softened. Stir in tomato paste and cook 1 minute. Lower heat to medium, add seasoned shanks and let cook with onions, turning occasionally, until meat and onions are lightly browned, about 10 minutes.',2);
INSERT INTO "recipe_steps" VALUES(33,3,'Heat oven to 400 degrees. Add cinnamon stick, dried ginger, chopped dates and water to barely cover (about 31/2 to 4 cups) to the pot. Bring to a simmer, cover pot with a tightfitting lid and place in oven. Bake for 30 minutes, then turn heat down to 350 degrees. Check sauce and add water if level of liquid is below meat. Continue baking for another hour, checking liquid level occasionally, then test meat by probing with skewer or paring knife. It should be quite tender and almost falling from bone, but cooked no further. (Tagine may be prepared to this point up to two days ahead. Reheat gently in a covered pot on the stovetop, adding a little more water as necessary.)',3);
INSERT INTO "recipe_steps" VALUES(37,13,'Cut the meat into two-inch cubes.',0);
INSERT INTO "recipe_steps" VALUES(38,13,'Using a large skillet, heat the oil and add the beef cubes in one layer. Add salt and pepper and cook, stirring and turning the pieces often, for about 10 minutes.',1);
INSERT INTO "recipe_steps" VALUES(39,13,'Add the garlic and onions and cook, stirring occasionally, for another 10 minutes. Sprinkle with flour and stir to coat the meat evenly.',2);
INSERT INTO "recipe_steps" VALUES(40,13,'Add the wine and stir until the mixture boils and thickens. Stir in the water. Add the cloves, bay leaf, thyme and parsley. Cover closely and simmer for one hour.',3);
INSERT INTO "recipe_steps" VALUES(41,13,'Meanwhile, cut the carrots into one-inch lengths. If the pieces are very large, cut them in half lengthwise. Add them to the beef. Cover and continue cooking for 30 minutes, or until the carrots are tender. Serve the stew sprinkled with chopped parsley.',4);
INSERT INTO "recipe_steps" VALUES(42,14,'In a mixing bowl, combine chickpea flour, all-purpose flour, cornmeal, salt, baking powder and turmeric.',1);
INSERT INTO "recipe_steps" VALUES(43,14,'In a food processor, grind corn kernels to a rough purée. Add purée to flour mixture and stir well to make a stiff batter.',2);
INSERT INTO "recipe_steps" VALUES(44,14,'Put ghee in a small pan over medium-high heat. Add cumin, fennel and mustard seeds. When seeds are lightly toasted and begin to pop, pour mixture into the batter. Add chile, scallions, cilantro and ginger, and stir well. (Batter may be prepared several hours in advance.)',3);
INSERT INTO "recipe_steps" VALUES(45,14,'Pour vegetable oil into a cast-iron skillet to a depth of 1 inch. Heat on medium-high until oil looks wavy. Using two large soup spoons, carefully slip morsels of batter into the oil, working in batches if necessary. Adjust the heat so pakoras brown gently on one side, about 2 minutes. Turn pakoras and brown on other side, about 2 minutes more. Remove with a slotted spoon or spatula and blot on paper towels. Serve hot with lime wedges and mango-tamarind chutney, or another chutney if desired.',4);
INSERT INTO "recipe_steps" VALUES(46,15,'Snap off the ends of the asparagus where they break naturally and peel the stalks. Cut the asparagus on a slant to pieces about an inch long.',1);
INSERT INTO "recipe_steps" VALUES(47,15,'Steam the asparagus until they are just barely tender and still bright green, about three minutes. Rinse under cold water, drain well on paper towels and set aside.',2);
INSERT INTO "recipe_steps" VALUES(48,15,'Bring a large pot of salted water to a boil for the pasta.',3);
INSERT INTO "recipe_steps" VALUES(49,15,'While the water is coming to a boil, melt the butter in a large heavy skillet. Add the shallots and saute until soft but not brown. Stir in the cream and simmer about five minutes, until the cream has thickened somewhat.',4);
INSERT INTO "recipe_steps" VALUES(50,15,'Cut the salmon into slivers, add it to the cream and remove the skillet from the heat. Season with pepper and lemon juice. Add the asparagus.',5);
INSERT INTO "recipe_steps" VALUES(51,15,'When the pot of water is boiling, add the fettuccine, stir it once or twice, then cook two to three minutes after the water has returned to a boil. Drain well.',6);
INSERT INTO "recipe_steps" VALUES(52,15,'Briefly reheat the sauce. Transfer the fettuccine to a warm serving bowl, pour the sauce over it and toss. Sprinkle with dill and serve.',7);
INSERT INTO "recipe_steps" VALUES(53,16,'Heat the oven to 275 degrees. Put the tomatoes in one layer in an ovenproof pan and drizzle them liberally with oil, then salt and sprinkle with thyme sprigs, if using. Roast for about an hour, then stir and roast for another half-hour or so. When tomatoes are shriveled, add garlic, turn down heat to 225 degrees and roast for at least another hour. They should not cook completely dry; if they threaten to overcook, turn the heat down or pull them out. Fish out the garlic if you like.',1);
INSERT INTO "recipe_steps" VALUES(54,16,'Sizzle the eggplant in about 1/4 inch of oil over medium heat. The oil should bubble steadily. Turn eggplant as needed until nicely browned. Drain on paper towels, and when cool enough to handle, cut roughly into strips.',2);
INSERT INTO "recipe_steps" VALUES(55,16,'Meanwhile, bring a large pot of water to boil for the pasta. Add the eggplant to the tomatoes and stir. If the sauce is too thick, thin it with a bit of the pasta water. Cook the pasta and warm a serving bowl. At the bottom of the bowl put half the sauce and half the ricotta salata. Add the pasta and the remaining sauce, cheese and basil and toss.',3);
INSERT INTO "recipe_steps" VALUES(56,17,'Place the dried mushrooms in a glass measuring cup and pour 2 cups boiling water over them. Let soak 30 minutes, while you prepare the other ingredients. Place a strainer over a bowl, line it with cheesecloth or paper towels, and drain the mushrooms. Squeeze the mushrooms over the strainer to extract all the flavorful juices. If using shiitakes, cut away and discard the stems. Then rinse the mushrooms, away from the bowl with the soaking liquid, until they are free of sand. Squeeze dry and set aside. Chop coarsely. Measure out 1 1/2 cups of the soaking liquid and set aside.',1);
INSERT INTO "recipe_steps" VALUES(57,17,'Heat 1 tablespoon olive oil in a large, heavy skillet over medium heat and add the shallots or onion. Cook, stirring often, until tender, 3 to 5 minutes. Add the garlic, stir together for about 30 seconds, then add the fresh and reconstituted mushrooms and salt to taste. Cook, stirring often, until the mushrooms begin to soften and to sweat, about 5 minutes. Add the wine and turn the heat to high. Cook, stirring, until the liquid boils down and glazes the mushrooms, 5 to 10 minutes. Add thyme and stir in the mushroom soaking liquid. Bring to a simmer, add salt, and cook over medium-high heat, stirring often, until the mushrooms are thoroughly tender and fragrant and the surrounding broth has reduced by a little more than half, about 10 to 15 minutes. Remove from the heat, stir in some freshly ground pepper, taste and adjust salt.',2);
INSERT INTO "recipe_steps" VALUES(58,17,'Meanwhile, make the béchamel. Heat the oil over medium heat in a heavy saucepan. Add the shallot or onion and cook, stirring, until softened, about 3 minutes. Stir in the flour and cook, stirring, for about 3 minutes, until smooth and bubbling, but not browned. It should have the texture of wet sand. Whisk in the milk all at once and bring to a simmer, whisking all the while, until the mixture begins to thicken. Turn the heat to very low and simmer, stirring often with a whisk and scraping the bottom and edges of the pan with a rubber spatula, for 10 to 15 minutes, until the sauce is thick and has lost its raw-flour taste. Season with salt and pepper. Strain while hot into the pan with the mushrooms.',3);
INSERT INTO "recipe_steps" VALUES(59,17,'Assemble the lasagna. Heat the oven to 350 degrees Fahrenheit. Oil or butter a 2-quart rectangular baking dish. Bring a large pot of water to a boil, salt generously and add 3 or 4 lasagna noodles, just the number you need for one layer. Cook only until flexible, and using tongs or a skimmer, remove from the pan and set on a kitchen towel to drain. Spoon a thin layer of béchamel and mushrooms over the bottom of the dish. Top with a layer of noodles. Spread a ladleful of the mushroom/béchamel mixture over the noodles and top with a layer of Parmesan. Cook the next layer of noodles and continue to repeat the layers (I get three layers in my pan), ending with a layer of the mushroom/béchamel mixture topped with Parmesan.  Cover with foil and place in the oven. Bake 30 minutes. Remove the foil, and if you want the edges of the noodles crispy and the top lightly browned, continue to bake uncovered for another 5 to 10 minutes. Serve hot or warm.',4);
INSERT INTO "recipe_steps" VALUES(60,18,'In a small heatproof bowl, whisk together egg and yolks. Set aside.',1);
INSERT INTO "recipe_steps" VALUES(61,18,'Place chocolate, butter and vanilla extract in a food processor or blender but don’t turn on.',2);
INSERT INTO "recipe_steps" VALUES(62,18,'In a medium pot, whisk together milk, cream, brown sugar, cocoa, cornstarch and salt until smooth. Bring to a full boil, whisking, and let bubble for 1 to 2 minutes to activate cornstarch. At that point, it will start to thicken, and when it does immediately pull the pot off the heat. (You don’t want to overboil the cornstarch, which can cause it to thin out again.)',3);
INSERT INTO "recipe_steps" VALUES(63,18,'Pour a little of the hot cornstarch mixture into the eggs, stirring constantly to prevent them from curdling, then pour eggs back into the pan with the remaining cornstarch mixture. Cook over low heat, whisking constantly, until mixture just returns to a bare simmer (one bubble is plenty). Immediately pour into the food processor or blender. Run the machine until the pudding is very smooth (the hot milk mixture will melt the chocolate).',4);
INSERT INTO "recipe_steps" VALUES(64,18,'Pour into individual bowls or teacups or 1 large decorative bowl and cover with plastic wrap. Refrigerate until firm and cold, at least 4 hours for individual servings and as many as 8 hours for 1 large bowl. Pudding can be made 3 days ahead. Serve with whipped cream or whipped crème fraîche, decorated with chocolate shavings and a pinch of sea salt, if you like.',5);
INSERT INTO "recipe_steps" VALUES(65,19,'In a large bowl stir together the egg white, cornstarch, 1 1/2 teaspoons of the rice wine or sherry, salt to taste and 1 1/2 teaspoons water. When you can no longer see any cornstarch add the chicken and stir together until coated. Cover the bowl and place in the refrigerator for 30 minutes.',1);
INSERT INTO "recipe_steps" VALUES(66,19,'Combine the remaining rice wine or sherry, the hoisin sauce, soy sauce, and sugar in a small bowl and set it near your wok. ',2);
INSERT INTO "recipe_steps" VALUES(67,19,'Fill a medium-size saucepan with water and bring to a boil. Add 1 tablespoon of the oil and turn the heat down so that the water is at a bare simmer. Carefully add the chicken to the water, stirring so that the pieces don’t clump. Cook until the chicken turns opaque on the surface but is not cooked through, about 1 minute. Drain in a colander set over a bowl.',3);
INSERT INTO "recipe_steps" VALUES(68,19,'Heat a 14-inch flat-bottomed wok or 12-inch steel skillet over high heat until a drop of water evaporates within a second or two when added to the pan. Add the remaining oil by pouring it down the sides of the pan and swirling the pan, then add the garlic, ginger and chile and stir-fry for no more than 10 seconds. Add the peppers and stir-fry for 1 minute. Add the chicken, cashews and hoisin sauce mixture and salt to taste.  Stir-fry for 1 to 2 minutes, until the chicken is cooked through, and serve with grains or noodles.',4);
INSERT INTO "recipe_steps" VALUES(69,20,'Drain soaked hominy and put in large soup pot. Cover with water and bring to boil. Let simmer briskly for 1 hour.',1);
INSERT INTO "recipe_steps" VALUES(70,20,'While hominy is cooking, make red chile purée: Toast dried chiles lightly in cast-iron skillet or stovetop grill, just until fragrant. Wearing gloves, slit chiles lengthwise with paring knife. Remove and discard stems and seeds. Put chiles in saucepan and cover with 4 cups water. Simmer 30 minutes and let cool. In blender, purée chiles to a smooth paste using some cooking water as necessary. Purée should be of milkshake consistency.',2);
INSERT INTO "recipe_steps" VALUES(71,20,'Season pork belly and pork shoulder generously with salt and pepper. After posole has cooked 1 hour, add pork shoulder, pork belly, onion stuck with cloves, bay leaf, garlic and cumin. Add enough water to cover by 2 inches, then return to a brisk simmer. While adding water occasionally and tasting broth for salt, simmer for about 2 1/2 hours more, until meat is tender and posole grains have softened and burst. Skim fat from surface of broth.',3);
INSERT INTO "recipe_steps" VALUES(72,20,'Stir in 1 cup chile purée and simmer for 10 minutes. Taste and correct seasoning. (At this point, posole can be cooled completely and reheated later. Refrigerate for up to 3 days.)',4);
INSERT INTO "recipe_steps" VALUES(73,20,'To serve, ladle posole, meat and broth into wide bowls. Pass bowls of diced onion, lime wedges, cilantro and oregano, and let guests garnish to taste.',5);
INSERT INTO "recipe_steps" VALUES(74,21,'Preheat the oven to 450 degrees. Sprinkle the pork chops on both sides with salt, then brush each side with mustard. Rub the cumin and pepper into the mustard.',1);
INSERT INTO "recipe_steps" VALUES(75,21,'Heat the oil in a large cast-iron skillet over high heat. Add the pork chops and brown for 2 minutes on each side. Put the skillet in the oven and bake until the chops are just cooked through, about 12 minutes. Divide among 4 plates and serve.',2);
INSERT INTO "recipe_steps" VALUES(76,22,'Preheat oven to 350 degrees. Rinse pork chops and pat dry with a paper towel. Season generously with salt and pepper. In a large, ovenproof skillet over medium-high heat, place 1 tablespoon oil. Sear chops until well browned, 3 to 4 minutes a side. Transfer to a plate.',1);
INSERT INTO "recipe_steps" VALUES(77,22,'Add remaining tablespoon oil to skillet and sauté onion and rosemary until onions are golden, about 5 minutes. Add garlic and cook for another minute.',2);
INSERT INTO "recipe_steps" VALUES(78,22,'Add tomatoes, anchovies and remaining salt and pepper and cook, stirring occasionally, until tomatoes begin to break down, about 8 minutes.',3);
INSERT INTO "recipe_steps" VALUES(79,22,'Add pork chops to skillet, spooning sauce over chops. Cover skillet and transfer to oven to bake until a thermometer inserted into center of meat reads 145 degrees, about 15 minutes. Allow chops to rest for 5 minutes in pan. If desired, serve with polenta, noodles or rice to soak up sauce.',4);
INSERT INTO "recipe_steps" VALUES(80,23,'In a small skillet over medium-low heat, toast pine nuts, tossing occasionally, until golden, about 3 minutes.',1);
INSERT INTO "recipe_steps" VALUES(81,23,'To prepare pesto, in a food processor or blender combine pea shoots, 1/2 cup toasted pine nuts, cilantro, Parmesan, garlic and salt. Pulse until roughly chopped. With motor running, slowly drizzle in olive oil; blend until well combined. Scrape pesto into a bowl.',2);
INSERT INTO "recipe_steps" VALUES(82,23,'Heat oven to 350 degrees. Cut each pork chop horizontally in half to bone, making a pocket for stuffing. Rub pork chops all over with cut side of garlic clove, grinding garlic juices into bone and meat. Season chops all over with salt and pepper, and fill each pocket with 1 tablespoon pesto.',3);
INSERT INTO "recipe_steps" VALUES(83,23,'In a very large ovenproof skillet, heat oil over medium-high heat until shimmering. Sear pork chops until well browned, about 3 minutes a side. Transfer skillet to oven. Cook pork chops until they register 140 degrees on an instant-read thermometer, 12 to 15 minutes (or cook pork to taste). Let stand in skillet for 5 minutes.',4);
INSERT INTO "recipe_steps" VALUES(84,23,'Meanwhile, prepare salad: In a large bowl, toss together pea shoots, arugula, remaining 1/4 cup pine nuts, cilantro and shallot. Toss with enough olive oil to lightly coat greens; drizzle with lemon juice and season with salt and pepper.',5);
INSERT INTO "recipe_steps" VALUES(85,23,'Divide salad among 4 serving plates. Place a pork chop on each bed of greens. Top chops with additional pesto. Spoon pan juices over each plate.',6);
INSERT INTO "recipe_steps" VALUES(86,24,'Heat broiler and line a baking sheet with foil or parchment.',1);
INSERT INTO "recipe_steps" VALUES(87,24,'Brush both sides of eggplant slices with 2 tablespoons olive oil and sprinkle with 1 teaspoon salt. Arrange slices on prepared baking sheet and broil in batches until they are deep mahogany brown, turning once halfway through, 5 to 7 minutes per side.',2);
INSERT INTO "recipe_steps" VALUES(88,24,'Adjust the oven to 375 degrees with rack positioned in the center.',3);
INSERT INTO "recipe_steps" VALUES(89,24,'In a large skillet, heat 1 tablespoon of the remaining olive oil over medium heat. Add onion and sauté until translucent, but not browned, stirring occasionally, about 5 minutes. Add garlic and cook until fragrant, about 1 minute. Add ground lamb or beef, stirring frequently and breaking up meat into very small pieces with the side of a metal spoon. Season with remaining teaspoon salt, cinnamon and pepper. Sauté until meat is just cooked through. Taste and add more salt or pepper, or both, as needed.',4);
INSERT INTO "recipe_steps" VALUES(90,24,'In a medium skillet, melt butter over medium heat. Add pine nuts and reduce heat to medium-low. Stir nuts to coat them with butter and continue stirring constantly until nuts are golden brown, 2 to 4 minutes. Keep a close watch over the nuts; they can burn quickly once they begin to brown. Transfer nuts to a bowl while still warm and salt them lightly.',5);
INSERT INTO "recipe_steps" VALUES(91,24,'Coat a 13-by-9-by-2-inch baking dish with remaining 1 tablespoon of olive oil. Spread 1/2 cup of tomato sauce in the bottom of the dish. Lay 1/3 of the eggplant slices in a single layer over the sauce, covering as much surface area of the bottom of the dish as possible. Spoon half the meat evenly over eggplant. Pour 1/3 of the remaining tomato sauce evenly over meat. Sprinkle with 1/3 of the pine nuts. Layer again with eggplant, meat, tomato sauce and pine nuts. Finish with a layer of eggplant and cover with more tomato sauce, sprinkling top with pine nuts.',6);
INSERT INTO "recipe_steps" VALUES(92,24,'Pour 1 cup warm water around the perimeter of the baking dish. (Sauce will thicken as it bakes.) Cover pan with foil and bake for 90 minutes. Remove foil and top eggplant evenly with mozzarella. Bake for 15 minutes longer, uncovered, or until the cheese is bubbling and golden. Serve eggplant warm, over rice.',7);
INSERT INTO "recipe_steps" VALUES(93,25,'Heat oven to 375 degrees. In a large ovenproof dish or pot with a tight lid, combine 2 tablespoons olive oil, the lemon juice, the ginger, the pepper and 1 teaspoon salt. Add the chicken and rub it around in the mixture until evenly coated. Turn chicken breast side down and roast, uncovered, for 50 minutes.',1);
INSERT INTO "recipe_steps" VALUES(94,25,'Meanwhile, in a large bowl, combine couscous, 2 cups water and 1/2 teaspoon salt. Set aside for 5 to 15 minutes to soak.',2);
INSERT INTO "recipe_steps" VALUES(95,25,'In a small skillet, melt the butter. Add almonds and cook, stirring constantly, just until toasted and golden; adjust heat so almonds and butter do not scorch. Turn off heat and stir in dates.',3);
INSERT INTO "recipe_steps" VALUES(96,25,'Add almond-date mixture to couscous, along with any butter left in pan, and mix, fluffing the grains with a fork. Mix in 2 tablespoons olive oil, the sugar, the cinnamon and the orange blossom water (if using).',4);
INSERT INTO "recipe_steps" VALUES(97,25,'Drizzle or paint honey over top of chicken (leave chicken breast-side down in pot). Add couscous mixture to the pot, arranging it around the chicken. Cover tightly with a lid or foil and return to the oven for 30 minutes more.',5);
INSERT INTO "recipe_steps" VALUES(98,25,'Remove from the oven. When cool enough to handle, remove chicken and carve into serving pieces. Stir and fluff couscous, scraping up any chicken skin stuck to bottom of pan, and place chicken pieces back on top of couscous. Sprinkle with chopped herbs and serve immediately.',6);
INSERT INTO "recipe_steps" VALUES(99,26,'Position a rack in the center of the oven and heat to 450 degrees.',1);
INSERT INTO "recipe_steps" VALUES(100,26,'Trim any wilted leaves and brown bits off the cauliflower, but leave healthy leaves. Put the cauliflower on its side on a cutting board. As if coring a tomato, core the base of the cauliflower: insert a small sharp knife about 1 inch into the base of the stem, make a circular cut to loosen the cone-shaped core, then pry it out and discard.',2);
INSERT INTO "recipe_steps" VALUES(101,26,'In a deep, heavy ovenproof pot (with a lid), large enough to hold the whole cauliflower, heat the oil over medium-high heat. Add the cauliflower cored side up; it should sizzle. Brown the exterior, turning it occasionally with tongs for even browning. This should take about 5 minutes; reduce the heat as needed to prevent scorching. Carefully turn over and brown the other side lightly, about 2 minutes.',3);
INSERT INTO "recipe_steps" VALUES(102,26,'Remove the cauliflower to a plate and add garlic, anchovies and rosemary to the pot. Stir until garlic is golden, about 30 seconds. Add tomatoes, white wine, chiles and salt. Stir well and bring to a simmer. Return cauliflower to pot, cored side down. Baste with the tomato liquid and pile some of the solids on top. Simmer, uncovered, 5 minutes to thicken the tomatoes.',4);
INSERT INTO "recipe_steps" VALUES(103,26,'Cover the pot, place in the oven and roast until tender, 30 to 45 minutes; a knife will go into the thick stems with almost no resistance. Check on the tomato sauce every 10 minutes or so; it should be punchy and intense but not too thick, so add a glug of wine if it seems to be getting too dry.',5);
INSERT INTO "recipe_steps" VALUES(104,26,'Transfer the cauliflower head to a serving plate or shallow bowl and cut in half, quarters or thick slices. Spoon on all the tasty stuff left in the pot. Add a drizzle of olive oil and a sprinkle of herbs. Serve immediately or at room temperature, passing salt and red pepper flakes at the table.',6);
INSERT INTO "recipe_steps" VALUES(105,27,'Preheat the oven to 475 degrees. Place the butter and half the herb in a roasting pan just large enough to fit the salmon and place it in the oven. Heat about 5 minutes, until the butter melts and the herb begins to sizzle.',1);
INSERT INTO "recipe_steps" VALUES(106,27,'Add the salmon to the pan, skin side up. Roast 4 minutes. Remove from the oven, then peel the skin off. (If the skin does not lift right off, cook 2 minutes longer.) Sprinkle with salt and pepper and turn the fillet over. Sprinkle with salt and pepper again.',2);
INSERT INTO "recipe_steps" VALUES(107,27,'Roast 3 to 5 minutes more, depending on the thickness of the fillet and the degree of doneness you prefer. Cut into serving portions, spoon a little of the butter over each and garnish with the remaining herb. Serve with lemon wedges.',3);
INSERT INTO "recipe_steps" VALUES(108,28,'Heat the oven to 200. Slice each chicken thigh open like a book and lay it flat between two sheets of plastic wrap. Using a meat pounder, a wine bottle or the bottom of a heavy skillet, pound each piece of chicken to 1/4-inch thickness. Put two large skillets over medium-high heat for a minute or 2. Meanwhile, sprinkle the chicken with salt and pepper and put the flour and bread crumbs on two plates or in two shallow bowls. Beat the eggs in another shallow bowl. Sprinkle all with salt and pepper.',1);
INSERT INTO "recipe_steps" VALUES(109,28,'Add 1 tablespoon each oil and butter to each skillet and swirl it around. When it is hot — a pinch of flour will sizzle — dredge a piece of the chicken in the flour, then dip it in the eggs and finally dredge it in the bread crumbs. Add the chicken piece to one of the pans, then repeat with another piece in the second pan. (You may be able to fit more than one paillard in each pan at a time.)',2);
INSERT INTO "recipe_steps" VALUES(110,28,'Cook the chicken, rotating occasionally and regulating the heat if necessary so it sizzles constantly but doesn’t burn. When the pieces are brown, after about 2 minutes, turn them over.',3);
INSERT INTO "recipe_steps" VALUES(111,28,'Cook on the second side until the chicken is firm to the touch, 1 to 2 minutes. (Cut into one with a thin-bladed knife; the center should be white or slightly pink.) Transfer the chicken to a platter and put it in the oven. Wipe out the pan with a paper towel and repeat with the remaining chicken, adding more oil and butter to each skillet as necessary.',4);
INSERT INTO "recipe_steps" VALUES(112,28,'When all the chicken is cooked, turn off the heat under one of the skillets. Add a tablespoon or 2 more oil or butter to the other pan if it looks dry and sprinkle the fat with 2 teaspoons of the remaining flour. Cook over medium-high heat, stirring, for 3 to 4 minutes. Add the wine and stir and scrape the pan until the wine has reduced by about half, about 1 minute. Add the stock and lemon juice and cook, stirring, until the mixture is slightly thickened and a bit syrupy, another 3 to 4 minutes.',5);
INSERT INTO "recipe_steps" VALUES(113,28,'Add 1 tablespoon butter and swirl the pan around until it melts. Add any juices that have accumulated around the cooked chicken, along with the 1/4 cup parsley. Stir, taste and adjust the seasoning. Spoon the sauce over the chicken, garnish with parsley and serve with lemon wedges.',6);
INSERT INTO "recipe_steps" VALUES(114,29,'In a small saucepan, combine all ingredients except cornstarch and chicken. Bring to boil over high heat. Reduce heat to low and stir until sugar is dissolved, about 3 minutes. Remove from heat and let cool. Discard cinnamon stick and mix in 1/2 cup water.',1);
INSERT INTO "recipe_steps" VALUES(115,29,'Place chicken in a heavy-duty sealable plastic bag. Add soy sauce mixture, seal bag, and turn to coat chicken. Refrigerate overnight.',2);
INSERT INTO "recipe_steps" VALUES(116,29,'Remove chicken and set aside. Pour mixture into a small saucepan. Bring to a boil over high heat, then reduce heat to low. Mix cornstarch with 2 tablespoons water and add to pan. Stir until mixture begins to thicken, and gradually stir in enough water (about 1/2 cup) until sauce is the consistency of heavy cream. Remove from heat and set aside.',3);
INSERT INTO "recipe_steps" VALUES(117,29,'Preheat a broiler or grill. Lightly brush chicken pieces on all sides with sauce, and broil or grill about 3 minutes per side. While chicken is cooking, place sauce over high heat and bring to a boil, then reduce heat to a bare simmer, adding water a bit at a time to keep mixture at a pourable consistency. To serve, slice chicken into strips, arrange on plates, and drizzle with sauce.',4);
INSERT INTO "recipe_steps" VALUES(118,30,'Put chicken in freezer while you prepare other ingredients. Put Parmesan, parsley and onion in a food processor and process until everything is finely chopped. Add egg, chicken and a good sprinkle of salt and pepper, and continue to pulse until the chicken is coarsely ground — finer than chopped, but not much. Shape into one-inch meatballs, pressing no more than necessary.',1);
INSERT INTO "recipe_steps" VALUES(119,30,'Put the oil in a large skillet over medium heat. One by one, dredge the meatballs in the flour and add to the oil. Cook, turning as necessary, until nicely browned all over, 10 to 15 minutes. Serve hot or at room temperature, with lemon wedges.',2);
INSERT INTO "recipe_steps" VALUES(120,31,'Trim shanks of excess fat, then season generously with salt and pepper. In a small bowl, combine garlic, fresh ginger, paprika and cumin, and smear over shanks. Leave shanks at room temperature to season for at least an hour. (Or you can wrap and refrigerate several hours, or overnight; return to room temperature before proceeding.) 
',1);
INSERT INTO "recipe_steps" VALUES(121,31,'In a Dutch oven or heavy-bottomed soup pot, melt butter over medium-high heat. Add onion, saffron and cayenne, and sprinkle with salt. Cook for 5 minutes, until somewhat softened. Stir in tomato paste and cook 1 minute. Lower heat to medium, add seasoned shanks and let cook with onions, turning occasionally, until meat and onions are lightly browned, about 10 minutes. 
',2);
INSERT INTO "recipe_steps" VALUES(122,31,'Heat oven to 400 degrees. Add cinnamon stick, dried ginger, chopped dates and water to barely cover (about 31/2 to 4 cups) to the pot. Bring to a simmer, cover pot with a tightfitting lid and place in oven. Bake for 30 minutes, then turn heat down to 350 degrees. Check sauce and add water if level of liquid is below meat. Continue baking for another hour, checking liquid level occasionally, then test meat by probing with skewer or paring knife. It should be quite tender and almost falling from bone, but cooked no further. (Tagine may be prepared to this point up to two days ahead. Reheat gently in a covered pot on the stovetop, adding a little more water as necessary.) 
',3);
INSERT INTO "recipe_steps" VALUES(123,31,'Remove meat from pot and place in deep, wide serving bowl. Skim off any surface fat from cooking liquid in pot. Add whole dates to pot and simmer for a few minutes to reduce sauce slightly. Pour sauce and dates over meat. To serve, garnish with raisins, pomegranate seeds and cilantro sprigs.
',4);
INSERT INTO "recipe_steps" VALUES(124,32,'In a small bowl, combine saffron with 1 tablespoon water and let soak 10 minutes. Place in food processor with yogurt and garlic and purée until smooth and yellow. Place chicken in glass or ceramic bowl; pour yogurt mixture on top, turn to coat; cover and refrigerate at least 3 hours or overnight.',1);
INSERT INTO "recipe_steps" VALUES(125,32,'In a medium bowl, combine flour, paprika, mint, salt and pepper. Heat a generous half-inch oil in a deep skillet over medium heat. Drop in a bit of bread to test temperature; oil should bubble vigorously. Working in batches to avoid crowding, dredge chicken pieces in flour mixture, then fry until golden brown on both sides, about 7 minutes a side. Remove and drain on paper towels.',2);
INSERT INTO "recipe_steps" VALUES(126,32,'Sprinkle with salt and serve immediately, topped with walnuts and lemon wedges.',3);
CREATE TABLE x_recipe_user (
	id INTEGER NOT NULL, 
	user_fk INTEGER, 
	recipe_fk INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_fk) REFERENCES users (user_id), 
	FOREIGN KEY(recipe_fk) REFERENCES recipes (recipe_id)
);
INSERT INTO "x_recipe_user" VALUES(4,1,4);
INSERT INTO "x_recipe_user" VALUES(5,1,5);
INSERT INTO "x_recipe_user" VALUES(6,1,6);
INSERT INTO "x_recipe_user" VALUES(7,1,7);
INSERT INTO "x_recipe_user" VALUES(8,1,8);
INSERT INTO "x_recipe_user" VALUES(9,1,9);
INSERT INTO "x_recipe_user" VALUES(10,1,10);
INSERT INTO "x_recipe_user" VALUES(13,1,13);
INSERT INTO "x_recipe_user" VALUES(14,1,14);
INSERT INTO "x_recipe_user" VALUES(15,1,15);
INSERT INTO "x_recipe_user" VALUES(16,1,16);
INSERT INTO "x_recipe_user" VALUES(17,1,17);
INSERT INTO "x_recipe_user" VALUES(18,1,18);
INSERT INTO "x_recipe_user" VALUES(19,1,19);
INSERT INTO "x_recipe_user" VALUES(20,1,20);
INSERT INTO "x_recipe_user" VALUES(21,1,27);
INSERT INTO "x_recipe_user" VALUES(22,1,21);
INSERT INTO "x_recipe_user" VALUES(23,1,22);
INSERT INTO "x_recipe_user" VALUES(24,1,23);
INSERT INTO "x_recipe_user" VALUES(25,1,24);
INSERT INTO "x_recipe_user" VALUES(26,1,25);
INSERT INTO "x_recipe_user" VALUES(27,1,26);
INSERT INTO "x_recipe_user" VALUES(28,1,28);
INSERT INTO "x_recipe_user" VALUES(29,1,29);
INSERT INTO "x_recipe_user" VALUES(30,1,30);
INSERT INTO "x_recipe_user" VALUES(31,1,31);
INSERT INTO "x_recipe_user" VALUES(32,1,32);
CREATE TABLE meals (
	meal_id INTEGER NOT NULL, 
	meal_type VARCHAR(20), 
	recipe_fk INTEGER, 
	user_fk INTEGER, 
	portions INTEGER, 
	date_planned DATETIME NOT NULL, 
	week_planned INTEGER, 
	list_fk VARCHAR(50), 
	PRIMARY KEY (meal_id), 
	FOREIGN KEY(recipe_fk) REFERENCES recipes (recipe_id), 
	FOREIGN KEY(user_fk) REFERENCES users (user_id)
);
INSERT INTO "meals" VALUES(2,'lunch',5,1,6,'2015-11-09 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(3,'dinner',8,1,6,'2015-11-09 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(4,'snack',4,1,6,'2015-11-10 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(5,'breakfast',7,1,6,'2015-11-10 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(6,'lunch',6,1,6,'2015-11-10 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(7,'lunch',4,1,4,'2015-11-11 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(8,'dinner',6,1,'','2015-11-11 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(9,'breakfast',5,1,6,'2015-11-12 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(11,'lunch',6,1,6,'2015-11-13 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(12,'breakfast',18,1,6,'2015-11-13 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(13,'dinner',9,1,6,'2015-11-13 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(14,NULL,NULL,1,NULL,'2015-11-13 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(15,'lunch',4,1,'','2015-11-15 00:00:00.000000',45,NULL);
INSERT INTO "meals" VALUES(16,'breakfast',18,1,6,'2015-11-16 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(17,'lunch',8,1,6,'2015-11-16 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(18,'dinner',14,1,6,'2015-11-16 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(19,'lunch',6,1,6,'2015-11-17 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(20,'dinner',27,1,6,'2015-11-18 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(21,'lunch',4,1,6,'2015-11-18 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(22,'breakfast',18,1,6,'2015-11-18 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(23,'dinner',32,1,6,'2015-11-19 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(24,'lunch',17,1,6,'2015-11-19 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(25,'breakfast',7,1,7,'2015-11-19 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(26,'lunch',5,1,6,'2015-11-20 00:00:00.000000',46,NULL);
INSERT INTO "meals" VALUES(27,'lunch',4,1,5,'2015-11-20 00:00:00.000000',46,NULL);
CREATE TABLE expences (
id INTEGER NOT NULL, 
store VARCHAR(50) NOT NULL, 
total REAL, 
date_of_purchase DATE NOT NULL, 
user_fk INTEGER,
PRIMARY KEY (id), 
FOREIGN KEY(user_fk) REFERENCES users (user_id)
);
INSERT INTO "expences" VALUES(1,'Safeway',99.26,'2015-11-14 00:00:00.000000',1);
INSERT INTO "expences" VALUES(2,'Whole Food',46.0,'2015-11-15 00:00:00.000000',1);
INSERT INTO "expences" VALUES(3,'Whole Food',35.89,'2015-11-10 00:00:00.000000',1);
INSERT INTO "expences" VALUES(4,'Safeway',28.45,'2015-11-14 00:00:00.000000',1);
INSERT INTO "expences" VALUES(5,'Trader''s Joe',99.26,'2015-11-15 00:00:00.000000',1);
INSERT INTO "expences" VALUES(6,'Safeway',47.36,'2015-11-10 00:00:00.000000',1);
INSERT INTO "expences" VALUES(7,'Trader''s Joe',106.0,'2015-11-03 00:00:00.000000',1);
INSERT INTO "expences" VALUES(8,'Safeway',250.0,'2015-10-14 00:00:00.000000',1);
COMMIT;
