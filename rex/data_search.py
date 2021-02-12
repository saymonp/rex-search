import re
import csv
from typing import List

from rex.pdf_reader import PdfReader


class DataSearch(object):

    def __init__(self):
        pass

    def search_type_1(self, data: str, id: str):
        """19967\.97"""
        employee = f"EMPREGADO - {id}\.\d{2} - .+"
        query = employee+"|\w\w\w\/201[0-8]|ORDENADO \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 1 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 2 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|REM\. VARIAVEL 3 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|COMISSAO FIXA \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ABONO DED\.INT\. \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|GRATIF OPER NEGOCIOS \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|BONUS \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ADIC\.REM\.COMP\.DISSID \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ADIC\.ACOR\.COL\.2008\/9 \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|GRATIF OPER NEGOCIOS \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|ANUENIO \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|PRORROG\.SAL\.MATERN\. \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|GRATIFIC\.CAIXA \s* (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"

        return re.findall(query, data)

    def search_type_2(self, data: str, id: str):
        employee = f"Empregado: {id} .+"
        query = employee+"|ANO: 201[1-8]|MÊS: \d{2}|V01 ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCK REMUNERACAO VARIAVEL 1 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCM REMUNERACAO VARIAVEL 2 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCL REMUNERACAO VARIAVEL 3 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|C01 COMPLEMENTO ORDENADO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V12 COMISSAO FIXA R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V17 ABONO DEDIC INTEGRAL - ADI R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCF BONUS VENDA CONSORCIO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 FERIAS NORMAIS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|A01 ORDENADO-AC COLETIVO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VF1 SALARIO ADIANTADO FERIAS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V13 ADIC REM COMP DISSID R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V15 ADIC\. ACOR\. COL\.2008\/9 R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VI7 ABONO DISSIDIO/ACORDO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V45 COMISSAO FIXA - SUBST\. R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VM1 SALARIO MATERNIDADE R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCE GRATIFIC OPERADOR NEGOCIOS R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V12 COMISSAO FIXA R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V21 ANUENIO R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V17 ABONO DEDIC INTEGRAL - ADI R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|V45 COMISSAO FIXA - SUBST\. R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))|VCR BONUS CONSORCIO POL INCENTI R\$ (?:(?<![\d])(?:(?:\d{1,2}\.)*\d{3}|(?:\d{1,3}))\,\d{2}(?!\d))"

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

    def search_by_page(self, pages: List[str], id: str, type: int):
        if type == 1:
            return self.search_by_page_type_1(pages, id)
        if type == 2:
            return self.search_by_page_type_2(pages, id)

    def search_by_page_type_2(self, pages: List[str], id: str):
        tocsv = []
        keys = []

        first = True

        for page in pages:
            matches = self.search_type_2(page, id)

            if matches[0].startswith(f"Empregado: {id}"):
                ordenado = bonusconpolin = adi = comfixsubst = comfix = anuenio = comfixasub = abono = comfixa = gratifop = salariomat = salaradi = adicrem = adicacor = comporde = feriasnorm = remvar1 = remvar1 = remvar2 = remvar3 = complemetoord = comfixa = abonodedic = bonus = salarioadi = ordenadocol = 0

                for m in matches:
                    if m.startswith("V01 ORDENADO"):
                        ordenado += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("C01 COMPLEMENTO ORDENADO"):
                        comporde += float(self.get_key_value(m)
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
                    if m.startswith("VCF BONUS VENDA CONSORCIO"):
                        bonus += float(self.get_key_value(m)
                                       [1].replace(".", "").replace(",", "."))
                    if m.startswith("VF1 FERIAS NORMAIS"):
                        feriasnorm += float(self.get_key_value(m)
                                            [1].replace(".", "").replace(",", "."))
                    if m.startswith("A01 ORDENADO-AC COLETIVO"):
                        ordenadocol += float(self.get_key_value(m)
                                             [1].replace(".", "").replace(",", "."))
                    if m.startswith("VF1 SALARIO ADIANTADO FERIAS"):
                        salaradi += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V13 ADIC REM COMP DISSID"):
                        adicrem += float(self.get_key_value(m)
                                         [1].replace(".", "").replace(",", "."))
                    if m.startswith("V15 ADIC. ACOR. COL.2008/9"):
                        adicacor += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("VI7 ABONO DISSIDIO/ACORDO"):
                        abono += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V45 COMISSAO FIXA - SUBST"):
                        comfixasub += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("VM1 SALARIO MATERNIDADE"):
                        salariomat += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("VCE GRATIFIC OPERADOR NEGOCIOS"):
                        gratifop += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V12 COMISSAO FIXA"):
                        comfix += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V21 ANUENIO"):
                        anuenio += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V17 ABONO DEDIC INTEGRAL - ADI"):
                        adi += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("V45 COMISSAO FIXA - SUBST"):
                            comfixsubst += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    if m.startswith("VCR BONUS CONSORCIO POL INCENTI"):
                            bonus += float(self.get_key_value(m)
                                          [1].replace(".", "").replace(",", "."))
                    

                dict_to_csv = {re.match("(Empregado: \d\d\d\d\d)", matches[0]).group(1): f"{self.get_month(matches[2])}/{self.get_year(matches[1])}",
                               "V01 Ordenado": str(ordenado).replace(".", ",") if ordenado > 0 else "",
                               "C01 COMPLEMENTO ORDENADO/A01 Ordenado AC Coletivo": str(comporde).replace(".", ",") if comporde > 0 else "",
                               "VCK Remuneração Variável 1": str(remvar1).replace(".", ",") if remvar1 > 0 else "",
                               "VCM Remuneração Variável 2": str(remvar2).replace(".", ",") if remvar2 > 0 else "",
                               "VCL Remuneração Variável 3": str(remvar3).replace(".", ",") if remvar3 > 0 else "",
                               #"A01 Ordenado AC Coletivo": str(ordenadocol).replace(".", ",") if ordenadocol > 0 else "",
                               "V15 ADIC. ACOR. COL.2008/9": str(adicacor).replace(".", ",") if adicacor > 0 else "",
                               "V13 ADIC REM COMP DISSID": str(adicrem).replace(".", ",") if adicrem > 0 else "",
                               #"VCE GRATIFIC OPERADOR NEGOCIOS": str(gratifop).replace(".", ",") if gratifop > 0 else "",
                               #"VI7 ABONO DISSIDIO/ACORDO": str(abono).replace(".", ",") if abono > 0 else "",
                               #"V45 COMISSAO FIXA - SUBST": str(comfixasub).replace(".", ",") if comfixasub > 0 else "",
                               #"VM1 SALARIO MATERNIDADE": str(salariomat).replace(".", ",") if salariomat > 0 else "",
                               "V17 ABONO DEDIC INTEGRAL - ADI": str(adi).replace(".", ",") if adi > 0 else "",
                               "BONUS/VCF BONUS VENDA CONSORCIO/VCR BONUS CONSORCIO POL INCENTI": str(bonus).replace(".", ",") if bonus > 0 else "",
                               "V12 COMISSAO FIXA/V45 COMISSAO FIXA - SUBST": str(comfix).replace(".", ",") if comfix > 0 else "",
                               #"VF1 Férias Normais": str(feriasnorm).replace(".", ",") if feriasnorm > 0 else "",
                               #"VF1 SALARIO ADIANTADO FERIAS": str(salaradi).replace(".", ",") if salaradi > 0 else "",
                               #"V45 COMISSAO FIXA - SUBST": str(comfixsubst).replace(".", ",") if comfixsubst > 0 else "",
                               #"VCR BONUS CONSORCIO POL INCENTI" : str(bonusconpolin).replace(".", ",") if bonusconpolin > 0 else "",
                               "VCE GRATIFIC OPERADOR NEGOCIOS": str(gratifop).replace(".", ",") if gratifop > 0 else "",
                               "V21 ANUENIO": str(anuenio).replace(".", ",") if anuenio > 0 else "",
                               }

                tocsv.append(dict_to_csv)

        return tocsv

    def search_by_page_type_1(self, pages: List[str], id: str):
        tocsv = []
        keys = []

        first = True

        for page in pages:
            matches = self.search_type_1(page, id)
            identifier = id.replace("\\", "")

            if matches[0].startswith(f"EMPREGADO - {identifier}"):

                for i in range(len(matches)):
                    if re.match("\w{3}\/\d{4}", matches[i]):
                        matches_separeted = (
                            matches[:i], [matches[0]]+matches[i:])
                        break
                not_first = False
                for list_matches in matches_separeted:
                    ordenado = comfixsubst = gratific = prosalmat = adi = anuenio = comfix = adicrem = gratifop = adicacor = bonusvenda = comporde = feriasnorm = remvar1 = remvar1 = remvar2 = remvar3 = complemetoord = comfixa = abonodedic = bonus = salarioadi = ordenadocol = 0
                    employee = re.search(
                        "(.+) \s* (\w{3}\/\d{4})", list_matches[0])

                    for m in list_matches:
                        if m.startswith("ORDENADO"):
                            ordenado += float(self.get_key_value_type_1(m)
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
                        if m.startswith("C01 COMPLEMENTO ORDENADO"):
                            complemetoord += float(self.get_key_value_type_1(m)
                                                   [1].replace(".", "").replace(",", "."))
                        if m.startswith("A01 ORDENADO-AC COLETIVO"):
                            complemetoord += float(self.get_key_value_type_1(m)
                                                 [1].replace(".", "").replace(",", "."))
                        if m.startswith("VCF BONUS VENDA CONSORCIO"):
                            bonus += float(self.get_key_value_type_1(m)
                                                [1].replace(".", "").replace(",", "."))
                        if m.startswith("ADIC.REM.COMP.DISSID"):
                            adicrem += float(self.get_key_value_type_1(m)
                                             [1].replace(".", "").replace(",", "."))
                        if m.startswith("ADIC.ACOR.COL.2008/9"):
                            adicacor += float(self.get_key_value_type_1(m)
                                              [1].replace(".", "").replace(",", "."))
                        if m.startswith("BONUS"):
                            bonus += float(self.get_key_value_type_1(m)
                                           [1].replace(".", "").replace(",", "."))
                        if m.startswith("GRATIF OPER NEGOCIOS"):
                            gratific += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("COMISSAO FIXA"):
                            comfix += float(self.get_key_value_type_1(m)
                                            [1].replace(".", "").replace(",", "."))
                        if m.startswith("ANUENIO"):
                            anuenio += float(self.get_key_value_type_1(m)
                                          [1].replace(".", "").replace(",", "."))
                        if m.startswith("ABONO DED.INT."):
                            adi += float(self.get_key_value_type_1(m)
                                          [1].replace(".", "").replace(",", "."))
                        if m.startswith("PRORROG.SAL.MATERN."):
                            prosalmat += float(self.get_key_value_type_1(m)
                                          [1].replace(".", "").replace(",", "."))     
                        if m.startswith("GRATIFIC.CAIXA"):
                            gratific += float(self.get_key_value_type_1(m)
                                          [1].replace(".", "").replace(",", "."))                       

                    dict_to_csv = {re.match("(EMPREGADO - \d\d\d\d\d\.\d\d)", employee.group(1)).group(1): list_matches[1] if not_first == True else employee.group(2),
                                   "V01 Ordenado": str(ordenado).replace(".", ",") if ordenado > 0 else "",
                                   "C01 COMPLEMENTO ORDENADO/A01 Ordenado AC Coletivo": str(complemetoord).replace(".", ",") if complemetoord > 0 else "",
                                   "VCK Remuneração Variável 1": str(remvar1).replace(".", ",") if remvar1 > 0 else "",
                                   "VCM Remuneração Variável 2": str(remvar2).replace(".", ",") if remvar2 > 0 else "",
                                   "VCL Remuneração Variável 3": str(remvar3).replace(".", ",") if remvar3 > 0 else "",
                                   #"VCF BONUS VENDA CONSORCIO": str(bonusvenda).replace(".", ",") if bonusvenda > 0 else "",
                                   #"A01 Ordenado AC Coletivo": str(ordenadocol).replace(".", ",") if ordenadocol > 0 else "",
                                   "V15 ADIC. ACOR. COL.2008/9": str(adicacor).replace(".", ",") if adicacor > 0 else "",
                                   "V13 ADIC REM COMP DISSID": str(adicrem).replace(".", ",") if adicrem > 0 else "",
                                   "V17 ABONO DEDIC INTEGRAL - ADI": str(adi).replace(".", ",") if adi > 0 else "",
                                   "BONUS/VCF BONUS VENDA CONSORCIO": str(bonus).replace(".", ",") if bonus > 0 else "",
                                   #"Prorrog. Sal. Matern.": str(prosalmat).replace(".", ",") if prosalmat > 0 else "",
                                   "V12 COMISSAO FIXA": str(comfix).replace(".", ",") if comfix > 0 else "",
                                   "VCE GRATIFIC OPERADOR NEGOCIOS/GRATIFIC.CAIXA": str(gratific).replace(".", ",") if gratific > 0 else "",
                                   "V21 ANUENIO": str(anuenio).replace(".", ",") if anuenio > 0 else "",
                                   #"VF1 Férias Normais": str(feriasnorm).replace(".", ",") if feriasnorm > 0 else "",
                                   }
                    not_first = True

                    tocsv.append(dict_to_csv)

        return tocsv

    def data_to_csv(self, id, name, tocsv, mode: str):
        keys = tocsv[0].keys()
        # identifier = id.replace("\\", "")

        with open(f'{id}-{name}.csv', mode, newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(tocsv)

    @staticmethod
    def get_extra_hours(self, data:str):
        hours = re.findall("\w{3}\/\d{2}.+", data)

        for h in hours:
            print(h.split()[5])