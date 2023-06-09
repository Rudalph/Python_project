from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

picFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'mainGlobeC.png')
    return render_template("homepage.html", user_image=pic1)  

@app.route('/', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=54a4215d65eb60a2a0c49c14c289a227&units=metric'
    response = requests.get(url).json()
    weather = {
        'temperature': round(response['main']['temp']),
        'description': response['weather'][0]['description'].title(),
        'wind_speed': response['wind']['speed'],
        'feels': round(response['main']['feels_like']),
        'name': response['name'],
        'visibility': round((response['visibility'])/1000),
        'humidity': response['main']['humidity'],
        'pressure': response['main']['pressure'],
        'temp_min':round(response['main']['temp_min']),
        'temp_max':round(response['main']['temp_max']),
    }
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'mainGlobeC.png')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'sun.png')
    return render_template('homepage.html', weather=weather, user_image=pic1,weather_icon=pic2)

if __name__ == '__main__':
    app.run(debug=True)