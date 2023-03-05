import os

import requests
from dotenv import load_dotenv

load_dotenv()

MY_API_KEY = os.getenv('MY_API_KEY')


def get_match_id_by_puuid(puuid, page=0):
    start = 100 * page
    url = f"https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count=100"
    headers = {
        "X-Riot-Token":MY_API_KEY,
        "User-Agent": "Meow"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception("status code ", resp.status_code)
    return resp.json()


def get_match(match_id):
    url = f"https://sea.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {
        "X-Riot-Token":MY_API_KEY,
        "User-Agent": "Meow"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception("status code ", resp.status_code)
    return resp.json()


if __name__ == "__main__":
    match_id_list = get_match_id_by_puuid("hNgSyrUajUcwRInZQra1nBU7UcBvDcCwGMnyvQuti7HLON0CRDmGz3lIkl8LhlputovzkHF7vTE7Ag")
    print(type(match_id_list))
    print(match_id_list)
    match_id = "VN2_40829816"
    match = get_match(match_id)
    print(type(match))
    print(match["metadata"])