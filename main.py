# -*- coding: utf-8 -*-
import turtle as t
import random
import blackJack
import numBaseball
import rsp
import hangman

t.shape("turtle")
t.penup()
t.speed(0)

current_stage = 1
is_loading = False        
is_interacting = False    

has_desk_ch1 = has_bed_ch1 = has_closet_ch1 = has_drawer_ch1 = False
has_bed_ch2 = has_desk_ch2 = has_drawer_ch2 = has_game_ch2 = False
has_desk_ch3 = has_rope_ch3 = has_recorder_ch3 = has_paper_ch3 = False
has_file_ch4 = has_shovel_ch4 = has_cloth_ch4 = has_blackjack_ch4 = False

COORD_DOOR = (0, 150)
COORD_A = (150, 150)    
COORD_B = (-150, -150)  
COORD_C = (150, -150)   
COORD_D = (-150, 150)      

screen = t.Screen()

def draw_map():
    global is_loading
    is_loading = True
    t.hideturtle()
    t.clear()
    t.penup()
    screen.bgcolor("#222222")
    
    t.goto(COORD_DOOR); t.dot(40, "red"); t.write(" [Door/Table]", align="center")
    t.goto(COORD_A); t.dot(40, "#8B4513"); t.write(" [A]", align="center")
    t.goto(COORD_B); t.dot(40, "#4682B4"); t.write(" [B]", align="center")
    t.goto(COORD_C); t.dot(40, "#8A2BE2"); t.write(" [C]", align="center")
    t.goto(COORD_D); t.dot(40, "#2E8B57"); t.write(" [D]", align="center")
    
    t.goto(0, 0)
    t.showturtle()
    
    print("\n--- STAGE {0} START ---".format(current_stage))
    if current_stage == 1:
        print("녹색이 서랍, 갈색이 책상, 보라색이 옷장, 파란색이 침대인 것 같다.")
    elif current_stage == 2:
        print("녹색이 게임, 갈색이 책상, 보라색이 서랍, 파란색이 침대인 것 같다.")
    elif current_stage == 3:
        print("녹색이 종이, 갈색이 책상, 보라색이 녹음기, 파란색이 밧줄인 것 같다.")
    elif current_stage == 4:
        print("녹색이 신분증, 갈색이 파일, 보라색이 천, 파란색이 삽인 것 같다.")
    is_loading = False

def disable_keys():
    screen.onkey(None, "w"); screen.onkey(None, "s")
    screen.onkey(None, "a"); screen.onkey(None, "d")

def enable_keys():
    screen.onkey(up, "w"); screen.onkey(down, "s")
    screen.onkey(left, "a"); screen.onkey(right, "d")
    screen.listen()

