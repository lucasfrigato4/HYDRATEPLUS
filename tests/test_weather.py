from unittest.mock import Mock, patch

from src.weather import get_current_temperature, hydration_tip_by_weather


@patch("src.weather.requests.get")
def test_get_current_temperature(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "current": {
            "temperature_2m": 31.5
        }
    }
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    temperature = get_current_temperature()

    assert temperature == 31.5


def test_hydration_tip_hot_weather():
    result = hydration_tip_by_weather(32)

    assert "Reforce sua hidratação" in result