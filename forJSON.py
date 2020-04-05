# топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

from pprint import pprint
from collections import Counter


def popular_words():

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

    union_description = find_descriptions()

    def find_list_of_words():
        list_of_words = []
        for word in union_description:
            if len(word) > 6:
                list_of_words.append(word)
        return list_of_words

    list_of_words = find_list_of_words()

    popular_words = Counter(list_of_words)
    pprint(popular_words.most_common(10))

popular_words()