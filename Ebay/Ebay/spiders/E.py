import json
import re
import scrapy
import re

class ESpider(scrapy.Spider):
    name = "E"
    start_urls = ["https://www.ebay.com/itm/255425870152?itmmeta=01J2BTZN2W81ZQHKEX339VSSK8&hash=item3b78917948:g"
                  ":kZ8AAOSwdVxg9Suh&itmprp=enc%3AAQAJAAAA0B8F4KNrhkxcaSD%2BYisfUjvlC9WuIolIQo3o1Q52ZodsWIOVy%2Bgb"
                  "KIb7g7IkZkuDKXFYq85D%2F35T%2BNI7LSysbmxYzAcpFthhZgxMFHnHE%2F91FcukIA%2FLuGC84b7jOfZqMcrTFCxznc11h"
                  "xZFvtrYpDNm0MPi6FQAtz1sDsfJg0tUIvPhelAkMyIcUdX%2FxrHIbG0%2FoABKDSlVuhQ5CFLhoMWuHbGlhnlGT%2BHkBZkMZ"
                  "bDk0Cf8tUzUHn5tgMe2SNB0n5MxQJK%2FtYTHrzeLrCIAisI%3D%7Ctkp%3ABk9SR8TR_vqSZA"]
    custom_settings = {
        'FEEDS': {'data.jsonl': {'format': 'jsonlines'}}
    }

    def parse(self, response):
        try:
            title = response.xpath('//h1[@class="x-item-title__mainTitle"]/span//text()').get()
        except:
            title = ''
        try:
            foto_url = response.xpath('//div[@class="ux-image-carousel-item image-treatment active  image"]/img/@'
                                      'src[contains(.,"jpg")]').get()
        except:
            foto_url = ''
        try:
            seller = response.xpath('//div[@class="x-sellercard-atf__info"]/div//a//text()').get()
        except:
            seller = ''
        try:
            price = response.xpath('//div[@class="x-bin-price__content"]/div[@class="x-price-primary"]/span//text()').get()
        except:
            price = ''
        try:
            product_url = response.url
        except:
            product_url = ''
        try:
            shipping_price = response.xpath('//span[contains(text(), "Shipping:")]/../../../following-sibling::div/d'
                                            'iv/div/span[@class="ux-textspans ux-textspans--BOLD"]//text()').get()
        except:
            shipping_price = ''
        data = {
            'Title': title,
            'URL Foto': foto_url,
            'Product URL': product_url,
            'Price': price,
            'Seller': seller,
            'Shipping Price': shipping_price
        }
        yield data