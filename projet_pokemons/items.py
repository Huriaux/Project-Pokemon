# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# nettoyer les données
from scrapy.loader.processors import Join, MapCompose, TakeFirst
# Join : pemret de joindre toute les valeurs d'un éléments en une seule chaine de caractère
# MapCompose : permet d'appliquer des fonctions et des méthodes sur la valeur
# TakeFirst : en cas de liste permet de récupérer la premier valeur

# permet d'enlever les éventuelles fioritures qu'il pourrait y avoir, par exemple des balises html qui serait resté par mégarde.
from w3lib.html import remove_tags

# pour que tous les mots commences par une Maj. et on renvoi le nom de la focntion dans 'input_processor=MapCompose()'
def clean_tags(tags_value):
    tags = tags_value.title().strip()
    return str(tags)

def clean_categories(categories_value):
    categories = categories_value.title().strip()
    return str(categories)

def clean_sku(sku_value):
    sku = sku_value.replace(' in stock', '').strip()
    return int(sku)

def clean_weight(weight_value):
    weight = weight_value.replace(' kg', '').strip()
    return float(weight)


class ProjetPokemonsItem(scrapy.Item):
    name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(str.strip, float), output_processor=TakeFirst())
    descript = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    tags = scrapy.Field(input_processor=MapCompose(clean_tags), output_processor=Join(', '))
    categories = scrapy.Field(input_processor=MapCompose(clean_categories), output_processor=Join(', '))
    sku = scrapy.Field(input_processor=MapCompose(clean_sku),output_processor=TakeFirst())
   
    weight = scrapy.Field(input_processor=MapCompose(clean_weight), output_processor=TakeFirst())
    length = scrapy.Field(input_processor=MapCompose(str.strip, int), output_processor=TakeFirst())
    width = scrapy.Field(input_processor=MapCompose(str.strip, int), output_processor=TakeFirst())
    height = scrapy.Field(input_processor=MapCompose(str.strip, int), output_processor=TakeFirst())


# VOILÀ COMMENT APPARAISSENT LES VALEURS DANS LA CONSOLE :
# (AVANT)
# 2023-11-25 15:42:30 [scrapy.core.scraper] DEBUG: Scraped from <200 https://scrapeme.live/shop/Stakataka/>
# {'categories': (['Pokemon', 'Rampart'],),
#  'descript': ('When stone walls started moving and attacking, the brute’s true '
#               'identity was this mysterious life-form, which brings to mind an '
#               'Ultra Beast.',),
#  'height': '18',
#  'length': '18',
#  'name': 'Stakataka',
#  'price': ('190.00',),
#  'sku': ('210 in stock',),
#  'tags': (['Beast Boost', 'Rampart', 'stakataka'],),
#  'weight': ('1807.8 kg',),
#  'width': '18'}

# (APRÈS)
# 2023-11-25 19:16:31 [scrapy.core.scraper] DEBUG: Scraped from <200 https://scrapeme.live/shop/Stakataka/>
# {'categories': 'Pokemon, Rampart',
#  'descript': 'When stone walls started moving and attacking, the brute’s true '
#              'identity was this mysterious life-form, which brings to mind an '
#              'Ultra Beast.',
#  'height': 18,
#  'length': 18,
#  'name': 'Stakataka',
#  'price': 190.0,
#  'sku': 210,
#  'tags': 'Beast Boost, Rampart, Stakataka',
#  'weight': 1807.8,
#  'width': 18}