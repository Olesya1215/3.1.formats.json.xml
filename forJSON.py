from pprint import pprint
from collections import Counter


def find_descriptions():
    import json
    with open("newsafr.json") as datafile:
        json_data = json.load(datafile)
        all_descriptions = json_data["rss"]["channel"]["items"]

        union_description = []
        for item in all_descriptions:
            description = item["description"].split()
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
