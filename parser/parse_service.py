from requests_html import HTMLSession

session = HTMLSession()


class WebSiteParser:
    def __init__(self):
        self.session = HTMLSession()
        self.url = 'https://cryptonews.com'

    @classmethod
    def validate_news(cls, news) -> list:
        news_list = []
        for element in news:
            link = ['https://cryptonews.com' + link for link in element.links][0]
            title = element.text
            news_list.append([title, link])
        return news_list

    def parse_news_from_site_and_validate(self) -> list:
        response = self.session.get(self.url)
        news = response.html.find('.article__title--featured')
        return self.validate_news(news)
