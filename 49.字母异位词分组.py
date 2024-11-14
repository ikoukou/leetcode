# 这题没有想到''.join()的用法，一直在纠结用dict.keys()去套每个字符串的字符

import collections

strs = ["eat", "tea", "btn", "abcd", "bcad", "ntd"]
res = collections.defaultdict(list)
for str in strs:
    i = ''.join(sorted(str))
    res[i].append(str)
print(list(res.values()))

res = {}
for str in strs:
    i = "".join(sorted(str))
    if i in res.keys():
        res[i].append(str)
    else:
        res[i] = [str]
print(list(res.values()))