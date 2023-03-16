from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=54a4215d65eb60a2a0c49c14c289a227'
    response = requests.get(url).json()
    weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon']
    }
    return render_template('homepage.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
