import re
import csv

from rex.pdf_reader import PdfReader

class DataSearch(object):

    def __init__(self):
        pass
    
    def get_id_from_name(self, name=str):
        ...

    def search(self, data=str, id=int):
        employee = f"Empregado: {str(id)} .+"
        query = employee+"|ANO: 201[1-8]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 SALARIO ADIANTADO FERIAS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"
        
        return re.findall(query, data) 

    def data_to_csv(self, data):
        ...
        """Empregado: 37709 .+|ANO: 201[1-4]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2} """
    
    def get_year(self, data):
        """Get only the year like year: 2017 return only 2017"""

        return re.search("\d{4}", data).group(0)

    def get_month(self, data):
        """Get only the month like month: 09 return only 09"""

        return re.search("\d{2}", data).group(0)

    def get_key_value(self, data):
        match = re.search("(.+) R\$ ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))", data)

        return (match.group(1), match.group(2))

    def search_to_csv(self, file=str, id=str):
        pdf = PdfReader()

        pages = pdf.read_by_page(file)

        tocsv = []
        keys = []

        first = True

        for page in pages:
            matches = self.search(page, id)

            if matches[0].startswith(f"Empregado: {id}"):
                ordenado = feriasnorm = ordenadocol = remvar1 = remvar1 = remvar2 = remvar3 = salarioadi = ""
            
                for m in matches:
                    if m.startswith("V01 ORDENADO"):
                        ordenado = self.get_key_value(m)[1]
                    if m.startswith("VF1 FERIAS NORMAIS"):
                        feriasnorm = self.get_key_value(m)[1]
                    if m.startswith("A01 ORDENADO-AC COLETIVO"):   
                        ordenadocol = self.get_key_value(m)[1]
                    if m.startswith("VCK REMUNERACAO VARIAVEL 1"):
                        remvar1 = self.get_key_value(m)[1]
                    if m.startswith("VCM REMUNERACAO VARIAVEL 2"):
                        remvar2 = self.get_key_value(m)[1]
                    if m.startswith("VCL REMUNERACAO VARIAVEL 3"):
                        remvar3 = self.get_key_value(m)[1]
                    if m.startswith("VF1 SALARIO ADIANTADO FERIAS"):
                        salarioadi = self.get_key_value(m)[1]

                print(matches[2], matches[1])
                dict_to_csv = {matches[0]: f"{self.get_month(matches[2])}/{self.get_year(matches[1])}",
                "V01 Ordenado": ordenado,
                "A01 Ordenado AC Coletivo": ordenadocol,
                "VF1 Férias Normais": feriasnorm,
                "VCK Remuneração Variável 1": remvar1,
                "VCM Remuneração Variável 2": remvar2,
                "VCL Remuneração Variável 3": remvar3,
                "VF1 Salário Adiantado Férias": salarioadi}

                if first == True:
                    keys = dict_to_csv.keys()
                    first = False

                tocsv.append(dict_to_csv)
        
        with open(f'{id}.csv', 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(tocsv)
        
        return {"ok": id}
  
