from setuptools import setup

setup(
    name="Subscenery",
    version="0.1",
    description="A subscene.com website scrapper written in python, " +
                "that outputs a nicely formatted objects for movie/series subtitles",
    url="https://github.com/mmghannam/subscenery",
    author="", # TODO
    author_email="", # TODO
    license='MIT',
    packages=['subscenery'],
    install_requires=[
        'bs4',
        'requests',
        'parse-torrent-name'
    ]
)