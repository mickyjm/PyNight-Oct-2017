import collections
f = open("txt/pwlist.txt")
count = collections.Counter(letter for line in f for letter in line.rstrip()).most_common()
print count[0][1] + count[1][1]
