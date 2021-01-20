import re
import csv
from typing import List

from rex.pdf_reader import PdfReader


class DataSearch(object):

    def __init__(self):
        pass

    
    def search_type_1(self, data:str, id:str):
        """19967\.97"""
        employee = f"EMPREGADO - {id} - .+"
        query = employee+"|\w\w\w\/201[0-8]|ORDENADO \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 1 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 2 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 3 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ADIANT\.FERIAS \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|FERIAS NORMAIS 1\/3 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"

        return re.findall(query, data)

    def search_type_2(self, data:str, id:str):
        employee = f"Empregado: {id} .+"
        query = employee+"|ANO: 201[1-8]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 SALARIO ADIANTADO FERIAS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"

        return re.findall(query, data)

    def get_year(self, data):
        """Get only the year like year: 2017 return only 2017"""

        return re.search("\d{4}", data).group(0)

    def get_month(self, data):
        """Get only the month like month: 09 return only 09"""

        return re.search("\d{2}", data).group(0)

    def get_key_value(self, data):
        match = re.search(
            "(.+) R\$ ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))", data)

        return (match.group(1), match.group(2))
    
    def get_key_value_type_1(self, data):
        match = re.search(
            "(.+) ((?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d)))", data)

        return (match.group(1), match.group(2))

    def search_by_page(self, pages:List[str], id:str, type:int):
        if type == 1:
            return self.search_by_page_type_1(pages, id)
        if type == 2:
            return self.search_by_page_type_2(pages, id)
    
    def search_by_page_type_2(self, pages:List[str], id:str):
        tocsv = []
        keys = []

        first = True

        for page in pages:
            matches = self.search_type_2(page, id)

            if matches[0].startswith(f"Empregado: {id}"):
                ordenado = feriasnorm = ordenadocol = remvar1 = remvar1 = remvar2 = remvar3 = salarioadi = 0

                for m in matches:
                    if m.startswith("V01 ORDENADO"):
                        ordenado += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("VF1 FERIAS NORMAIS"):
                        feriasnorm += float(self.get_key_value(m)
                                            [1].replace(".", "").replace(",", "."))
                    if m.startswith("A01 ORDENADO-AC COLETIVO"):
                        ordenadocol += float(self.get_key_value(m)
                                             [1].replace(".", "").replace(",", "."))
                    if m.startswith("VCK REMUNERACAO VARIAVEL 1"):
                        remvar1 += float(self.get_key_value(m)
                                         [1].replace(".", "").replace(",", "."))
                    if m.startswith("VCM REMUNERACAO VARIAVEL 2"):
                        remvar2 += float(self.get_key_value(m)
                                         [1].replace(".", "").replace(",", "."))
                    if m.startswith("VCL REMUNERACAO VARIAVEL 3"):
                        remvar3 += float(self.get_key_value(m)
                                         [1].replace(".", "").replace(",", "."))
                    if m.startswith("VF1 SALARIO ADIANTADO FERIAS"):
                        salarioadi += float(self.get_key_value(m)
                                            [1].replace(".", "").replace(",", "."))

                dict_to_csv = {re.match("(Empregado: \d\d\d\d\d)", matches[0]).group(1): f"{self.get_month(matches[2])}/{self.get_year(matches[1])}",
                               "V01 Ordenado": str(ordenado).replace(".", ",") if ordenado > 0 else "",
                               "A01 Ordenado AC Coletivo": str(ordenadocol).replace(".", ",") if ordenadocol > 0 else "",
                               "VF1 Férias Normais": str(feriasnorm).replace(".", ",") if feriasnorm > 0 else "",
                               "VCK Remuneração Variável 1": str(remvar1).replace(".", ",") if remvar1 > 0 else "",
                               "VCM Remuneração Variável 2": str(remvar2).replace(".", ",") if remvar2 > 0 else "",
                               "VCL Remuneração Variável 3": str(remvar3).replace(".", ",") if remvar3 > 0 else "",
                               "VF1 Salário Adiantado Férias": str(salarioadi).replace(".", ",") if salarioadi > 0 else ""}

                tocsv.append(dict_to_csv)

        return tocsv

    def search_by_page_type_1(self, pages:List[str], id:str):
        tocsv = []
        keys = []

        first = True

        for page in pages:
            matches = self.search_type_1(page, id)
            identifier = id.replace("\\", "")
            
            if matches[0].startswith(f"EMPREGADO - {identifier}"):
                
                for i in range(len(matches)):
                    if re.match("\w{3}\/\d{4}", matches[i]):
                        matches_separeted = (matches[:i], [matches[0]]+matches[i:])
                        break
                not_first = False
                for list_matches in matches_separeted:       
                    ordenado = feriasnorm = ordenadocol = remvar1 = remvar1 = remvar2 = remvar3 = salarioadi = 0
                    employee = re.search("(.+) \s* (\w{3}\/\d{4})", list_matches[0])

                    for m in list_matches:
                        if m.startswith("ORDENADO"):
                            ordenado += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("VF1 FERIAS NORMAIS"):
                            feriasnorm += float(self.get_key_value_type_1(m)
                                                [1].replace(".", "").replace(",", "."))
                        if m.startswith("A01 ORDENADO-AC COLETIVO"):
                            ordenadocol += float(self.get_key_value_type_1(m)
                                                [1].replace(".", "").replace(",", "."))
                        if m.startswith("REM. VARIAVEL 1"):
                            remvar1 += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("REM. VARIAVEL 2"):
                            remvar2 += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("REM. VARIAVEL 3"):
                            remvar3 += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("FERIAS NORMAIS 1/3"):
                            salarioadi += float(self.get_key_value_type_1(m)
                                                [1].replace(".", "").replace(",", "."))
                    print(list_matches)
                    dict_to_csv = {re.match("(EMPREGADO - \d\d\d\d\d\.\d\d)", employee.group(1)).group(1): list_matches[1] if not_first == True else employee.group(2),
                                "V01 Ordenado": str(ordenado).replace(".", ",") if ordenado > 0 else "",
                                "A01 Ordenado AC Coletivo": str(ordenadocol).replace(".", ",") if ordenadocol > 0 else "",
                                "VF1 Férias Normais": str(feriasnorm).replace(".", ",") if feriasnorm > 0 else "",
                                "VCK Remuneração Variável 1": str(remvar1).replace(".", ",") if remvar1 > 0 else "",
                                "VCM Remuneração Variável 2": str(remvar2).replace(".", ",") if remvar2 > 0 else "",
                                "VCL Remuneração Variável 3": str(remvar3).replace(".", ",") if remvar3 > 0 else "",
                                "VF1 Salário Adiantado Férias": str(salarioadi).replace(".", ",") if salarioadi > 0 else ""}
                    not_first = True

                    tocsv.append(dict_to_csv)

        return tocsv

    def data_to_csv(self, id, name, tocsv, mode:str):
        keys = tocsv[0].keys()
        # identifier = id.replace("\\", "")

        with open(f'{id}-{name}.csv', mode, newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(tocsv)