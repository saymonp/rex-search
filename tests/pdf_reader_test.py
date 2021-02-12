from rex.pdf_reader import PdfReader

def test_read():
    pdf = PdfReader()

    # text = pdf.read(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")
    processo = r"G:/Trabalho/SEEB IJUI/Processo_0020469-52.2015.5.04.0601.pdf"
    text = pdf.read(processo)
    print(text)
    with open("processo_read.txt", "w", encoding='utf-8') as text_file:
        n = text_file.write(text)
        
def test_read_xml():
    pdf = PdfReader()

    text = pdf.read_xml(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/Completo.pdf")

    text_file = open("complete_read_xml.txt", "w", encoding='utf-8')
    n = text_file.write(text)
    text_file.close()

def test_read_by_page():
    pdf = PdfReader()

    text = pdf.read_by_page(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PAGAMENTO - tipo1.pdf")
    print(text)
    print(text[0])
    text_file = open("FOLHA DE PAGAMENTO TIPO1_read_by_page.txt", "w", encoding='utf-8')

    # for page in text:
    #     n = text_file.write("%s\n" % page)
    # text_file.close()

def test_parse_file():
    pdf = PdfReader()

    response = pdf.parse_from_file(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/FOLHA DE PRESENÇA - 12.2012.pdf")

    print(response)