import json

import requests


class Brewery:
    def __init__(self, id, name, brewery_type, address_1, address_2, address_3, city, state_province, postal_code, country, phone, website_url, longitude, latitude, state, street):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.phone = phone
        self.website_url = website_url
        self.longitude = longitude
        self.latitude = latitude
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.street = street

    def __str__(self):
        return (f'ID: {self.id} '
                f'\nName: {self.name}'
                f'\nBrewery type: {self.brewery_type}'
                f'\nAddress 1: {self.address_1}'
                f'\nAddress 2: {self.address_2}'
                f'\nAddress 3: {self.address_3}'
                f'\nCity: {self.city}'
                f'\nState: {self.state}'
                f'\nPhone: {self.phone}'
                f'\nWebsite URL: {self.website_url}'
                f'\nLongitude: {self.longitude}'
                f'\nLatitude: {self.latitude}'
                f'\nState Province: {self.state_province}'
                f'\nPostal Code: {self.postal_code}'
                f'\nCountry: {self.country}'
                f'\nStreet: {self.street}'
                f'')


def cast_json_to_object(json_data):
    data = json.loads(json_data.text)
    return [Brewery(**item) for item in data]


BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'

response = requests.get(f"{BASE_URL}?per_page=20")

breweries = cast_json_to_object(response)
for brewery in breweries:
    print(brewery.__str__())
