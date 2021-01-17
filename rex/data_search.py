import re

class DataSearch(object):

    def __init__(self):
        pass
    
    def get_id_from_name(self, name=str):
        ...

    def search(self, data=str, name=None, id=None):
        if name:
            query = f"EMPREGADO — \d+\.\d+ |CLAUDIO OLDEMAR KOHLMANN| \D\D\D\/201[0-8]|MENSAL\.SINDICAL (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ABONO DED\.INT\. (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|\D\D\D\/201[0-8]"
        print(query)
        return re.findall("EMPREGADO — \d+\.\d+ |CLAUDIO OLDEMAR KOHLMANN| \D\D\D\/201[0-8]|MENSAL\.SINDICAL (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ABONO DED\.INT\. (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|\D\D\D\/201[0-8]", data) 

    def data_to_csv(self, data):
        ...