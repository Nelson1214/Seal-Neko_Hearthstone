from jsonParse import *
from crawler import crawl

if __name__ == "__main__":
    crawl()
    dict_1 = hero_data()
    for i in dict_1:
        print(i.get_name(), i.get_pick_rate())