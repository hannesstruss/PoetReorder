# -*- coding: utf-8 -*-

import re
import random
import math

def read_input(path):
	content = open(path).read()
	
	result = {}
	
	words = re.findall(r"[a-zA-ZäöüÄÖÜß']+", content)
	for n in xrange(len(words) - 1):
		word = words[n].lower()
		next_word = words[n + 1].lower()
		d = result[word] = result.get(word, {})
		#d["__count__"] += 1
		d[next_word] = d.get(next_word, 0)
		d[next_word] += 1
	
	return result

def get_most_common_follower(followers):
	result = None
	max_count = 0
	for follower, count in followers.iteritems():
		if count > max_count:
			result = follower
			max_count = count
	return result

def get_gaussian_distributed_follower(follower_list):
	rnd = min(len(follower_list) - 1, int(abs(random.gauss(0, 0.05)) * len(follower_list)))
	return follower_list[rnd]

def create_poem(db):
	word = random.choice(db.keys())
	result = []
	while len(result) < 20:
		result.append(word)
		#word = random.choice(db[word].keys())
		word = get_gaussian_distributed_follower(get_sorted_follower_list(db[word]))
		
	return " ".join(result)

def get_sorted_follower_list(followers):
	return map(lambda x: x["k"], sorted(
		[{"k": key, "v": value} for key,value in followers.iteritems()],
		key=lambda a: a["v"],
		reverse=True
	))

def get_pretty_follower_list(word, db):
	followers = db[word]
	result = [word]
	for x in get_sorted_follower_list(followers):
		result.append("%s\t\t\t%s" % (x["word"], x["count"]))
		
	return "\n".join(result)
	
if __name__ == '__main__':
	input = read_input("heine_wintermaerchen.txt")
	for i in xrange(10):
		print create_poem(input)
