from django.shortcuts import render
import urllib.request
import json
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url= urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=e8bf1045b9e493c868c62767dd8bdc9a').read()
        w_data= json.loads(url)

        data = {
            "description": w_data['weather'][0]['description'],
            "temperature": w_data['main']['temp'],
            "pressure": w_data['main']['pressure'],
            "humidity":w_data['main']['humidity'],
        }
        
    else:
        city = None
        data = {}
    return render(request, 'index.html', {"city": city, "data" :data})
    