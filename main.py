from jsonParse import *
from crawler import crawl
from pyqt import *

if __name__ == "__main__":
    crawl()
    dict_1 = hero_data()
    print(len(dict_1))
    createView(dict_1)
    # for i in dict_1:
    #     print(i.get_name(), i.get_pick_rate())