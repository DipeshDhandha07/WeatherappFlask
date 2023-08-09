from flask import Flask, request, render_template
import requests
import datetime as dt

app = Flask(__name__)

# Your API Key
API_KEY = '37d41fd392d68dcd84981a5f9c460855'


@app.route('/', methods=["POST", "GET"])
def search_city():
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return render_template("error.html")
        if len(city) <= 1:
            return render_template("error.html")
        units = 'Metric'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={units}'
        response = requests.get(url).json()

        country = response["sys"]["country"]
        current_date = response["dt"]
        m = dt.datetime.fromtimestamp(int(current_date)).strftime('%d-%m-%Y %H:%M:%S ')
        new_city = city
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        icon = response["weather"][0]["icon"]
        humidity = response["main"]["humidity"]

        return render_template("weather_new.html", city=new_city, temperature=temperature, description=description,
                               icon=icon, humidity=humidity, country=country, m=m)
    return render_template("weather_new.html")


if __name__ == '__main__':
    app.run()
