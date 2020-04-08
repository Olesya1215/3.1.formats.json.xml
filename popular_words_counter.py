from pprint import pprint
from collections import Counter


def parse_json():
    import json
    with open("newsafr.json") as datafile:
        json_data = json.load(datafile)
        all_descriptions = json_data["rss"]["channel"]["items"]

        union_description = []
        for item in all_descriptions:
            description = item["description"].split()
            union_description += description
    return union_description


def parse_xml():
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")

    with open("newsafr.xml") as datafile:
        tree = ET.parse("newsafr.xml", parser)
        root = tree.getroot()
        channel = root.find("channel")
        items = channel.findall("item")
        union_description = []
        for item in items:
            description = item.find("description").text
            description = description.split()
            union_description += description
    return union_description


def find_list_of_words(union_description):
    list_of_words = []
    for word in union_description:
        if len(word) > 6:
            list_of_words.append(word.casefold())
    return list_of_words


def popular_words(format):
    if format == 'json':
        union_description = parse_json()
    elif format == 'xml':
        union_description = parse_xml()
    else:
        print('Неверный формат файла')
    list_of_words = find_list_of_words(union_description)

    popular_words = Counter(list_of_words)
    pprint(popular_words.most_common(10))


popular_words('json')
popular_words('xml')
