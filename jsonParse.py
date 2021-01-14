import json

f = open('all.json', encoding="utf-8") 
data = json.load(f) 
list=[]
for i in data:
    if "battlegroundsHero" in i:
        list.append(i)
f.close()
print(list)