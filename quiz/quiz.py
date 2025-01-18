import pgzrun

TITLE = "Quiz Master"
WIDTH = 600
HEIGHT = 500

answer_boxes = []
welcome_box = Rect(0,0,600,50)

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
    
    question = questions.pop(0).split(",")
    
    return question

def draw():
    global answer_boxes
    
    x0 = 0 # for even numbered boxes
    y0 = 200
    x1 = 0 # for odd numbered boxes
    y1 = 330
    
    screen.fill(color="black")
    screen.draw.filled_rect(welcome_box, "black")
    screen.draw.textbox("Welcome to Quiz Master!", welcome_box)

    question_box = Rect(0,70,430,100)
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.textbox(question[0], question_box)

    for i in range(4):
        if i % 2 != 0: # odd
            answer_box = Rect(x1,y1,200,100)
            screen.draw.filled_rect(answer_box, "orange")
            screen.draw.textbox(question[i+1], answer_box)
            answer_boxes.append(answer_box)
            x1 += 230
        else: # even
            answer_box = Rect(x0,y0,200,100)
            screen.draw.filled_rect(answer_box, "orange")
            screen.draw.textbox(question[i+1], answer_box)
            answer_boxes.append(answer_box)
            x0 += 230

def update():
    move_welcome_box()

def on_mouse_down(pos):
    index = 1
    
    for answer_box in answer_boxes:
        if answer_box.collidepoint(pos):
            if index == int(question[5]):
                print("correct answer")
                handle_correct_answer()
        index += 1

def handle_correct_answer():
    global question

    question = get_one_question()

question = get_one_question()

pgzrun.go()