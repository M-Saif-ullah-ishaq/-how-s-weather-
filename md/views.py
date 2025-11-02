
import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def weather_api(request):
    # Define the city or get it from user input
     
    if request.method == 'POST':
        city = request.POST['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q='+city +'&units=metric&appid=e3219343f4a71ce4d0520df320419be8'
        response = urllib.request.urlopen(url)
        list_of_data = json.loads(response.read())

    # Create the data dictionary
        data = {
           "country_code": str(list_of_data['sys']['country']),
           "coordinate": str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
           "temp": str(list_of_data['main']['temp']) + '°C',
           "pressure": str(list_of_data['main']['pressure']) + ' hPa',
           "humidity": str(list_of_data['main']['humidity']) + '%',
           'main': str(list_of_data['weather'][0]['main']),
           'description': str(list_of_data['weather'][0]['description']),
           'icon': str(list_of_data['weather'][0]['icon']),
        }
        # return HttpResponse(data)
        return render(request, 'base.html', {'data': data})
    else:
        return render(request,'base.html')
        
    
    
    # Render the data to the HTML template

    
    