#!/usr/bin/env python3

import requests

"""This module fetches the list of starships that can hold at least 'passengerCount' passengers."""


def availableShips(passengerCount):
    """
    Fetches the list of starships that can hold at least `passengerCount` passengers.

    Args:
        passengerCount (int): Minimum number of passengers the ship should hold.

    Returns:
        List[str]: Names of starships that meet the requirement.
    """
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break  # Stop if there's an error

        data = response.json()
        for ship in data['results']:
            passengers = ship['passengers'].replace(',', '')  # Remove commas in numbers
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship['name'])

        url = data.get('next')  # Get next page URL for pagination

    return ships
