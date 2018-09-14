#!/usr/bin/python3
queries = [[0,0], [1,1], [-1, -1]]
coordinate = [[2, 2], [2, 3]]
for item in coordinate:
	for lamp in queries:
		if abs(item[0] - lamp[0]) == abs(item[1] - lamp[1]):
			print("{} and {} are diagonal".format(item, lamp))
		else:
			print("{} and {} are NOT diagonal".format(item, lamp))

