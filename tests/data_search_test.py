from rex.data_search import DataSearch
from rex.pdf_reader import PdfReader

def test_search():
    with open('c:/Users/saymo/Desktop/rex-search/FOLHA DE PAGAMENTO TIPO1_read_by_page.txt', "r", encoding='utf-8') as f:
        text = f.read()
    
    dt = DataSearch()

    response = dt.search_type_1(text, "37709\.31")

    print(response)

def test_search_by_page_2():
    file = 'c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo2.pdf'
    pdf = PdfReader()

    pages = pdf.read_by_page(file)

    dt = DataSearch()
    dt.search_to_csv(pages, "37709", type=2)

def test_search_by_page_1():
    file = 'c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo1.pdf'
    pdf = PdfReader()

    pages = pdf.read_by_page(file)

    dt = DataSearch()
    dt.search_by_page(pages, "37709\.31", type=1)

def test_search_to_csv_type_1():
    file = 'c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo1.pdf'
    pdf = PdfReader()

    pages = pdf.read_by_page(file)

    dt = DataSearch()
    dt.search_by_page(pages, "37709\.31", type=1)

def test_get_extra_hours():
#     data = """fev/11 - 180,00 - Média 5,96 1,49 - - - - - -
# mar/11 1.444,16 180,00 12,03 Média 5,96 1,49 17,93 2,99 - - 6,24 27,16
# abr/11 1.140,13 180,00 9,50 Média 5,96 1,49 14,16 2,36 - - 7,08 23,59
# mai/11 1.140,13 180,00 9,50 Média 5,96 1,49 14,16 2,36 - - 5,79 22,31"""

    with open("c:/Users/saymo/Desktop/rex-search/horas.txt", "r", encoding='utf-8') as f:
        print(f)
        data = f.read()    
    print(data)
    dt = DataSearch()

    res = dt.get_extra_hours("1", "Cristiane Belmonte Penteado", data)

    print(res)

def test_search_all_by_page():
    folha_2010_2014 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 01.2010 A 06.2014.pdf'
    folha_2014_2017 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 07.2014 A 12.2017.pdf'
    folha_2018 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 2018.pdf'

    pdf = PdfReader()

    pages_2010_2014 = pdf.read_by_page(folha_2010_2014)
    pages_2014_2017 = pdf.read_by_page(folha_2014_2017)
    pages_2018 = pdf.read_by_page(folha_2018)

    dt = DataSearch()

    name = "EULANI DE FATIMA VINCENSI"
    id_1 = "29244\.12"
    id_2 = "29244"

    dict_2010_2014 = dt.search_by_page(pages_2010_2014, id_1, type=1)
    dict_014_2017 = dt.search_by_page(pages_2014_2017, id_2, type=2)
    dict_2018 = dt.search_by_page(pages_2018, id_2, type=2)

    dt.data_to_csv(id_2, name, dict_2010_2014, "w")
    dt.data_to_csv(id_2, name, dict_014_2017, "a")
    dt.data_to_csv(id_2, name, dict_2018, "a")

def test_search_all_by_page_bulk():
    folha_2010_2014 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 01.2010 A 06.2014.pdf'
    folha_2014_2017 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 07.2014 A 12.2017.pdf'
    folha_2018 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 2018.pdf'

    pdf = PdfReader()

    pages_2010_2014 = pdf.read_by_page(folha_2010_2014)
    pages_2014_2017 = pdf.read_by_page(folha_2014_2017)
    pages_2018 = pdf.read_by_page(folha_2018)

    dt = DataSearch()

    empolyees = [ 
                {"name": "ELAINE MARLI PIESANTI", "id_1":"39194\.63", "id_2":"39194"},
                {"name": "ELIANA CIUDROWSKI", "id_1":"36762\.34", "id_2":"36762"},
                {"name": "ELIANE FERNANDA HENTGES", "id_1":"36813\.43", "id_2":"36813"},
                {"name": "ELISA CARINA BECK", "id_1":"32150\.59", "id_2":"32150"},
                {"name": "ELISABETH REGINA MEOTTI OLIVEIRA", "id_1": "23522\.65", "id_2": "23522"},
                {"name": "ELISETE HAIDE DOLOVITSCH DURKS", "id_1":"36310\.28", "id_2":"36310"},
                {"name": "ERLINDA TEREZINHA PEDROSO ROSSNER", "id_1":"26232\.93", "id_2":"26232"},
                {"name": "EULANI DE FATIMA VINCENSI", "id_1":"29244\.12", "id_2":"29244"}]

    for e in empolyees:
        name = e["name"]
        id_1 = e["id_1"]
        id_2 = e["id_2"]

        dict_2010_2014 = dt.search_by_page(pages_2010_2014, id_1, type=1)
        dict_014_2017 = dt.search_by_page(pages_2014_2017, id_2, type=2)
        dict_2018 = dt.search_by_page(pages_2018, id_2, type=2)

        dt.data_to_csv(id_2, name, dict_2010_2014, "w")
        dt.data_to_csv(id_2, name, dict_014_2017, "a")
        dt.data_to_csv(id_2, name, dict_2018, "a")
