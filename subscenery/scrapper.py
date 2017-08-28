from bs4 import BeautifulSoup as soup
import requests
from itertools import islice
import PTN


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

    # TODO : add ability to search for series
    def __init__(self, movie_name, is_filename=False):
        """
        Used to initialized scrapper
        :param movie_name: name of the file or the direct name of the media  
        :param is_filename: indicated 
        """
        if is_filename:
            parsed_info = PTN.parse(movie_name)
            movie_name = parsed_info['title']

        Scrapper.__init__(self, SubSceneScrapper.SUBSCENE_DOMAIN +
                          SubSceneScrapper.QUERY_URI +
                          movie_name.replace(' ', '+'))

        self.movie_name = movie_name

    def __search_media(self):
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
                            'uri': list_item.div.a['href'],
                            'text': list_item.div.a.get_text()
                        })
        return movie_results

    @staticmethod
    def __get_subtitles_from_uri(uri):
        """
        Queries for subtitles with a uri of the movie found by search_media()
        :param uri: uri of the movie subtitles 
        :return: a formatted dict of the subtitles with links and languages
        """
        scrapper = Scrapper(SubSceneScrapper.SUBSCENE_DOMAIN + uri)
        results_table_contents = scrapper.soup.find_all('tbody')[0].children
        subtitles = {}
        for item in results_table_contents:
            if item.name == 'tr':
                # print(item.td['class'])
                if item.td['class'] == ['a1']:
                    language = item.td.a.span.get_text().strip(' \r\n\t')
                    subtitle = {
                        # TODO: add rating
                        'uri': item.td.a['href'],
                    }
                    if language in subtitles:
                        subtitles[language].append(subtitle)
                    else:
                        subtitles[language] = [subtitle]
        return subtitles

    def get_subtitles(self, must_be_exact=False):
        """
        :return: subtitles of all languages found for the given movie 
        """
        search_result = self.__search_media()
        if not search_result['Exact']:
            if must_be_exact:
                raise ValueError("Couldn't find an exact match for '{}'".format(self.movie_name))
            elif search_result['Popular']:
                return self.__get_subtitles_from_uri(search_result['Popular'][0]['uri'])
            elif search_result['Close']:
                return self.__get_subtitles_from_uri(search_result['Close'][0]['uri'])
            else:
                raise ValueError("Couldn't find a match for '{}'".format(self.movie_name))
        else:
            return self.__get_subtitles_from_uri(search_result['Exact'][0]['uri'])
