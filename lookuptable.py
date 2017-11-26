import hashlib
f1 = open("txt/lookup_admin_pass.txt")
f2 = open("txt/top1000passwords.txt")
adminh = f1.readline().rstrip()
f1.close()
for line in f2:
    line = line.rstrip()
    if hashlib.sha512(line).hexdigest() == adminh:
        print line
        break
f2.close()
