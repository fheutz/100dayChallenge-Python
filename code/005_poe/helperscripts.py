import requests
from requests_html import HTMLSession
import json

def get_all_item_types():
    session = HTMLSession()
    r = session.get("http://poe.trade/")
    #   types = r.html.find('type_chosen > div > ul > li:nth-child(2)')
    types = r.html.find('.chosen-drop')
    print(types)
#    for type in types:
#        dict_type = type.attrs
#        print(dict_type["value"])

def get_explicit_groups():
    session = HTMLSession()
    r = session.get("http://poe.trade/")
    #   types = r.html.find('type_chosen > div > ul > li:nth-child(2)')
    types = r.html.find('#explicit-mods')
    print(types)
    for type in types:
        dict_type = type.attrs
        print(type)


#get_all_item_types()
get_explicit_groups()