# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetPokemonsItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    descript = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    sku = scrapy.Field()
    weight = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()