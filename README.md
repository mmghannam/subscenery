# subscene-scrapper (WIP)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
A subscene.com website scrapper written in python, that outputs a nicely formatted objects for movie/series subtitles


## Usage
```python
from scrapper import SubSceneScrapper
movie_name = 'August Rush'
# initialize scrapper
scrapper = SubSceneScrapper(movie_name)
# get Exact Result
exact_result = scrapper.search_media()['Exact'][0]['link']
# get subtitles
scrapper.get_subtitles(exact_result)
```

