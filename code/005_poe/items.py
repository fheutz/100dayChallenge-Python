import json

# Items we want to sell via POE.ninja
poe_ninja = ["gem", "currency", "flask", "fragments", "scarabs", "incubators", "fossil", "resonators", "essences",
             "cards", "skill gems", "prophecies"]

# open Mapping for POE.trade
with open('sell_types.json') as json_data_file:
    type_mapping = json.load(json_data_file)

with open('poe_trade_form.json') as json_data_file:
    trade_form = json.load(json_data_file)


def item_name(item):
    return item["typeLine"] + item["name"]


def get_category(item):
    key = list(item["category"].keys())[0]
    if len(item["category"][key]) == 0:
        return key
    if len(item["category"][key]) >= 1:
        # TODO: Lists of itemtypes
        return item["category"][key][0]
    else:
        return "unclassified: " + key


def get_tradesite(item):
    if get_category(item) in poe_ninja:
        return "ninja"
    else:
        return "trade"


def get_price(item):
    if get_tradesite(item) == "trade":
        return poe_trade_price(item)
    else:
        return ninja_price(item)


def ninja_price(item):
    # TODO implement poe Ninja
    print("Ninja", "2c", item_name(item))


def parse_mod(mod):
    mod_name = "(pseudo) (total) +# to maximum Life"
    mod_min = 1
    mod_max = 100

    return (mod_name, mod_min, mod_max)


def poe_trade_price(item):
    itemForm = trade_form
    for key in type_mapping.keys():
        if get_category(item) in type_mapping[key]:
            itemForm["type"] = key
    if "explicitMods" in item:
        for mod in item["explicitMods"]:
            (mod_name, mod_min, mod_max) = parse_mod(mod)
            itemForm["mod_name"].append(mod_name)
            itemForm["mod_min"].append(mod_min)
            itemForm["mod_name"].append(mod_max)
