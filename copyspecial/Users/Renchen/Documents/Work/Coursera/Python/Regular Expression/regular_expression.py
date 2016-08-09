import re

file = open("a2/regex_sum_248230.txt")
ret = 0
for line in file:
    findr = re.findall('[0-9]+', line)
    if findr:
        for val in findr:
            ret += int(val)

print ret
