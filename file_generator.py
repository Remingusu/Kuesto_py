from docx import Document
from docx.shared import Pt, Inches
from questions_randomizer import Randomizer


class Generator:
    def __init__(self, xlsx_file_name: str, list_nbr_question: list, nbr_copies: int, qcm_file_prefix: str):
        quest_and_answer = Randomizer('exemple', [2, 3]).dico_quest_ans
        print(quest_and_answer)
        for i in range(nbr_copies):
            file = Document()
            for sheet in quest_and_answer:
                quest_and_answer_ws = quest_and_answer[sheet]
                for question in quest_and_answer_ws.values():
                    quest_and_answer_wsiq = quest_and_answer_ws[question]
                    pg = file.add_paragraph(style='List Number').add_run(question)
                    pg.font.size = Pt(12)
                    pg.font.name = 'Calibri Light'
                    for i1 in range(len(quest_and_answer_wsiq)):
                        file.add_paragraph()
                        pg.paragraph_format.left_indent = Inches(0.24)
                        # interligne
                        pg_run = pg.add_run(f"□ {chr(65 + i1)}. {quest_and_answer_wsiq[i1]}")
                        pg_run.font.size = Pt(12)
                        pg_run.font.name = 'Calibri Light'
                file.add_paragraph()
            file.save(f'{qcm_file_prefix}_{i+1}.docx')


Generator('exemple', [2, 3], 2, 'my_exemple_qcm')
