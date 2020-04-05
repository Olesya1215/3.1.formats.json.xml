from pprint import pprint
from collections import Counter


def find_descriptions():
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
            list_of_words.append(word)
    return list_of_words


def popular_words():
    union_description = find_descriptions()
    list_of_words = find_list_of_words(union_description)

    popular_words = Counter(list_of_words)
    pprint(popular_words.most_common(10))

popular_words()
