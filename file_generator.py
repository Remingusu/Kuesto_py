from docx import Document
from docx.shared import Pt, Inches
from questions_randomizer import Randomizer


class Generator:
    def __init__(self, xlsx_file_name: str, list_nbr_question: list):
        quest_and_answer = Randomizer('exemple', [2, 3]).dico_quest_ans
