import scrapy

class RedditSpider(scrapy.Spider):
    name = 'reddit'

    start_urls = ['https://www.reddit.com/r/rarepuppers/']

    def parse(self, response):
        links = response.css('img::attr(src)').getall()
        html = ""

        for link in links:
            print(link)
            

            if any(extension in link for extension in ['.jpg', '.jpeg', '.png', '.gif' ]):
                html += """<a href = "{link}" target="_blank">
                    <img src="{link}" height="33%" width="33%"/>
                    </a>""".format(link=link)

                with open("frontpage.html","a") as page:
                    page.write(html)
                    page.close()