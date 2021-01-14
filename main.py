from jsonParse import *
from crawler import crawl

if __name__ == "__main__":
    crawl()
    dict_hero = hero_data()
    for hero in dict_hero:
        print("\nname: ", hero.get_name())
        print("pick rate: ", hero.get_pick_rate())
        print("pop: ", hero.get_popularity())
        print("avg plcmnt: ", hero.get_avg_final_placement())
        print("plcmnt distr: ", hero.get_final_placement_distribution())
        print("id: ", hero.get_id(), "\n")