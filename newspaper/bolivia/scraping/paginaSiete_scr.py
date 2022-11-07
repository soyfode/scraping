from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
 

class Periodico(Item):
    titulo = Field()
    fecha = Field()
    hora = Field()

class paginaSiete(CrawlSpider):
    name = "PáginaSiete"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_EXPORT_FIELDS': ["titulo","fecha","hora"],
        #'CLOSESPIDER_PAGECOUNT': 20,
        #'CLOSESPIDER_ITEMCOUNT': 20,
        'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes
    }

    download_delay = 1

    # Me aseguro que no irán a páginas que no sean de este dominio
    allowed_domains = ['www.paginasiete.bo']

    start_urls = [
            'https://www.paginasiete.bo/archivo/-/search/%5E/false/false/19700101/20221104/date/false/false/c2VjdGlvbk5hbWU6MMKnODBjMWViODktYTdmZC00M2EwLThhOTQtZmYwOTQ5Njg2MmQwKg%3D%3D/0/meta/0/13431522-106982-8969384-107102-106974-106980-106990-106992-265456-234764-13433769-106986-106978-106976-106988-235476-229328-106984-3665695-11675327-229325/0/' + str(i) for i in range(4313,4316)
            ]

    rules = (
        #paginación
        Rule(
            LinkExtractor(
                allow = r'/archivo/-/search/%5E/false/false/19700101/20221104/date/false/false/c2VjdGlvbk5hbWU6MMKnODBjMWViODktYTdmZC00M2EwLThhOTQtZmYwOTQ5Njg2MmQwKg%3D%3D/0/meta/0/13431522-106982-8969384-107102-106974-106980-106990-106992-265456-234764-13433769-106986-106978-106976-106988-235476-229328-106984-3665695-11675327-229325/0/\d+'
            ), follow = True, callback = 'parse_items'
        ),
    )

    def quitarEspacio(self, fecha):
        fecha = fecha.replace('\n', '')
        return fecha.strip()

    def espacio(self, hora):
        return hora.strip()

    def parse_items(self, response):
        item = ItemLoader(Periodico(), response)

        item.add_xpath('titulo', '//*[@id="3128922993"]/ul/li/div/div[3]/div[2]/a/h2/text()',
                        MapCompose(self.espacio)
        )
        item.add_xpath('fecha', '//*[@id="3128922993"]/ul/li/div/div[1]/text()',
                        MapCompose(self.quitarEspacio)
        )
        item.add_xpath('hora', '//div[@class="hour"]/h2/text()',
                        MapCompose(self.espacio)
        )

        yield item.load_item()

process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # formato del archivo generado
    'FEED_URI': './data/paginaSiete3.json',  # nombre del archivo generado
    'FEED_EXPORT_ENCODING': 'utf-8'
    })
process.crawl(paginaSiete)
process.start() # the script will block here until the crawling is finished
