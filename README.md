# Crypto Analysis

This little project was created to demonstrate how to perform an analysis of a crypto time series using Python, Statistics and Machine Learning techniques for strategy optimization. The project is divided into 2 parts, one for data scraping and another for the analysis of the extracted data.

## Table of contents
* [Data Scraping](#data-scraping)
* [Data Analysis](#data-analysis)

## Data Scraping
Using the **Bybit API** and the [**pybit module**](https://pypi.org/project/pybit/) you can extract all the historical data of the selected pair, from the moment it was listed on the exchange until today, you can also choose the _extraction timeframe_. We will be able to do this important task with **_crypto_scraper.py_** file and you can see an application example in the **_example.py_** file (both the files are in the Scraping folder).
