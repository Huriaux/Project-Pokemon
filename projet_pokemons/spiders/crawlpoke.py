import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlpokeSpider(CrawlSpider):
    name = "crawlpoke"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop"]

    rules = (Rule(LinkExtractor(restrict_css=".woocommerce-LoopProduct-link.woocommerce-loop-product__link"), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_css=".page-numbers a.next"))
             )

    def parse_item(self, response):
        dimensions = response.css('.product_dimensions::text').get()
        length = width = height = None
        if dimensions is not None:
            dimension_values = re.findall(r'\d+\.\d+|\d+', dimensions)

            length = dimension_values[0] if dimension_values else None
            width = dimension_values[1] if len(dimension_values) > 1 else None
            height = dimension_values[2] if len(dimension_values) > 2 else None


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

