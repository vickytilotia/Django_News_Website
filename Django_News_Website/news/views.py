from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import requests
import json

class Home(View):

    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'sortBy=popularity&'
       'apiKey=8f684780f2814ca1a146e42481abda44')
    
    url_b = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
       'category=business&'
       'apiKey=8f684780f2814ca1a146e42481abda44')
    
    url_t = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
       'category=technology&'
       'apiKey=8f684780f2814ca1a146e42481abda44')

    def get(self, request):
        headlines = requests.get(self.url).json()
        
        headlines_list = headlines['articles']
        author = []
        title = []
        description = []
        news_url = []
        img_url = []
        published_date = []
        content = []
        
        for headline in headlines_list:
            author.append(headline['author'])
            title.append(headline['title'])
            description.append(headline['description'])
            news_url.append(headline['url'])
            img_url.append(headline['urlToImage'])
            published_date.append(headline['publishedAt'].split('T')[0])
            content.append(headline['content'])
        
        # print(title)
        final_list = zip(author,title,description,news_url,img_url,published_date,content)
        
        # one news from buisness
        headlines = requests.get(self.url_b).json()
        headlines_list = headlines['articles']
        for headline in headlines_list:
            if len([headline['title']])<30:
                author = [headline['author']]
                title = [headline['title']]
                description = [headline['description']]
                news_url = [headline['url']]
                img_url = [headline['urlToImage']]
                published_date = [headline['publishedAt'].split('T')[0]]
                content = [headline['content']]
                break

        buisness_list = zip(author,title,description,news_url,img_url,published_date,content)

        # one for technology
        # one news from buisness
        headlines = requests.get(self.url_t).json()
        headlines_list = headlines['articles']
        for headline in headlines_list:
            if len([headline['title']])<20:
                author = [headline['author']]
                title = [headline['title']]
                
                description = [headline['description']]
                news_url = [headline['url']]
                img_url = [headline['urlToImage']]
                published_date = [headline['publishedAt'].split('T')[0]]
                content = [headline['content']]
                break

        tech_list = zip(author,title,description,news_url,img_url,published_date,content)
        heading_list = tech_list
        context = {'list':final_list,'buisness_list':buisness_list,'tech_list':tech_list,'heading':heading_list}
        # print(context)
        return render(request, "index.html",context)