def check_interaction():
    global is_interacting, current_stage, has_blackjack_ch4
    global has_desk_ch1, has_bed_ch1, has_closet_ch1, has_drawer_ch1
    global has_bed_ch2, has_desk_ch2, has_drawer_ch2, has_game_ch2
    global has_desk_ch3, has_rope_ch3, has_recorder_ch3, has_paper_ch3
    global has_file_ch4, has_shovel_ch4, has_cloth_ch4
    
    if is_loading or is_interacting: return
    is_interacting = True
    
    try:
        if t.distance(COORD_DOOR) < 40:
            t.backward(40)
            disable_keys()
            if current_stage == 4 and has_blackjack_ch4:
                print("\n[카드 테이블을 조사하자 진실을 마주할 선택지가 떠올랐다.]")
                print("1. 진실을 받아들인다.")
                print("2. 기억을 지우고 처음으로 돌아간다.")
                print("3. 끝까지 그를 사기꾼이라고 주장한다.")
                choice = input("선택: ")
                if choice == "1": 
                    print("\n[진실: 무너지는 기억]"); print("주인공은 떨리는 손으로 머리를 감싸 쥐었다. 밀려드는 기억 속에서 피해자는 사기꾼이 아니었다. 그는 진실을 파헤치던 암행 경찰이었다.")
                    print("자신이 그를 납치하고 죽음에 이르게 했다는 끔찍한 사실이 톱니바퀴처럼 맞춰진다. 주인공은 결국 바닥에 주저앉아 오열하며 자신의 죄를 인정했다.")
                elif choice == "2": 
                    print("\n[엔딩: 영원한 굴레]"); print("주인공은 고개를 저으며 생각을 멈췄다. 이 지독한 진실을 마주할 용기가 없었다. 기억의 파편을 강제로 지우는 장치를 작동시킨다.")
                    print("시야가 하얗게 점멸하고, 모든 것이 리셋된다. 다시 1점의 방, 차가운 바닥 위에서 눈을 뜬다. 아무것도 기억하지 못한 채, 지옥 같은 반복의 첫 발을 다시 내딛는다.")
                elif choice == "3": 
                    print("\n[엔딩: 뒤틀린 현실]"); print("주인공은 분노를 내뱉으며 끝까지 피해자를 사기꾼이라 몰아세웠다. 시스템은 그의 현실 인식을 '실패'로 규정한다.")
                    print("더욱 깊은 교화 단계가 시작된다. 더 어둡고 복잡한, 끝없는 기억 복구의 미궁 속으로 주인공은 끌려 들어간다.")
            elif current_stage == 4:
                if blackJack.play(): has_blackjack_ch4 = True
            else:
                target_pwd = None
                if current_stage == 1 and has_desk_ch1 and has_bed_ch1 and has_closet_ch1 and has_drawer_ch1: target_pwd = "7294"
                elif current_stage == 2 and has_desk_ch2 and has_bed_ch2 and has_drawer_ch2 and has_game_ch2: target_pwd = "312"
                elif current_stage == 3 and has_desk_ch3 and has_rope_ch3 and has_recorder_ch3 and has_paper_ch3: target_pwd = "납치"
                if target_pwd:
                    pwd = input("Password: ")
                    if pwd == target_pwd: current_stage += 1; draw_map()
                    else: print("비밀번호가 다릅니다.")
                else: print("단서가 더 필요할 것 같다.")
            enable_keys()
        
        elif current_stage == 1:
            if t.distance(COORD_A) < 40 and not has_desk_ch1: t.backward(40); has_desk_ch1 = True; print("7일 안에 갚을 것...7")
            elif t.distance(COORD_B) < 40 and not has_bed_ch1: t.backward(40); has_bed_ch1 = True; print("침대 밑에 메모가 있다. 2번째 기회...2")
            elif t.distance(COORD_C) < 40 and not has_closet_ch1: t.backward(40); has_closet_ch1 = True; print("옷장 안엔 찢어진 복권이 있었다. 90000+0...9")
            elif t.distance(COORD_D) < 40 and not has_drawer_ch1: t.backward(40); has_drawer_ch1 = True; print("서랍 안엔 찢어진 복권이 있었다. 00004+0...4")
        elif current_stage == 2:
            if t.distance(COORD_A) < 40 and not has_desk_ch2: t.backward(40); has_desk_ch2 = True; print("낡은 카드(1)와 겜블 칩이 있다.")
            elif t.distance(COORD_B) < 40 and not has_bed_ch2: t.backward(40); has_bed_ch2 = True; print("찢어진 복권(3)이 있다.")
            elif t.distance(COORD_C) < 40 and not has_drawer_ch2: t.backward(40); has_drawer_ch2 = True; print("사기꾼(2)이라고 적힌 메모가 있다.")
            elif t.distance(COORD_D) < 40 and not has_game_ch2:
                t.backward(40); disable_keys()
                print("작은 게임기 화면에 글자가 떠 있다. '이기면 그날의 판을 보여주겠다.'")
                if rsp.play(): print("승리! 순서: 복권 > 카드 > 사기꾼"); has_game_ch2 = True
                enable_keys()
        elif current_stage == 3:
            if t.distance(COORD_A) < 40 and not has_desk_ch3: t.backward(40); has_desk_ch3 = True; print("피해자를 사기꾼이라 써놓은 나의 메모다.")
            elif t.distance(COORD_B) < 40 and not has_rope_ch3: t.backward(40); has_rope_ch3 = True; print("누군가를 묶었던 듯한 밧줄이다.")
            elif t.distance(COORD_C) < 40 and not has_recorder_ch3: t.backward(40); has_recorder_ch3 = True; print("녹음기 너머로 피해자의 음성이 흘러 나온다.")
            elif t.distance(COORD_D) < 40 and not has_paper_ch3:
                t.backward(40); disable_keys()
                if hangman.play("kidnap"): print("정답! 단서 '납치' 획득"); has_paper_ch3 = True
                enable_keys()
        elif current_stage == 4:
            if t.distance(COORD_A) < 40 and not has_file_ch4: t.backward(40); has_file_ch4 = True; print("파일 획득: 사건 장소, 납치, 감금 내용이 나와 있다.")
            elif t.distance(COORD_B) < 40 and not has_shovel_ch4: t.backward(40); has_shovel_ch4 = True; print("삽 획득: 삽 끝에 흙이 묻어 있다.")
            elif t.distance(COORD_C) < 40 and not has_cloth_ch4: t.backward(40); has_cloth_ch4 = True; print("천 획득: 낡은 천에 핏자국이 있다.")
            elif t.distance(COORD_D) < 40: print("신분증 획득: 피해자는 암행 경찰이었다.")
    finally:
        is_interacting = False

def up(): t.sety(t.ycor() + 20); check_interaction()
def down(): t.sety(t.ycor() - 20); check_interaction()
def left(): t.setx(t.xcor() - 20); check_interaction()
def right(): t.setx(t.xcor() + 20); check_interaction()

screen.listen()
enable_keys()
draw_map()
t.mainloop()
