import set
import card
from set_question_builder import *

while True:
    answer_num, question_time, imported_set = intro()
    try:
        while True:
                question_display(answer_num, question_time, imported_set)
    except KeyboardInterrupt:
        pass
