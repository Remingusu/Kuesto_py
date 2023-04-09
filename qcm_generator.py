from docx import Document
from docx.shared import Pt, Inches
from random import randint
from xlsx_extractor import Extractor


class Generator:
    def __init__(self, xlsx_file_name):
        work_dict = Extractor(xlsx_file_name)
