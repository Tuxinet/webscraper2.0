import scraper

if __name__ == '__main__':
    url = raw_input("Input url: ")
    limit = input("Input number of urls to visit: ")
    sleeptime = input("Input sleeptime: ")
    spider = scraper.Scraper(url, limit, sleeptime)
    spider.crawl()