from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '2e2e1b6811c04e82aa536d5f34ae75a9'

def home(request):
    country = request.GET.get('country', '').strip()
    category = request.GET.get('category', '').strip()

    # Construct the base URL
    url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}'

    # Append parameters if they are provided
    if country and category:
        url += f'&country={country}&category={category}'
    elif country:
        url += f'&country={country}'
    elif category:
        url += f'&category={category}'
    else:
        # If no country or category, use a default query to satisfy the API requirement
        url += f'&q=news'

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Initialize the context variables
    articles = []
    error_message = None

    # Check if the response status is ok
    if data.get('status') == 'ok':
        articles = data.get('articles', [])
    else:
        error_message = data.get('message', 'An error occurred while fetching the news.')



    # Pass data to the template
    context = {
        'articles': articles,
        'error_message': error_message,
    }

    return render(request, 'home.html', context)
