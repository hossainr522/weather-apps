from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


def weather_data(city):
    city = city.replace(' ', '+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 ' \
                 'Safari/537.36 '
    LANGUAGE = 'en-US,en;q=0.9,bn;q=0.8'
    session = requests.session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')

    results = {}

    results['area'] = soup.find('span', attrs={'class': 'BBwThe'}).text
    results['daytime'] = soup.find('div', attrs={'id': 'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id': 'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id': 'wob_tm'}).text
    return results


# Create your views here.

def find_weather_data(request):
    if request.method == "GET" and "city" in request.GET:
        city = request.GET.get("city")
        results = weather_data(city)
        context = {'results': results}
    else:
        context = {}

    return render(request, "home.html", context)
