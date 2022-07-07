# STOCKSCIENCE WEB APP
Web App for Stock Quotes &amp; Live News Stream; Building a Portfolio Using Python &amp; Django

## Purpose
* It is a web application for stock market data where users can get **real-time stock data** via **AlphaVantage** and
**IEXCloud APIs**. 
* It provides **stock market news** via **NewsAPI**. Search-box implemented for company specific news.
* Users can create **Personal Stock Portfolio** to keep the track of stocks and get **Email Alert** for any major price changes.
* Adding charts visualization and implementing machine learning to analyze stocks will be the second goal, when I expand this app in the near future.

## Video Demo
For a demo of the code and how the web app works, please see this screen recording:

## Requirements
* Get your own Django secret key
	* Create your own Django app
	* Copy secret key
	* Paste key into this project's secret key location at settings.py or in your own environment.
* API key is required if you want to use data from IEX cloud.
	* Create free account at https://iexcloud.io/.
	* Real-time data is free, however it is limited. You can use unlimited simulated data for free.
* API key is required to receive news (from news.html) via  News API.
	* Create free account at https://newsapi.org.
* API key is required from Alpha Vantage if you want to use Email aLert feature.
	* https://www.alphavantage.co/support/#api-key
* Use pipenv to install python dependencies for the backend.

## How to Run
* Run backend server with the following command:
* "python manage.py runserver"

## Technical Summary
* Django
* Django Rest Framework
* Back end language: Python (the version used here is Python 3.7.7)
* Bootstrap
* HTML/CSS
* JavaScript
* SQL
