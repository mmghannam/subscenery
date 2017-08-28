from bs4 import BeautifulSoup as soup
import requests
from itertools import islice


class Scrapper:
    def __init__(self, link):
        page_html = requests.get(link).content
        self.soup = soup(page_html, 'html.parser')

    def get_id(self, id):
        return soup.find_all(id=id)


class SubSceneScrapper(Scrapper):
    # subscene constants
    SUBSCENE_DOMAIN = 'https://subscene.com'
    QUERY_URI = '/subtitles/title?q='

    def __init__(self, movie_or_series_name):
        Scrapper.__init__(self, SubSceneScrapper.SUBSCENE_DOMAIN +
                          SubSceneScrapper.QUERY_URI +
                          movie_or_series_name.replace(' ', '+'))

        self.movie_or_series_name = movie_or_series_name

    def search_media(self):
        """
        Scrapes subscene for movie search 
        :return: A formatted dict representing search results 
        """
        search_result_div = self.soup.find_all('div', 'search-result')[0].contents
        current_category = ''
        movie_results = {
            'Exact': [],
            'Popular': [],
            'Close': []
        }
        for tag in search_result_div:
            if tag.name == 'h2':
                current_category = tag.get_text()
            elif tag.name == 'ul':
                for list_item in tag.contents:
                    if list_item.name == 'li':
                        movie_results[current_category].append({
                            'link': list_item.div.a['href'],
                            'text': list_item.div.a.get_text()
                        })
        return movie_results

    @staticmethod
    def get_subtitles(uri):
        scrapper = Scrapper(SubSceneScrapper.SUBSCENE_DOMAIN + uri)
        results_table_contents = scrapper.soup.find_all('tbody')[0].children
        subtitles = {}
        for item in results_table_contents:
            if item.name == 'tr':
                # print(item.td['class'])
                if item.td['class'] == ['a1']:
                    language, title = islice(item.td.a.children, 2)
                    subtitle = {
                        'link': item.td.a['href'],
                        'title': title.get_text().strip(' \r\t\n')
                    }
                    if language in subtitles:
                        subtitles[language].append(subtitle)
                    else:
                        subtitles[language] = [subtitle]
        return subtitles
    def change_movie_or_series_name(self, movie_or_series_name):
        other = SubSceneScrapper(movie_or_series_name)
        self.soup = other.soup
