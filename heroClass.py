class Hero:
    def __init__(self, json_data):
        self._pick_rate = json_data["pick_rate"]
        self._popularity = json_data["popularity"]
        self._avg_final_placement = json_data["avg_final_placement"]
        self._final_placement_distribution = json_data["final_placement_distribution"]
        self._id = json_data["hero_dbf_id"]

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_pick_rate(self):
        return self._pick_rate

    def get_popularity(self):
        return self._popularity

    def get_avg_final_placement(self):
        return self._avg_final_placement

    def get_final_placement_distribution(self):
        return self._final_placement_distribution

    def get_id(self):
        return self._id

    def set_tier(self, tier):
        self._tier = tier
    
    def get_tier(self):
        return self._tier