import pgzrun

TITLE = "Quiz Master"
WIDTH = 600
HEIGHT = 500

answer_boxes = []
x = 0 # for even numbered boxes
y = 200

def draw():
    global answer_boxes
    global x
    global y

    screen.fill(color="black")
    welcome_box = Rect(0,0,600,50)
    screen.draw.filled_rect(welcome_box, "green")

    question_box = Rect(0,70,430,100)
    screen.draw.filled_rect(question_box, "blue")

    x1 = 0 # for odd numbered boxes
    y1 = 330
    for i in range(4):
        if i % 2 != 0:
            answer_box = Rect(x1,y1,200,100)
            screen.draw.filled_rect(answer_box, "orange")
            screen.draw.textbox(str(i), answer_box)
            answer_boxes.append(answer_box)
            x1 += 230
        else:
            answer_box = Rect(x,y,200,100)
            screen.draw.filled_rect(answer_box, "orange")
            screen.draw.textbox(str(i), answer_box)
            answer_boxes.append(answer_box)
            x += 230



    
pgzrun.go()