import re
fp = file('file_test.txt','r+')

txt = fp.readlines()

print txt

count = 0

for s in txt:
    c = re.findall("two",txt)
    if len(c) > 0:
        count = count + len(c)
print count
