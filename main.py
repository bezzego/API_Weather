import requests
from urllib.parse import urlencode


def fetch_weather(city):
    params = {
        "n": "",
        "T": "",
        "q": "",
        "m": "",
        "lang": "ru",
    }
    url = f"https://wttr.in/{city}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    cities = ["london", "moscow", "cherepovets"]
    for city in cities:
        print(fetch_weather(city))


if __name__ == "__main__":
    main()
