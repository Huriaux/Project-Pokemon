# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetPokemonsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class PokeItem(scrapy.item):
    name = scrapy.Field()
    price = scrapy.Field()
    descript = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    sku = scrapy.Field()
    weight = scrapy.Field()
    dimensions = scrapy.Field()
    dimensions = scrapy.Field()