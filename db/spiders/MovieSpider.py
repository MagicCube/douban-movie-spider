import json
import scrapy

class MovieSpider(scrapy.Spider):
    name = "moviespider"
    start_urls = [ "http://api.douban.com/v2/movie/search?q=%E6%8C%87%E7%8E%AF%E7%8E%8B" ]

    def parse(self, response):
        result = self.parse_json(response)
        subjects = [ result["subjects"][0] ]
        for subject in subjects:
            id = subject["id"]
            url = "http://api.douban.com/v2/movie/subject/%s" % id
            yield scrapy.Request(url, callback=self.parse_movie_subject)

    def parse_movie_subject(self, response):
        result = self.parse_json(response)
        yield result

    def parse_json(self, response):
        return json.loads(response.body_as_unicode())
