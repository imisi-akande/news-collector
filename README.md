# Scraping News stories
<p align="center">
  <img src="./images/sahara_report.png">
</p>

The aim of the project is to scrape news from Sahara reporters and perform certain 
sentiment analysis on the collected data

### Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Data](#data)
4. [Running the code](#running)
5. [Results](#results)

### Introduction<a name="introduction"></a>
In this repository, I shall be scraping all sahara reporters news by category. The aim of this 
project is to perform analyses on stories data and perform some sentiment analysis on the scraped data:

### Prerequisites<a name="prerequisites"></a>
*Steps to install*
- Run `python3 -m pip install --user virtualenv` to install virtualenv on MACOS or `py -m pip install --user virtualenv` on Windows
- Go to the project root directory and run `python3 -m venv news_env` or `py -m venv news_env` on Windows
- Run `source news_env/bin/activate` to activate the virtual environment on MAC or `.\env\Scripts\activate` on Windows
- Run `pip install -r requirements.txt` to install used packages

---------------------------------------------------------------------------------------------------------------------
*Packages to install*
- virtualenv
- Scrapy

### Data<a name="data"></a>
scraped news data

### Running the code<a name="running"></a>
- [`news_crawler`] - This folder embeds the project
- [`spiders`] - This folder consists of a single spider(news) which is the file that consists of the code that crawl the web.
*how to scrape the news stories*
- Run `scrapy crawl news -o stories.csv -o stories.xml -o stories.json` to generate all files
at once.
- You can also combine the argument and the output file options in the crawl command to scrape by category
e.g `scrapy crawl news -a story="entertainment" -o entertainment.csv`.

### Results<a name="results"></a>
csv, json and xml files generated