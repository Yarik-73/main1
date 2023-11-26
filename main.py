from PyQt5.QtWidgets import QApplication
app = QApplication([])
from  Ter import*

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Наступне запитання')
btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)

def menu_generation():
    menu_win.show()
    window.hide()

btn_menu.cliked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_back.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_right_ans2.text(),
                     le_wrong_ans3.text())
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)

window.show()
app.exec_()