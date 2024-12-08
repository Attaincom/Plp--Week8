import requests
from django.conf import settings
from django.shortcuts import render

def get_weather(city_name):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def weather_view(request):
    weather_data = None
    if request.method == "POST":
        city_name = request.POST.get('city')
        weather_data = get_weather(city_name)
    return render(request, 'weather/weather.html', {'weather_data': weather_data})
