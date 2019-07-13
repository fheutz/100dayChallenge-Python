import json
import requests
from items import *
import pprint

with open('creds.json') as json_data_file:
    config = json.load(json_data_file)

pp = pprint.PrettyPrinter(indent=4)

# Config for POE
league = "legion"
stashNo = 2
url = "https://www.pathofexile.com/character-window/get-stash-items?league=" \
      + league + "&tabs=1&tabIndex=" \
      + str(stashNo) + "&accountName=" \
      + config["account"]

# Load Stash
def load_stash():
    response = requests.get(url,
                            cookies=config["cookie"],
                            proxies=config["proxies"])
    return response.json()["items"]

for item in load_stash():
    get_price(item)
