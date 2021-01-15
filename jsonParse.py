import json
from heroClass import Hero

def id_and_name():
    battle_grounds_hero_lst=[]
    id_to_name_lst=[]
    keys_lst=["dbfId", "name"]

    f = open('./jsonFile/allCards.json', encoding="utf-8") 
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

def id_and_data():
    f = open('./jsonFile/battleGround.json', encoding="utf-8")
    data = json.load(f)
    f.close()

    dict_hero = dict()
    for i in range(len(data["series"]["data"])):
        hero = Hero(data["series"]["data"][i])
        dict_hero[data["series"]["data"][i]["hero_dbf_id"]] = hero
    return(dict_hero)

def bind_id_and_name():
    lst = id_and_name()
    dict_hero = id_and_data()
    for i in lst:
        dict_hero[i["dbfId"]].set_name(i["name"])
    return(dict_hero)

def hero_data():
    allHero = list(bind_id_and_name().values())
    allHero.sort(key=lambda x: x.get_avg_final_placement())
    for hero in allHero:
        if (hero.get_avg_final_placement() < 4.5):
            hero.set_tier(2)
        elif (hero.get_avg_final_placement() < 4.75):
            hero.set_tier(3)
        else:
            hero.set_tier(4)
    allHero[0].set_tier(1)
    allHero.sort(key=lambda x: x.get_name())
    return(allHero)