import requests
import re
import collections
import json
import datetime

today_date = datetime.date.today()
exp_period = datetime.timedelta(days=7)
synonym_data = {}

def get_thesaurus(word, renew=False):
    url = 'https://www.thesaurus.com/browse/' + word
    response = requests.get(url)
    url_content = response.text
    pattern_url = re.compile(r'"synonyms":\[({"similarity":"\d{2,3}","isInformal":"0","isVulgar":"0","term":"[a-zA-Z.\-\' ]+","targetTerm":"[a-zA-Z.\-\' ]+","targetSlug":"[a-z.\-%270]+"}[\]]?,)+')
    url_match = re.search(pattern_url, url_content)
    if url_match:
        pattern_synonyms = re.compile(r'"term":"([a-zA-Z.\-\' ]+)"')
        synonym_match = re.findall(pattern_synonyms, url_match.group(0))
        if renew:
            synonym_data[word][0] = synonym_match
            synonym_data[word][1] = today_date + exp_period
        else:
            synonym_data[word].append(synonym_match)
            synonym_data[word].append(today_date + exp_period)
            print("Synonyms: " + ', '.join(synonym_data[word][0]) + ".")
        synonym_file = open('synonym_data.json', 'w')
        synonym_file.write(json.dumps(synonym_data, indent=4, sort_keys=True, default=str))
        synonym_file.close()
    else:
        print("No Synonyms found.")

def update_word(word):
    word_exp_date = datetime.datetime.strptime(synonym_data[word][1], '%Y-%m-%d')

    if word_exp_date.date() > today_date:
        print("File has not yet expired.")
    else:
        print("File has EXPIRED.")
        get_thesaurus(word, renew=True)
        print("File has been updated, with new expiration date: ", synonym_data[word][1])

if __name__ == '__main__':
    try:
        synonym_file = open('synonym_data.json', 'r')
        synonym_data = collections.defaultdict(list, json.load(synonym_file))
        synonym_file.close()
    except Exception:
        print("(Synonyms Local Data-base not found and will be created.)")
        synonym_data = collections.defaultdict(list)

    word = input("Enter a word: ")

    if word in synonym_data.keys():
        print("(word found in local data.)")
        print("Synonyms: " + ', '.join(synonym_data[word][0]) + ".")
        print("Expiration Date: ", synonym_data[word][1])
        update_word(word)
    else:
        print("(word not found in local data, obtaining from Thesaurus.)")
        get_thesaurus(word, renew=False)