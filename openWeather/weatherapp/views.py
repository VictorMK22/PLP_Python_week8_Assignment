from urllib.request import urlopen
import json
from django.shortcuts import render

def index(request):
    data = {}
    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            try:
              # Replace with your API key
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid="<API_KEY>"
                source = urlopen(url).read()
                list_of_data = json.loads(source)

                data = {
                    "country_code": str(list_of_data["sys"]["country"]),
                    "coordinate": f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
                    "temp": str(round(list_of_data["main"]["temp"] - 273.15, 2)) + "°C",
                    "pressure": str(list_of_data["main"]["pressure"]),
                    "humidity": str(list_of_data["main"]["humidity"]),
                    "main": str(list_of_data["weather"][0]["main"]),
                    "description": str(list_of_data["weather"][0]["description"]),
                    "icon": list_of_data["weather"][0]["icon"],
                }
            except Exception as e:
                data = {"error": "City not found or API request failed."}
                print(f"Error: {e}")

    return render(request, "main/index.html", {"data": data})
