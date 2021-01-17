from rex.data_search import DataSearch

def test_search():
    with open('c:/Users/saymo/Desktop/rex-search/sample_read_by_page.txt', "r", encoding='utf-8') as f:
        text = f.read()
    
    # text = open('c:/Users/saymo/Desktop/rex-search/sample_read_by_page.txt', "r", encoding='utf-8')
    print(text)
    dt = DataSearch()
    #print(text)
    response = dt.search(text, "CLAUDIO OLDEMAR KOHLMANN")

    print(response)
