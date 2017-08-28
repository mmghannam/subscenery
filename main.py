from pprint import pprint

from subscenery.scrapper import SubSceneScrapper

movie_name = 'August bebo'
scrapper = SubSceneScrapper(movie_name)
pprint(scrapper.get_subtitles())
