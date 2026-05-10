import turtle as t

t.shape("turtle")
t.penup()

game_count = 0
played_games = []
stage = 1

# 처음 맵을 그리는 건데 정확한 사물의 배치를 몰라서 대충 만들었습니다.
def draw_map():
    t.clear()
    if stage == 1:
        t.goto(100, 100)
        t.dot(40, "blue")
        t.write(f"미니게임 (완료: {game_count}/3)", align="center")
        
        #미니게임 실행 후 암호 입력 창 등장, 입력
        if game_count >= 3:
            t.goto(-100, -100)
            t.dot(40, "red")
            t.write("암호를 입력하시오", align="center")
            
    elif stage == 2:
        t.bgcolor("lightgreen")
        t.goto(0, 0)
        t.write("STAGE 2", align="center", font=("Arial", 20, "bold"))
    
    t.goto(0, 0)

#암호, 미니게임
def check_interaction():
    global game_count, stage
    
    # 미니게임 해야 하는 물체 접촉 (100, 100)
    if stage == 1 and t.distance(100, 100) < 30:
        choice = t.textinput("게임 선택", "1:가위바위보, 2:야구, 3:행맨 (숫자 입력)")
        
        if choice in ["1", "2", "3"]:
            if choice not in played_games:
                played_games.append(choice)
                game_count += 1
                t.write(f"{choice}번 게임 클리어! (남은 게임: {3-game_count})", align="center")
            else:
                t.write("이미 클리어한 게임입니다!", align="center")
            
            t.backward(60)
            draw_map()

    #탈출구 (-100, -100) - 게임 3개 다 했을 때만 작동
    elif stage == 1 and game_count >= 3 and t.distance(-100, -100) < 30:
        pw = t.textinput("최종 관문", "모든 게임을 마쳤습니다. 암호를 입력하세요:")
        if pw == "1234":
            stage = 2
            draw_map()
        else:
            t.write("암호가 틀렸습니다!", align="center")
            t.backward(60)

#WASD 이동(여긴 잘 모르겠어서 찾아보고 하느라 오류가 있을 수도 있어요..)
def up():    t.sety(t.ycor() + 20); check_interaction()
def down():  t.sety(t.ycor() - 20); check_interaction()
def left():  t.setx(t.xcor() - 20); check_interaction()
def right(): t.setx(t.xcor() + 20); check_interaction()

#실행 중
draw_map()
t.listen()
t.onkeypress(up, "w")
t.onkeypress(down, "s")
t.onkeypress(left, "a")
t.onkeypress(right, "d")

t.mainloop()
