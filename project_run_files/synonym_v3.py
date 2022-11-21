#!/usr/bin/python3

import requests
import re
import collections
import json
import datetime

class synonym:
	def __init__(self):
		self.today_date = datetime.date.today()
		self.exp_period = datetime.timedelta(days=7)
		self.synonym_data = {}
	
	def load_data(self):
		try:
			synonym_file = open('synonym_data.json', 'r')
			self.synonym_data = collections.defaultdict(list, json.load(synonym_file))
			synonym_file.close()
		except Exception:
			print("(Synonyms Local Data-base not found and will be created.)")
			self.synonym_data = collections.defaultdict(list)

		return self.synonym_data
		
	def get_thesaurus(self, word):
		self.synonym_data[word] = []
		url = 'https://www.thesaurus.com/browse/' + word
		response = requests.get(url)
		url_content = response.text
		pattern_url = re.compile(r'"synonyms":\[({"similarity":"\d{2,3}","isInformal":"0","isVulgar":"0","term":"[a-zA-Z.\-\' ]+","targetTerm":"[a-zA-Z.\-\' ]+","targetSlug":"[a-z.\-%270]+"}[\]]?,)+')
		url_match = re.search(pattern_url, url_content)
		
		if url_match:
			pattern_synonyms = re.compile(r'"term":"([a-zA-Z.\-\' ]+)"')
			synonym_match = re.findall(pattern_synonyms, url_match.group(0))
			self.synonym_data[word].append(synonym_match)
		else:
			self.synonym_data[word].append(False)
		
		self.synonym_data[word].append(self.today_date + self.exp_period)
		synonym_file = open('synonym_data.json', 'w')
		synonym_file.write(json.dumps(self.synonym_data, indent=4, sort_keys=True, default=str))
		synonym_file.close()

		return self.synonym_data

	def check_update(self, word):
		word_exp_date = datetime.datetime.strptime(self.synonym_data[word][1], '%Y-%m-%d')

		if word_exp_date.date() > self.today_date:
			print("File has not yet expired.")
		else:
			print("File has EXPIRED, updating...")
			self.get_thesaurus(word)
			print("File has been updated.")
		
		return self.synonym_data

if __name__ == '__main__':
    my_synonyms = synonym()
    synonym_data = my_synonyms.load_data()
    user_input = input()
    
    for word in user_input.split():
        if word in synonym_data.keys():
            print("(word found in local data.)")
            synonym_data = my_synonyms.check_update(word)
        else:
            print("(word not found in local data, obtaining from Thesaurus.)")
            synonym_data = my_synonyms.get_thesaurus(word)
            
        word_synonyms = synonym_data[word][0]
        word_expiration = synonym_data[word][1]
        
        if word_synonyms != False:
            print("Synonyms: " + ', '.join(word_synonyms) + ".")
            print("Expiration Date: ", word_expiration)
        else:
            print("No synonyms found.")
