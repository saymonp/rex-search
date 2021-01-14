from rex.pdf_reader import PdfReader

def test_read():
    pdf = PdfReader()

    text = pdf.read(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")

    print(text)

def test_read_xml():
    pdf = PdfReader()

    text = pdf.read_xml(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")

    print(text)

def test_read_by_page():
    pdf = PdfReader()

    text = pdf.read_by_page(r"c:/Users/saymo/Desktop/rex-search/tests/fixtures/test.pdf")

    print(text)
