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
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

# 3. Scraper des données sur des pages détaillées
    def parse_poke_page(self, response):
        # extraire les données
        dimensions = response.css('.product_dimensions::text').get()  # voir le RegexOne

        # retourne les données
        result = {
            'name': response.css('.product_title::text').get(),
            'price': response.css('p.price span.woocommerce-Price-amount::text').get(),
            'descript': response.css('.woocommerce-product-details__short-description p::text').get(),
            'tags': response.css('span.tagged_as a::text').getall(),
            'categories': response.css('.posted_in a::text').getall(),
            'sku': response.css('p.in-stock::text').get(),
            'weight': response.css('.product_weight::text').get(),
            # 'dimensions': dimensions
        }

        # TODO: aidé avec GPT (revoir RegEx)
        # extraire les dimensions individuelles (regex)
        dimension_values = re.findall(r'\d+\.\d+|\d+', dimensions)

        # assigne les valeurs à L, l et H 
        result['length'] = dimension_values[0] if dimension_values else None
        result['width'] = dimension_values[1] if len(dimension_values) > 1 else None
        result['height'] = dimension_values[2] if len(dimension_values) > 2 else None

        yield result