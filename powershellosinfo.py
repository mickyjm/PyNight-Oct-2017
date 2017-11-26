f = open("txt/os.txt")
l = f.readline()
l1 = f.readline().replace('"',"").split(",")
l2 = f.readline().replace('"',"").split(",")
f.close()
l = dict(zip(l1, l2))
print l['SerialNumber']
