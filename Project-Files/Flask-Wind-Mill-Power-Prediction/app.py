import numpy as np
import joblib
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load("power_prediction.sav")

# ---------- LANDING PAGE ----------
@app.route('/')
def intro():
    return render_template("intro.html")

# ---------- PREDICT PAGE ----------
@app.route('/predict')
def predict_page():
    return render_template("predict.html")

# ---------- WEATHER ----------
@app.route('/windapi', methods=['POST'])
def windapi():
    city = request.form.get('city')
    api_key = "14a9ab075532156acf8801d0f39ca758"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    data = requests.get(url)
    data = data.json()

    temp = str(data['main']['temp'])+" °C"
    humid = str(data['main']['humidity'])+" %"
    pressure = str(data['main']['pressure'])+" mmHG"
    speed = str(data['wind']['speed'])+" m/s"

    return render_template(
        "predict.html",
        temp=temp,
        humid=humid,
        pressure=pressure,
        speed=speed
    )

# ---------- RESULT PAGE ----------
@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[float(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output = prediction[0]
    
    return render_template(
        "predict.html",
        prediction_text="The energy predicted is {:.2f} kW".format(output)
    )

if __name__ == "__main__":
    app.run(debug=False)
