from parsel import Selector
import requests


class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    START_URL = "https://24.kg/ekonomika/"
    LINK_XPATH = '//div[@class="one"]/div/a/@href'
    TITLE_V1_XPATH = '//div[@class="one"]/div/a/strong/text()'
    TITLE_V2_XPATH = '//div[@class="one"]/div/a/span/text()'

    def parse_data(self):
        text = requests.get(self.START_URL).text
        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).extract()
        first_v_title = tree.xpath(self.TITLE_V1_XPATH).extract()
        second_v_title = tree.xpath(self.TITLE_V2_XPATH).extract()
        first_v_title.extend(second_v_title)
        iis = 0
        for link, title in zip(links, first_v_title):
            if iis < 5:
                print(self.PLUS_URL + link)
                print(title)
                iis += 1


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()