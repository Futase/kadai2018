import sys
import re

pattern = re.compile("[!-/:-@[-`{-~]")
args = sys.argv
for i in range(0,len(args)):
	if args[i][-4:] == ".txt":
		fp = open(args[i])
		lines = fp.read().split()
		fp.close()
		words = []
		for j in range(0,len(lines)):
			foo = pattern.sub("",lines[j])
			if foo!="":
				words.append(foo)

		count_dict = {}
		for j in range(0,len(words)):
			if count_dict.get(words[j]):
				count_dict[words[j]] += 1
			else:
				count_dict[words[j]] = 1

		#sort in ascending order
		count_dict1 = sorted(count_dict.items(), key=lambda x: x[1], reverse = True)
		
		for j in range(0,10):
			print(count_dict1[j][0], count_dict1[j][1])
