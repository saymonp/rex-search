from rex.data_search import DataSearch

def test_search():
    with open('c:/Users/saymo/Desktop/rex-search/FOLHA DE PAGAMENTO TIPO1_read_by_page.txt', "r", encoding='utf-8') as f:
        text = f.read()
    
    dt = DataSearch()

    response = dt.search_type_1(text, "37709\.31")

    print(response)

def test_search_to_csv_type_2():
    file = 'c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo2.pdf'
    
    dt = DataSearch()
    dt.search_to_csv(file, "37709", type=2)

def test_search_to_csv_type_1():
    file = 'c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo1.pdf'
    
    dt = DataSearch()
    dt.search_to_csv(file, "37709\.31", type=1)

