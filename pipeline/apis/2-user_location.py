#!/usr/bin/env python3
""" This module returns the location of a user
    with a GitHub API URL."""

import requests
import sys
from datetime import datetime, timedelta

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <API_URL>")
        sys.exit(1)

    api_url = sys.argv[1]

    try:
        response = requests.get(api_url, timeout=5)  # Added timeout to prevent hanging
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('location', 'Location not specified'))
        elif response.status_code == 403:
            reset_timestamp = response.headers.get('X-RateLimit-Reset')
            if reset_timestamp:
                reset_time = datetime.fromtimestamp(int(reset_timestamp))
                now = datetime.now()
                minutes_remaining = max(0, (reset_time - now).total_seconds() // 60)
                print(f'Reset in {int(minutes_remaining)} min')
            else:
                print('Rate limit exceeded, but reset time unavailable.')
        elif response.status_code == 404:
            print('Not found')
        else:
            print(f'Error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
