from random import randint
from xlsx_extractor import Extractor


class Randomizer:
    def __init__(self, xlsx_file_name: str, list_nbr_question: list):
        list_questions = []
        self.dico_quest_ans = {}
        work_dict = Extractor(xlsx_file_name).work_dict
        print(work_dict)
        for sheet in work_dict:
            self.dico_quest_ans[sheet] = {}
            for question in work_dict[sheet]:
                list_questions.append(question)
            for i in range(list_nbr_question[0]):
                nbr_choose = randint(0, len(list_questions)-1)
                selected_question = list_questions[nbr_choose]
                self.dico_quest_ans[sheet][selected_question] = work_dict[sheet][selected_question]
                list_questions.remove(selected_question)
            list_questions.clear()
            list_nbr_question.pop(0)
