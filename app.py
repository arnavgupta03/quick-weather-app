from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    API_KEY = "54640b5da3fd28953cbdc34af59edda9"
    value = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Port%20Credit&appid=" + API_KEY)
    jsonified = value.json()
    temp = int(int(jsonified['main']['temp']) - 273.15)
    feelsLike = int(int(jsonified['main']['feels_like']) - 273.15)
    mainDescript = jsonified['weather'][0]['main']
    otherDescript = jsonified['weather'][0]['description']
    return render_template("index.html", temp = temp, feelsLike = feelsLike, mainDescript = mainDescript, otherDescript = otherDescript)

if __name__ == '__main__':
    app.run()