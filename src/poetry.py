# -*- coding: utf-8 -*-

import re
import random

PATH = "input_utf8.txt"

def read_input(path):
	content = open(path).read()
	
	result = {}
	
	words = re.findall(r"[a-zA-Z]+", content)
	for n in xrange(len(words) - 1):
		word = words[n].lower()
		next_word = words[n + 1].lower()
		d = result[word] = result.get(word, {})
		#d["__count__"] += 1
		d[next_word] = d.get(next_word, 0)
		d[next_word] += 1
	
	return result

def create_poem(db):
	word = random.choice(db.keys())
	result = []
	while len(result) < 20:
		result.append(word)
		word = random.choice(db[word].keys()) 
		
	return " ".join(result)
	
if __name__ == '__main__':
	input = read_input(PATH)
	for i in xrange(10):
		print create_poem(input)