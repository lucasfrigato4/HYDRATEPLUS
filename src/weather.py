import requests

API_URL = "https://api.open-meteo.com/v1/forecast"


def get_current_temperature(latitude=-16.3285, longitude=-48.9534):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["current"]["temperature_2m"]


def hydration_tip_by_weather(temperature):
    if temperature >= 30:
        return "🔥 Está quente hoje. Reforce sua hidratação!"
    return "💧 Temperatura agradável. Mantenha sua meta diária de água."