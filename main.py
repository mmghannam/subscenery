from scrapper import SubSceneScrapper
from pprint import pprint

movie_name = 'August Rush'
scrapper = SubSceneScrapper(movie_name)
exact_result = scrapper.search_media()['Exact'][0]['link']
pprint(scrapper.get_subtitles(exact_result))
