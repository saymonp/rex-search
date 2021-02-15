import pickle

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

    empolyees = [
        {"name": "MAITHE DE ALMEIDA RIBAS", "id": "39747"},
        {"name": "MARA MARCIANE PERSCH", "id": "38888"},
        {"name": "MARCIA CRISTIANE DE LIMA BRITTES", "id": "33557"},
        {"name": "MARELI TERESINHA DALCIN FREIBERGER", "id": "35192"},
        {"name": "MARIA ANALIA DE COUTO", "id": "28517"},
        {"name": "MARIA DE LOURDES DAL FORNO KINALSKI", "id": "23370"},
        {"name": "MARIA INES FOGACA DOS SANTOS", "id": "29341"},
        {"name": "MARIA TEREZA SCHEID", "id": "25652"},
        {"name": "MARIANE ELISA CARVALHO GRATSCH", "id": "36271"},
        {"name": "MARIANE LAUTERT CANDIDO", "id": "23135"},
        {"name": "MARILENE FATIMA ILGENFRITZ", "id": "25324"},
        {"name": "MARINA IVANI MAFALDA RODRIGUES", "id": "26622"},
        {"name": "MARISA PIENIZ SILVEIRA", "id": "37397"},
        {"name": "MARLENE BERNIERI", "id": "29161"},
        {"name": "MARLENE GRATSCH", "id": "20783"},
        {"name": "MARLI BEHLING SIKACZ", "id": "23768"},
        {"name": "MARLI TERESINHA SCHWEIG", "id": "27503"},
        {"name": "MIRTA BRAGA PEIXOTO", "id": "23472"}]

    with open('pages_2010_2014.pkl', 'rb') as f:
        pages_2010_2014 = pickle.load(f)

    with open('pages_2014_2017.pkl', 'rb') as f:
        pages_2014_2017 = pickle.load(f)

    with open('pages_2018.pkl', 'rb') as f:
        pages_2018 = pickle.load(f)

    dt = DataSearch()

    for e in empolyees:
        name = e["name"]
        id = e["id"]
        print(name, id)
        dict_2010_2014 = dt.search_by_page(pages_2010_2014, id, type=1)
        dict_014_2017 = dt.search_by_page(pages_2014_2017, id, type=2)
        dict_2018 = dt.search_by_page(pages_2018, id, type=2)

        mode = "a"

        if len(dict_2010_2014) > 0:
            print(dict_2010_2014)
            dt.data_to_csv(id, name, dict_2010_2014, "w")
        else:
            mode = "w"
        if len(dict_014_2017) > 0:
            # print(mode)
            dt.data_to_csv(id, name, dict_014_2017, mode)
            mode = "a"
        if len(dict_2018) > 0:
            # print(dict_2018)
            dt.data_to_csv(id, name, dict_2018, mode)


def test_serialize():
    folha_2010_2014 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 01.2010 A 06.2014.pdf'
    folha_2014_2017 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 07.2014 A 12.2017.pdf'
    folha_2018 = 'G:/Trabalho/SEEB IJUI/SEEB IJUI CD/FOLHA DE PAGAMENTO - 2018.pdf'

    pdf = PdfReader()

    pages_2010_2014 = pdf.read_by_page(folha_2010_2014)
    pages_2014_2017 = pdf.read_by_page(folha_2014_2017)
    pages_2018 = pdf.read_by_page(folha_2018)

    with open('pages_2010_2014.pkl', 'wb') as f:
        pickle.dump(pages_2010_2014, f)

    with open('pages_2014_2017.pkl', 'wb') as f:
        pickle.dump(pages_2014_2017, f)

    with open('pages_2018.pkl', 'wb') as f:
        pickle.dump(pages_2018, f)


def test_deserialize():
    with open('pages_2010_2014.pkl', 'rb') as f:
        mynewlist = pickle.load(f)

    return mynewlist
