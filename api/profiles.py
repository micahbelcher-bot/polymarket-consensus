import requests

BASE_URL = "https://gamma-api.polymarket.com/public-profile"


def get_profile(wallet):
    response = requests.get(
        BASE_URL,
        params={"address": wallet}
    )

    if response.status_code == 200:
        return response.json()

    return None