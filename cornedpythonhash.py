import hashlib
f = open("txt/hash_list.txt")
count = 0
for line in f:
	l = line.split(" ")
	if hashlib.sha256(l[0].encode()).hexdigest() == l[1].rstrip():
		count = count + 1
print count
