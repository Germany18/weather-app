from main import Main
from condition import Condition
class Forecast: 
    def __init__(self, data):
        if data ["cod"] == 200:
            self.status = 200
            self.city = data ["name"]
            self.main = Main (data ["main"])
            for condition in data ["weather"]:
                self.condition = Condition (condition)
        else:
            self.status = 404