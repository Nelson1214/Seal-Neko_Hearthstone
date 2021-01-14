import json

def id_to_name():
    battle_grounds_hero_lst=[]
    id_to_name_lst=[]
    keys_lst=["dbfId", "name"]

    f = open('all.json', encoding="utf-8") 
    data = json.load(f)
    f.close()

    for i in data:
        if "battlegroundsHero" in i:
            battle_grounds_hero_lst.append(i)

    for dict_1 in battle_grounds_hero_lst:
        dict_2 = dict_1.copy()
        for keys in dict_1.keys():
            if keys not in keys_lst:
                dict_2.pop(keys)
        id_to_name_lst.append(dict_2)

    return(id_to_name_lst)

def winrate():
    f = open('battleGround.json', encoding="utf-8") 
    data = json.load(f)
    f.close()

    