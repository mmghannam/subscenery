# subscenery
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)

A subscene.com website scrapper written in python, that outputs a nicely formatted objects for movie/series subtitles

## Dependencies
**BeautifulSoup4**
```
pip install bs4
```
**requests**
```
pip install requests
```
**parse-torrent-name**
```
pip install parse-torrent-name
```
## Usage
```python
from subscenery.scrapper import SubSceneScrapper
movie_name = 'August Rush'
# initialize scrapper
scrapper = SubSceneScrapper(movie_name)
# get subtitles
scrapper.get_subtitles()
```

