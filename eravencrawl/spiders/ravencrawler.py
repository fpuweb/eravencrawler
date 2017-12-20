# -*- coding: utf-8 -*-
import urlparse
import scrapy

class RavencrawlerSpider(scrapy.Spider):
    name = 'ravencrawler'
    allowed_domains = ['eraven.franklinpierce.edu']
    start_urls = ['http://eraven.franklinpierce.edu/']

    def parse(self, response):
       
        #Extract article information
		titles = response.xpath('//item/title/text()').extract()
        links = response.xpath("//item/link/text()").extract()
        date = response.xpath('//item/pubDate/text()').extract()
		
        #Give the extracted content row wise
        for item in zip(titles,links,date,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'titles' : item[0],
                'links' : item[1],
                'date' : item[2],
            }
            #yield or give the scraped info to scrapy
            yield scraped_info
