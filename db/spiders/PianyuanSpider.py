import scrapy

class PianyuanSpider(scrapy.Spider):
    name = "pianyuanspider"
    start_urls = [ "http://pianyuan.net/mv" ]

    def parse(self, response):
        for link in response.css("h5 a"):
            title = link.css("::text").extract_first()
            pianyuan_link = response.urljoin(link.css("::attr(href)").extract_first())
            yield {
                "title": title,
                "pianyuan_link": pianyuan_link
            }
