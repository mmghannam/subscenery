from pprint import pprint

from subscenery.scrapper import SubSceneScrapper

movie_name = 'A.United.Kingdom.2016.720p.BluRay.x264-[YTS.AG]'
scrapper = SubSceneScrapper(movie_name, True)
pprint(scrapper.get_best_match_subtitle('Arabic'))
