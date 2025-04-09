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
    query_string = urlencode(params)
    url = f"https://wttr.in/{city}?{query_string}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    cities = ["london", "moscow", "cherepovets"]
    for city in cities:
        print(fetch_weather(city))


if __name__ == "__main__":
    main()
