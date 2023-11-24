import scrapy
import re

class PokedexSpider(scrapy.Spider):
# 1. Configuration de base
    name = "pokedex"  # nom du scraper
    allowed_domains = ["scrapeme.live"]  # le domaine scrapé
    start_urls = ["https://scrapeme.live/shop"]  # url sur lequel on démarre

# 2. Récupère les liens et indique le comportement qu'on attend sur les liens
    def parse(self, response):
        # sélectionner les éléments Pokemon
        pokemons = response.css('li.product')

        for pokemon in pokemons:
            link = pokemon.css('.woocommerce-LoopProduct-link.woocommerce-loop-product__link::attr(href)').get()
            yield response.follow(url=link, callback=self.parse_poke_page)

        # pagination
        next_page = response.css('.page-numbers a.next::attr(href)').get()
        # condition : s'il y a une page suivante...
        if next_page:
            # suit la page suivante
            yield response.follow(url=next_page, callback=self.parse)

# 3. Scraper des données sur des pages détaillées
    def parse_poke_page(self, response):
        # extraire les données

        dimensions = response.css('.product_dimensions::text').get()
        #  je donne directment la valeur None à L x l x H
        length = width = height = None
        # condition : si dimensions n'est pas None, alors attribut les valeurs fournit dans le site
        if dimensions is not None:
            # TODO: aidé avec GPT (revoir RegEx)
            # extraire les dimensions individuelles (regex)
            dimension_values = re.findall(r'\d+\.\d+|\d+', dimensions)
            # assigne les valeurs à L, l et H 
            length = dimension_values[0] if dimension_values else None
            width = dimension_values[1] if len(dimension_values) > 1 else None
            height = dimension_values[2] if len(dimension_values) > 2 else None

        # retourne les données
        yield {
            'name': response.css('.product_title::text').get(),
            'price': response.css('p.price span.woocommerce-Price-amount::text').get(),
            'descript': response.css('.woocommerce-product-details__short-description p::text').get(),
            'tags': response.css('span.tagged_as a::text').getall(),
            'categories': response.css('.posted_in a::text').getall(),
            'sku': response.css('p.in-stock::text').get(),
            'weight': response.css('.product_weight::text').get(),
            'length' : length,
            'width' : width,
            'height' : height
        }