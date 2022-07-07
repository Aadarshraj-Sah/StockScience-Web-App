from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
from .email_alert import check,mailing

# Browser request for home page, pass in dict
def home(request):
	import requests
	import json
	
	if request.method == 'POST':
		ticker = request.POST['ticker']
		# pass in url that calls the api
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=YOUR_API_KEY")
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api, 
			'error':"Could not access the api"})
	
	else:
	
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})



def about(request):
	
	return render(request, 'about.html', {})


def add_stock(request):
	import requests
	import json
	import os
	
	if request.method == 'POST':
		form = StockForm(request.POST or None)
	
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added to your portfolio!"))				
			return redirect('add_stock')

	else:	
		ticker = Stock.objects.all()
		# save ticker info from api output into python list ('output list')
		output = []
		
		# modify to pull multiple stock tickers at the same time
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=YOUR_API_KEY")
			try:
				api = json.loads(api_request.content)
				output.append(api)
				# mailing(str(ticker_item) + " " + check(ticker_item))
				# print(ticker_item)
			except Exception as e:
				api = "Error..."	
				
		return render(request, 'add_stock.html', {'ticker': ticker, 'output':  output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id) # call database by primary key for id #
	item.delete()
	messages.success(request, ("Stock Has Been Deleted From Portfolio!"))
	return redirect(add_stock)
	
def news(request):
	import requests
	import json
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("http://newsapi.org/v2/everything?q="+ticker+"&apiKey=YOUR_API_KEY").json()
	# News API
	else:
		api_request = requests.get('http://newsapi.org/v2/everything?q=stocks&apiKey=YOUR_API_KEY').json()

	
	
	# BASIC - Stock News API
	#api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=general&items=50&token=</your_api_key>')
	
	# PREMIUM - Stock News API
	# api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token=</your_api_key>')
	# api = json.loads(api_request.content)
	articles = api_request['articles']
	url = []
	desc = []
	news = []
	img = []
	time = []
	source = []
	for i in range(len (articles)):
		article =  articles[i]
		url.append (article['url'])
		desc.append (article['description'])
		news.append (article['title'])
		img. append (article['urlToImage'])
		time.append (article['publishedAt'])
		articlesource = article['source']
		source.append(articlesource['name'])
		# source.append(articles[i].source['name'])


	mylist = zip(url, news, desc, img, time, source)
	return render(request, 'news.html', context = {"mylist": mylist}) 
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(add_stock)





