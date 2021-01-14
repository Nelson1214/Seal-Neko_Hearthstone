import os
from os import listdir
from jsonParse import *

def get_file_list():
    path = "./hs"
    file_lst = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
    return(file_lst)

def id_to_name(id):
    name=""
    dict_1 = hero_data()
    for i in dict_1:
        if(i.get_id() == id):
            name = i.get_name()
    return(name)

def name_to_id(name):
    id=0
    dict_1 = hero_data()
    for i in dict_1:
        if(i.get_name() == name):
            id = i.get_id()
    return(id)