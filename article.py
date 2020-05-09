# -*- coding: utf-8 -*-
import scrapy
import json

from wk_daily.items import articles, article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    def parse(self, response):
        host = self.allowed_domains[0]
        contador = 1 
        
        for link in response.css(".featured_article_metadata > a"):
            link = f"{link.attrib.get('href')}"
            title = link
            yield response.follow(link,callback=self.parse_detail,meta={'link':link, 'contador':contador})
            
            contador = contador + 1 
            if contador > 25: 
                break;  # deja de leer links

    def parse_detail(self, response):
        items = articles()
        item = article()
        
        item["title"] = response.css('title::text').extract()
        item["paragraph"] = list()
        
        for text in response.css(".mw-parser-output > p::text").extract():
            item["paragraph"].append(text)
            if ".\n" in text:
                break;
                
        items["body"] = item
        items["link"] = response.meta["link"]
       
        if response.meta["contador"] ==1:
            fout = ({
                'Link' : items["link"],
                'Body' : {
                    'Title': item["title"],
                    'Paragraph':item["paragraph"]}
            })
            
            with open('output.json','w') as jsonFile:
                json.dump(fout, jsonFile)
            
        return items