from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose, Join
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from time import sleep
import random
 

class Periodico(Item):
    titular = Field()
    fecha = Field()
    hora = Field()

class elComercio(CrawlSpider):
    name = "elComercio"
    allowed_domains = ['elcomercio.pe'] # Me aseguro que no irán a páginas que no sean de este dominio
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_EXPORT_FIELDS': ["titular","fecha","hora"],
        #'CLOSESPIDER_PAGECOUNT': 35,
        #'CLOSESPIDER_ITEMCOUNT': 20,
        'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes
    }

    download_delay = sleep(random.uniform(2.0, 3.0))

    start_urls = [
            'https://elcomercio.pe/buscar/a/politica/ascendente/' + str(i) for i in range(421, 1668)
            ]


    rules = (
        #paginación
        Rule(
            LinkExtractor(
                allow = ()
            ),
            callback = 'parse_items',follow= True
        ),
    )


    def parse_items(self, response):
        sel = Selector(response)
        opiniones = sel.xpath('//div[@class="paginated-list paginated-list--search"]/div[@class="story-item w-full pr-20 pl-20 pb-20 mb-20 border-b-1 border-solid border-gray md:pl-0 md:pr-0  lg:p-0 "]')

        for opinion in opiniones:
            item = ItemLoader(Periodico(), opinion)
            ## condición if para dos paths diferentes

            item.add_xpath('titular', 'div/div/div[2]/h2/a/text()')
            item.add_xpath('fecha', 'div/div/div[1]/p/span[1]/text()')
            item.add_xpath('hora', 'div/div/div[1]/p/span[3]/text()')

            yield item.load_item()

    
process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # formato del archivo generado
    'FEED_URI': '../data/elComercio5.json',  # nombre del archivo generado
    'FEED_EXPORT_ENCODING': 'utf-8'
    })
process.crawl(elComercio)
process.start() # the script will block here until the crawling is finished
