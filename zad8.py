from typing import List
import json
import requests
import argparse
import Items.Brewery as Brewery


def get_breweries_from_api(city) -> list:
    BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'
    if city == '':
        response = requests.get(f"{BASE_URL}?per_page=20")
    else:
        response = requests.get(f"{BASE_URL}?by_city={city}")
    return response


def brewery_factory(breweries) -> List[Brewery]:
    data = json.loads(breweries.text)
    return [Brewery.Brewery(**item) for item in data]


def parse_arguments():
    parser = argparse.ArgumentParser(description='Brewery API')
    parser.add_argument('city', type=str, help='city name')
    return vars(parser.parse_args())


def main():

    args = parse_arguments()
    breweries = get_breweries_from_api(args['city'])
    breweries = brewery_factory(breweries)

    for brewery in breweries:
        print(brewery.__str__())


main()
