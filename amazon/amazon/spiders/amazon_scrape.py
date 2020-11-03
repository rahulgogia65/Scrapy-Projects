import scrapy

x=input('Product name: ').split()
url='https://www.amazon.in/s?k='
temp=""
if len(x)>1:
    for y in x:
        temp += y +'+'
        url += temp
        temp=""
else:
    url = url + x[0]



class AmazonSpider(scrapy.Spider):
    name='amazon.com'

    allowed_domains=['amazon.in', 'amazon.com']
    start_urls=[url]

    def parse(self, response):
        product_name = response.css('span.a-size-medium.a-color-base.a-text-normal::text').get(default='').strip()
        product_price = response.css('span.a-price-whole::text').get(default='').strip()

        yield{ 
            'Product' : product_name,
            'Price' :  product_price,
        }

        
