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

def test_search_all_by_page():
    folha_2010_2014 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 01.2010 A 06.2014.pdf'
    folha_2014_2017 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 07.2014 A 12.2017.pdf'
    folha_2018 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 2018.pdf'

    pdf = PdfReader()

    pages_2010_2014 = pdf.read_by_page(folha_2010_2014)
    pages_2014_2017 = pdf.read_by_page(folha_2014_2017)
    pages_2018 = pdf.read_by_page(folha_2018)

    dt = DataSearch()

    name = "DANIELE CARLISE SCHOFFEL LIZOT"
    id_1 = "37908\.19"
    id_2 = "37908"

    dict_2010_2014 = dt.search_by_page(pages_2010_2014, id_1, type=1)
    dict_014_2017 = dt.search_by_page(pages_2014_2017, id_2, type=2)
    dict_2018 = dt.search_by_page(pages_2018, id_2, type=2)

    dt.data_to_csv(id_2, name, dict_2010_2014, "w")
    dt.data_to_csv(id_2, name, dict_014_2017, "a")
    dt.data_to_csv(id_2, name, dict_2018, "a")

