import requests
import pprint
import json
from requests_html import HTMLSession

# Pretty Printer
pp = pprint.PrettyPrinter(indent=4)

# Load Stash
def load_stash():
    response = requests.get(url, cookies=cookie)
    return response.json()["items"]

def predict_item():
    session = HTMLSession()
    r = session.post("https://poe.trade/search", data=formdata)
    item_containers = r.html.find('tbody.item')
    for item in item_containers:
        print(item.attrs["data-name"], "\t\t\t", item.attrs["data-buyout"])

category_dict = {
    "tier2" : ["accessories", "weapons", "armour"],
    "tier1" : ["jewels", "gems", "currency", "flasks"]
}

poe_ninja = ["gem", "currency", "flask", "fragments", "scarabs", "incubators", "fossil", "resonators", "essences", "divination cards", "skill gems", "prophecies"]


def get_category(item):
    key = list(item["category"].keys())[0]
    if len(item["category"][key]) == 0:
        return key
    if len(item["category"][key]) >= 1:
        #TODO: Lists of itemtypes
        return item["category"][key][0]
    else:
        return "unclassified: " + key

def get_tradesite(item):
    item_category = get_category(item)
    if item_category in poe_ninja:
        name = item["typeLine"] + item["name"]
        print (name, "ninja")

for item in load_stash():
    tier = get_tradesite(item)
    name = item["typeLine"] + item["name"]

get_category(load_stash()[0])