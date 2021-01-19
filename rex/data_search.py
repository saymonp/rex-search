import re

class DataSearch(object):

    def __init__(self):
        pass
    
    def get_id_from_name(self, name=str):
        ...

    def search(self, data=str, id=int):
        """37709"""
        """"EMPREGADO — \d+\.\d+ |CLAUDIO OLDEMAR KOHLMANN| \D\D\D\/201[0-8]|MENSAL\.SINDICAL (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ABONO DED\.INT\. (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|\D\D\D\/201[0-8]"""
        employee = f"Empregado: {str(id)} .+"
        query = employee+"|ANO: 201[0-8]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"
        
        return re.findall(query, data) 

    def data_to_csv(self, data):
        ...
        """Empregado: 37709 .+|ANO: 201[1-4]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2} """
    
    def get_year(self, data):
        """Get only the year like ANO: 2017 return only 2017"""

        return re.search("\d{4}", data).group(0)

    def get_month(self, data):
        """Get only the month like MÊS: 09 return only 09"""

        return re.search("\d{2}", data).group(0)
    
    def get_ordenado(self, data):
        query = "(V01 ORDENADO) R\$ ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))"
        match = re.search(query, data)

        return (match.group(1), match.group(2))

    def get_remuneracao_variavel(self, data):
        match = re.search("(\w\w\w REMUNERACAO VARIAVEL \d) R\$ ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))", data)
        
        return (match.group(1), match.group(2)) 

    def get_key_value(self, data):
        match = re.search("(.+) R\$ ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))", data)

        return (match.group(1), match.group(2))
