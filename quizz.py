question = ['What is the name of the project', 'Second question', 'X']
answer = [0, 1, 0]
current_question_index = 0

def menu():
    print(question[current_question_index])
    answer_ = input("Enter answer: ")
    check_answer(answer_)
    next_question()

def check_answer(answer_):
    if answer_ == str(answer[current_question_index]):
        print("Correct")
    else:
        print("Wrong")

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(question):
        print(question[current_question_index])
    else:
        print("No more questions available.")
        menu()

while True:
    menu()