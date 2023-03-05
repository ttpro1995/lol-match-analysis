"""

Fetch first 100 match
"""
import dotenv
import os
from dotenv import load_dotenv
from api_call import get_match_id_by_puuid, get_match
from tqdm import tqdm
import json
import time
import jsonlines

load_dotenv()

MY_PUUID=os.getenv('MY_PUUID')
DATA_MATCHES=os.getenv("DATA_MATCHES")


############ GET SEED DATA ################################################

def get_100_match_id():
    match_id_file = os.path.join(DATA_MATCHES, "my_match_id.txt")
    with open(match_id_file, "w") as file:
        match_ids = get_match_id_by_puuid(puuid=MY_PUUID)
        for match in match_ids:
            file.write(match + "\n")

def get_100_match():
    """
    Read from my_100_match_id.txt
    get match
    :return:
    """
    match_id_file = os.path.join(DATA_MATCHES, "my_100_match_id.txt")
    matches_file = os.path.join(DATA_MATCHES, "my_100_matches.txt")
    with open(match_id_file, "r") as id_file, open(matches_file, "w") as matches_file:
        match_ids = id_file.readlines()
        for match_id in tqdm(match_ids):
            process_match_id = match_id.strip()
            if len(process_match_id) > 3:
                match_dict = get_match(process_match_id)
                match_json = json.dumps(match_dict)
                time.sleep(1.2)
                matches_file.write(match_json+"\n")
                # print("write match ", process_match_id)
            else:
                continue


def get_puuid_from_100_matches():
    """
    read my_100_matches.txt
    get list of puuid
    :return:
    """
    puuids = []
    matches_file = os.path.join(DATA_MATCHES, "my_100_matches.txt")
    with jsonlines.open(matches_file) as reader:
        for obj in tqdm(reader):
            players_puuid = obj["metadata"]["participants"]
            # print()

##################################################################################

if __name__ == "__main__":
    get_puuid_from_100_matches()