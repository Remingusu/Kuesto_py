from random import shuffle
from xlsx_extractor import Extractor


class Randomizer:
    def __init__(self, xlsx_file_name: str, list_nbr_questions: list):
        work_dict = Extractor(xlsx_file_name).work_dict
        self.dico_quest_ans = {}
        for sheet in work_dict:
            list_questions = list(work_dict[sheet])
            shuffle(list_questions)
            self.dico_quest_ans[sheet] = {}
            for i in range(list_nbr_questions[0]):
                list_answers = list(work_dict[sheet][list_questions[0]])
                shuffle(list_answers)
                self.dico_quest_ans[sheet][list_questions[0]] = list_answers
                list_questions.pop(0)
            list_nbr_questions.pop(0)
