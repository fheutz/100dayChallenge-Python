import json

poe_ninja = ["gem", "currency", "flask", "fragments", "scarabs", "incubators", "fossil", "resonators", "essences", "divination cards", "skill gems", "prophecies"]

def item_name(item):
    return item["typeLine"] + item["name"]

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

def price_ring(item):
    return item_name(item) + "price ring"

def price_belt(item):
    return item_name(item) + "price belt"

trade_dict = {
    "ring" : price_ring,
    "belt" : price_belt,
}

def poe_trade_price(item):
    # print("Trade", get_category(item), item_name(item))
    if get_category(item) == "ring" or get_category(item) == "belt":
        print(trade_dict[get_category(item)](item))
