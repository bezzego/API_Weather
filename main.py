import requests

cities = ["london", "moscow", "cherepovets"]

for city in cities:

    url = f"https://wttr.in/{city}?nTqm&lang=ru"

    response = requests.get(url)
    response.raise_for_status()

    filename = f"weather_{city}.txt"
    with open(filename, "wb") as file:
        file.write(response.content)

    print(response.text)
