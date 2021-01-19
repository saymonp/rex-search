from rex.data_search import DataSearch

def test_search():
    with open('c:/Users/saymo/Desktop/rex-search/test.txt', "r", encoding='utf-8') as f:
        text = f.read()
    
    dt = DataSearch()

    response = dt.search(text, 37709)

    print(response)
