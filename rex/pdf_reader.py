from tika import parser
import re

class PdfReader(object):

    def __init__(self):
        pass

    def read(self, file):
        # Parse data from file
        file_data = parser.from_file(file)
        # Get files text content
        text = file_data["content"]
        
        return text

    def read_xml(self, file):
        # Parse data from file
        file_data = parser.from_file(file, xmlContent=True)
        # Get files text content
        text = file_data["content"]

        return text

    def read_by_page(self, file):
        parsed_data_full = parser.from_file(file, xmlContent=True)
        parsed_data_full = parsed_data_full['content']

        return re.findall('<div class="page">(.[\s\S]*?)<\/div>', parsed_data_full)

    def parse_from_file(self, file=str):
        headers = {
            'X-Tika-PDFextractInlineImages': 'true',
        }
        parsed = parser.from_file(file)
        print(parsed)
        print(parsed['content'])
