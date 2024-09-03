import pgzrun

WIDTH = 870
HEIGHT = 650
TITLE = "Quiz Game"

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,350)

score = 0
time_left = 10
questions = []
marquee_message = ""
question_count = 0
question_index = 0
is_game_over = False
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
question_file = "questions.txt"

marquee_box.move_ip(0,10)
question_box.move_ip(10,100)
timer_box.move_ip(670,100)
skip_box.move_ip(670,260)
answer_box1.move_ip(10,260)
answer_box2.move_ip(360,260)
answer_box3.move_ip(10,430)
answer_box4.move_ip(360,430)

def draw ():
    global marquee_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box, "sky blue")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, " green")
    screen.draw.filled_rect(skip_box, "dark green")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "orange")

    marquee_message = "Welcome to Quiz Master!"
    marquee_message = marquee_message + f"Q:{question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box, color="white")
    screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(0,5, 0,5), scolor="dim grey")
    screen.draw.textbox("Skip", skip_box, color ="white", angle=-90)
    screen.draw.textbox(question[0].strip(), question_box, color="white")

    index = 1
    for i in answer_boxes:
        screen.draw.textbox(question(index).strip(), i, color="black")
        index = index + 1

def move_marquee():
    marquee_box.x=marquee_box.x-2

    if marquee_box.right<0:
        marquee_box.left = WIDTH
     
def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.colidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index = index + 1
    if skip_box.collidepoint(pos):
        skip_question()

def game_over():
    global question, time_left, is_game_over
    message = f"Game Over!\n Your score is {score}!"
    question = [message, "-", "-", "-", "-"]
    time_left = 0
    is_game_over = True

def skip_question():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left-1
    else:
        game_over()

def correct_answer():
    global score, questions, time_left, question
    score = score + 1
    
    if questions:
        question = read_next_question()
        time_left = 10

    
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left, 1)



pgzrun.go()