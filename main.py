import time
from set_question_builder import *

while True:
    answer_num, question_time, imported_set = intro()
    try:
        while True:
                question_display(answer_num, question_time, imported_set)
                time.sleep(2)
    except KeyboardInterrupt:
        pass
