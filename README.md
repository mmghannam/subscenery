# subscenery
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

movie_name = 'A.United.Kingdom.2016.720p.BluRay.x264-[YTS.AG].mp4'
# initialize scrapper
scrapper = SubSceneScrapper(movie_name, is_filename=True)
# get subtitles
scrapper.get_subtitles()
# get best match subtitle for language
best_match = scrapper.get_best_match_subtitle('English')
# download subtitle to current path
scrapper.download_subtitle_to_path(best_match, '')

```

