#Occurance of digit in array
a=[22,22,22,22,33,11]
hash={}
for item in a:
    hash[item]=hash.get(item,0)+1
print(hash)

#Max occurance of a value
a=[22,22,22,22,33,11]
hash={}
for item in a:
    hash[item]=hash.get(item,0)+1
a=(max(hash.values()))
key=[k for k,v in hash.items() if v==a]
print(key[0])