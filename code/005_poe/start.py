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

def create_form(item_json):
    formdata = {
        "league": "Legion",
        "type": "",
        "base": "",
        "name": "",
        "dmg_min": "",
        "dmg_max": "",
        "aps_min": "",
        "aps_max": "",
        "crit_min": "",
        "crit_max": "",
        "dps_min": "",
        "dps_max": "",
        "edps_min": "",
        "edps_max": "",
        "pdps_min": "",
        "pdps_max": "",
        "armour_min": "",
        "armour_max": "",
        "evasion_min": "",
        "evasion_max": "",
        "shield_min": "",
        "shield_max": "",
        "block_min": "",
        "block_max": "",
        "sockets_min": "",
        "sockets_max": "",
        "link_min": "",
        "link_max": "",
        "sockets_r": "",
        "sockets_g": "",
        "sockets_b": "",
        "sockets_w": "",
        "linked_r": "",
        "linked_g": "",
        "linked_b": "",
        "linked_w": "",
        "rlevel_min": "",
        "rlevel_max": "",
        "rstr_min": "",
        "rstr_max": "",
        "rdex_min": "",
        "rdex_max": "",
        "rint_min": "",
        "rint_max": "",
        "mod_name": "",
        "mod_min": "",
        "mod_max": "",
        "mod_weight": "",
        "group_type": "",
        "group_min": "",
        "group_max": "",
        "group_count": "",
        "q_min": "",
        "q_max": "",
        "level_min": "",
        "level_max": "",
        "ilvl_min": "",
        "ilvl_max": "",
        "rarity": "",
        "progress_min": "",
        "progress_max": "",
        "sockets_a_min": "",
        "sockets_a_max": "",
        "map_series": "",
        "altart": "",
        "identified": "",
        "corrupted": "",
        "shaper": "",
        "elder": "",
        "crafted": "",
        "enchanted": "",
        "mirrored": "",
        "veiled": "",
        "fractured": "",
        "synthesised": "",
        "seller": "",
        "thread": "",
        "online": "",
        "capquality": "",
        "buyout_min": "",
        "buyout_max": "",
        "buyout_currency": "",
        "exact_currency": "",
        "has_buyout": ""
    }
    formdata["rarity"] = item_json

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
