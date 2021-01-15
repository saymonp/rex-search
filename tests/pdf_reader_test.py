from rex.pdf_reader import PdfReader

def test_read():
    pdf = PdfReader()

    text = pdf.read(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")
    print(text)
    text_file = open("sample_read.txt", "w", encoding='utf-8')
    n = text_file.write(text)
    text_file.close()

def test_read_xml():
    pdf = PdfReader()

    text = pdf.read_xml(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")

    text_file = open("sample_read_xml.txt", "w", encoding='utf-8')
    n = text_file.write(text)
    text_file.close()

def test_read_by_page():
    pdf = PdfReader()

    text = pdf.read_by_page(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")
    print(len(text))
    print(text[0])
    text_file = open("sample_read_by_page.txt", "w", encoding='utf-8')
    for page in text:
        n = text_file.write("%s\n" % page)
    text_file.close()
