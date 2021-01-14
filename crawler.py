import requests


def crawl():
    r1 = requests.get("https://api.hearthstonejson.com/v1/70986/enUS/cards.json")
    f1 = open("./jsonFile/allCards.json", "wb")
    f1.write(r1.content)
    f1.close() 

    r2 = requests.get("https://hsreplay.net/analytics/query/battlegrounds_list_heroes/?BattlegroundsMMRPercentile=TOP_50_PERCENT&BattlegroundsTimeRange=LAST_7_DAYS")
    f2 = open("./jsonFile/battleGround.json", "wb")
    f2.write(r2.content)
    f2.close() 