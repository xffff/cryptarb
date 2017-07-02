# -*- coding: utf-8 -*-
import scrapy


class CryptoWatchSpider(scrapy.Spider):
    name = 'cryptowatch'
    allowed_domains = ['cryptowat.ch']
    start_urls = ['https://cryptowat.ch/']

    def parse(self, response):
        for exchange in response.css("div.rankings-footer__menu-item__title"):
            yield {
                'exchange' : rate.css("div::text").extract_first(),
            }
            
