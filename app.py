from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    # return render_template('homepage.html')
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'profilePic.png')
    return render_template("homepage.html", user_image=pic1)  

@app.route('/', methods=['POST'])
def get_weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=54a4215d65eb60a2a0c49c14c289a227&units=metric'
    response = requests.get(url).json()
    weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'wind_speed': response['wind']['speed'],
        'icon': response['weather'][0]['icon']
    }
    return render_template('homepage.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)