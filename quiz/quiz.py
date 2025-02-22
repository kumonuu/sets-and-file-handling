import pgzrun
import time

TITLE = "Quiz Master"
WIDTH = 600
HEIGHT = 500

questions = []
welcome_box = Rect(0,0,600,50)
timer_box = Rect(450,70,125,100)
skip_box = Rect(450,200,125,230)
countdown = 15
answer_boxes = []
score = 0
game_finished = False
question_number = 1

x0 = 0 # for even numbered boxes
y0 = 200
x1 = 0 # for odd numbered boxes
y1 = 330

for i in range(4):
    if i % 2 != 0: # odd
        answer_box = Rect(x1,y1,200,100)
        answer_boxes.append(answer_box)
        x1 += 230
    else: # even
        answer_box = Rect(x0,y0,200,100)
        answer_boxes.append(answer_box)
        x0 += 230

def move_welcome_box():
    welcome_box.left -= 10
    if welcome_box.left < -600:
        welcome_box.right = 1200

def read_questions_from_file():
    file = open("pgzero\quiz\questions.txt", "r")
    questions = file.readlines()
    file.close()
    
    return questions

questions = read_questions_from_file()

def get_one_question():
    global questions
    global question
    
    if questions: # if questions list if not empty
        question = questions.pop(0).split(",")
    return question

def draw():
    global answer_boxes
    
    screen.fill(color="black")
    screen.draw.filled_rect(welcome_box, "black")
    screen.draw.textbox("Welcome to Quiz Master!", welcome_box)

    question_box = Rect(0,70,430,100)
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.textbox(question[0], question_box)

    screen.draw.filled_rect(timer_box, "blue")
    screen.draw.textbox(str(countdown), timer_box)

    screen.draw.filled_rect(skip_box, "red")
    screen.draw.textbox("Skip", skip_box, angle=90)

    index = 1
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "orange")
        screen.draw.textbox(question[index], answer_box)
        index += 1

def update():
    move_welcome_box()

def game_over():
    global question
    global countdown
    countdown = 0
    question = ["Game Over, You got " + str(score) + "/10!","-","-","-","-","0"]

def update_timer():
    global countdown

    if countdown > 0:
        countdown -= 1
    elif game_finished:
        countdown = 0
    else:
        game_over()
    
 
def on_mouse_down(pos):
    global countdown
    
    index = 1
    for answer_box in answer_boxes:
        if answer_box.collidepoint(pos):
            if index == int(question[5]):
                handle_correct_answer()
            else:
                game_over()
        index += 1

    if skip_box.collidepoint(pos):
        get_one_question()
        countdown = 15

def congrats_screen():
    global question
    global countdown
    question = ["Congratulations! You got " + str(score) + "/10!","-","-","-","-","0"]
    countdown = 0

def handle_correct_answer():
    global question
    global countdown
    global score
    global game_finished
    global question_number
    
    if questions:
        question = get_one_question()
    print(questions)

    countdown = 15
    score += 1
    question_number += 1

    if question_number == 11:
        game_finished = True
        congrats_screen()

question = get_one_question()
clock.schedule_interval(update_timer, 1)

pgzrun.go()