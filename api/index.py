from flask import Flask

from src.weather import get_current_temperature, hydration_tip_by_weather

app = Flask(__name__)


@app.route("/")
def home():
    temperature = get_current_temperature()
    tip = hydration_tip_by_weather(temperature)

    return f"""
    <h1>💧 HydratePlus</h1>
    <h2>Recomendação de hidratação com API pública</h2>
    <p><strong>Temperatura atual:</strong> {temperature}°C</p>
    <p>{tip}</p>
    <hr>
    <p>Projeto desenvolvido em Python com integração à API Open-Meteo.</p>
    """