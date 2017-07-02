# -*- coding: utf-8 -*-
import scrapy


class CryptoWatchSpider(scrapy.Spider):
    name = 'cryptowatch'
    allowed_domains = ['cryptowat.ch']
    start_urls = ['https://cryptowat.ch/']

    def parse(self, response):
        for exchange in response.css("div.rankings-footer__menu-item"):
            yield {
                'exchange' : exchange.css("div.rankings-footer__menu-item__title::text").extract()
                , 'pair' : exchange.css("a.rankings-footer__menu-item__listing > div.rankings-footer__menu-item__listing__pair::text").extract()
                , 'price' : exchange.css("a.rankings-footer__menu-item__listing > div.rankings-footer__menu-item__listing__price::text").extract()
            }
