from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import csv
import requests
import json
from bs4 import BeautifulSoup 
from .models import Name
from googlesearch import search
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .forms import NameForm
import openai
from urllib.parse import quote

# Create your views here.
def index(request):
    return render(request,"index.html")


def excel_download(request):

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="consumer.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Id'])

    return response


def search(request):
    # Define API key and search engine ID
    # api_key = 'AIzaSyBkSuQXJY4x4YhJBYyOcimrUP0vXePRSZQ'
    # search_engine_id = 'e2ffc7ac0c0934c9f'
    
    # query = request.GET.get('company_name', '')
    # service = build("customsearch", "v1", developerKey=api_key)
    # response = service.cse().list(q=query, cx=search_engine_id, num=1).execute()

    # items = response.get('items', [])
    # if items:
    #     answer = items[0].get('title', '')
    #     x = answer.split("-")
    #     y = x[0]
    #     print(x)
    #     print(type(answer))
    #     return JsonResponse({'answer': answer})
    # else:
    #     return JsonResponse({'answer': 'No results found'})



    company_name = request.GET.get('company_name')
    if company_name:
        # Prepare the query URL
        query = f"{company_name} CEO founder director CTO"
        url = f"https://www.google.com/search?q={query}"

        # Send a GET request to Google and parse the HTML response
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the relevant information from the search results
        ceo = soup.find('div', class_='BNeawe').text

        founder = soup.find('div', class_='BNeawe').find_next('div', class_='BNeawe').text

        x= founder.split(" ")[2]        
        founder_linkedin = f"https://www.linkedin.com/in/{x}/"

        y = ceo.split("-")[0]
        ceo_linkedin = f"https://www.linkedin.com/in/{x}/"

        # director = soup.find('div', class_='BNeawe').find_next('div', class_='BNeawe').find_next('div', class_='BNeawe').text
        # cto = soup.find('div', class_='BNeawe').find_next('div', class_='BNeawe').find_next('div', class_='BNeawe').find_next('div', class_='BNeawe').text

        # Return the information as JSON response
        return JsonResponse({
            'ceo': y,
            'ceo_linkedin': ceo_linkedin,
            'founder': x,
            'founder_linkedin':founder_linkedin,
            # 'director': director,
            # 'cto': cto,
        })

    return JsonResponse({'error': 'Company name not provided.'})