from typing import List
import json
import requests
import Items.Brewery as Brewery


def get_breweries_from_api() -> list:
    BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'
    response = requests.get(f"{BASE_URL}?per_page=20")
    return response


def brewery_factory(breweries) -> List[Brewery]:
    data = json.loads(breweries.text)
    return [Brewery.Brewery(**item) for item in data]


def main():
    breweries = get_breweries_from_api()
    breweries = brewery_factory(breweries)

    for brewery in breweries:
        print(brewery.__str__())


main()
