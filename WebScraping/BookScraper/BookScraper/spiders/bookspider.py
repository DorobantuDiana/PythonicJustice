import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield{
                'name': book.css('h3 a::text').get(),
                'price': book.css('.product_price .price_color::text').get(),
                'url': book.css('h3 a').attrib['href']
            }

        next_pg = response.css('li.next a ::attr(href)').get()
  
        if next_pg is not None:
            if 'catalogue/' in next_pg:
                next_pg_url = 'https://books.toscrape.com/' + next_pg
            else:
                next_pg_url = 'https://books.toscrape.com/catalogue/' + next_pg
                
            yield response.follow(next_pg_url, callback=self.parse)