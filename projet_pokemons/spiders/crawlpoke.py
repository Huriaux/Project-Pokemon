import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ProjetPokemonsItem
from scrapy.loader import ItemLoader


class CrawlpokeSpider(CrawlSpider):
    name = "crawlpoke"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop"]

    rules = (Rule(LinkExtractor(restrict_css=".woocommerce-LoopProduct-link.woocommerce-loop-product__link"), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_css=".page-numbers a.next"))
             )

    def parse_item(self, response):
        # je remplace toute cette partie là...
#         '''
#         name = response.css('.product_title::text').get()
#         price = response.css('p.price span.woocommerce-Price-amount::text').get()
#         descript = response.css('.woocommerce-product-details__short-description p::text').get()
#         tags = response.css('span.tagged_as a::text').getall()
#         categories = response.css('.posted_in a::text').getall()
#         sku = response.css('p.in-stock::text').get()
#         weight = response.css('.product_weight::text').get()

#         project = ProjetPokemonsItem()
#         project['name'] = name
#         project['price'] = price
#         project['descript'] = descript
#         project['tags'] = tags
#         project['categories'] = categories
#         project['sku'] = sku
#         project['weight'] = weight
#         '''
        # par ceci :
        # on extrait les dimensions, donc ça change pas
        dimensions = response.css('.product_dimensions::text').get()

        # on initialise un ItemLoader avec le modèle ProjetPokemonsItem() et la réponse actuelle
        l = ItemLoader(item=ProjetPokemonsItem(), response=response)

        # ajouter les champs
        l.add_css("name", '.product_title::text')
        l.add_css("price", 'p.price span.woocommerce-Price-amount::text')
        l.add_css("descript", '.woocommerce-product-details__short-description p::text')
        l.add_css("tags", 'span.tagged_as a::text')
        l.add_css("categories", '.posted_in a::text')
        l.add_css("sku", 'p.in-stock::text')
        l.add_css("weight", '.product_weight::text')

        # ici ça change pas non plus
        if dimensions and isinstance(dimensions, str):
            dimension_values = re.findall(r'\d+\.\d+|\d+', dimensions)
            # modification de l'ajout des valeurs des dimensions => ItemLoader
            l.add_value("length", dimension_values[0] if dimension_values else None)
            l.add_value("width", dimension_values[1] if len(dimension_values) > 1 else None)
            l.add_value("height", dimension_values[2] if len(dimension_values) > 2 else None)
        else:
            # ajout des valeurs nulles
            l.add_value("length", None)
            l.add_value("width", None)
            l.add_value("height", None)

        return l.load_item()