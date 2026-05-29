# -*- coding: utf-8 -*-
import sys
import os
import time
import builtins
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "minigame"))

from clear import clear
from title import show_title
import turtle as t
import blackJack
import rsp
import hangman
import numBaseball

current_stage = 1
is_loading = False
is_interacting = False

has_desk_ch1 = has_bed_ch1 = has_closet_ch1 = has_drawer_ch1 = False
has_bed_ch2 = has_desk_ch2 = has_drawer_ch2 = has_game_ch2 = False
has_desk_ch3 = has_rope_ch3 = has_recorder_ch3 = has_paper_ch3 = False
has_file_ch4 = has_shovel_ch4 = has_cloth_ch4 = has_blackjack_ch4 = False
has_id_ch4 = False

COORD_DOOR = (0, 150)
COORD_TABLE = (0, 60)
COORD_A = (150, 150)
COORD_B = (-150, -150)
COORD_C = (150, -150)
COORD_D = (-150, 150)

screen = None

TEXT_SPEED = 0.025

def print(*args, **kwargs):
    text = " ".join(str(arg) for arg in args)
    end = kwargs.get("end", "\n")
    flush = kwargs.get("flush", True)

    for char in text:
        builtins.print(char, end="", flush=True)
        time.sleep(TEXT_SPEED)

    builtins.print(end=end, flush=flush)


def reset_game():
    global current_stage
    global has_desk_ch1, has_bed_ch1, has_closet_ch1, has_drawer_ch1
    global has_bed_ch2, has_desk_ch2, has_drawer_ch2, has_game_ch2
    global has_desk_ch3, has_rope_ch3, has_recorder_ch3, has_paper_ch3
    global has_file_ch4, has_shovel_ch4, has_cloth_ch4, has_blackjack_ch4, has_id_ch4

    current_stage = 1

    has_desk_ch1 = has_bed_ch1 = has_closet_ch1 = has_drawer_ch1 = False
    has_bed_ch2 = has_desk_ch2 = has_drawer_ch2 = has_game_ch2 = False
    has_desk_ch3 = has_rope_ch3 = has_recorder_ch3 = has_paper_ch3 = False
    has_file_ch4 = has_shovel_ch4 = has_cloth_ch4 = has_blackjack_ch4 = False
    has_id_ch4 = False

    draw_map()


def draw_map():
    global is_loading

    clear()
    is_loading = True

    t.hideturtle()
    t.clear()
    t.penup()
    screen.bgcolor("#222222")

    t.goto(COORD_DOOR)
    t.dot(40, "red")
    t.write(" [Door]", align="center")

    if current_stage == 4:
        t.goto(COORD_TABLE)
        t.dot(40, "orange")
        t.write(" [Table]", align="center")

    t.goto(COORD_A)
    t.dot(40, "#8B4513")
    t.write(" [A]", align="center")

    t.goto(COORD_B)
    t.dot(40, "#4682B4")
    t.write(" [B]", align="center")

    t.goto(COORD_C)
    t.dot(40, "#8A2BE2")
    t.write(" [C]", align="center")

    t.goto(COORD_D)
    t.dot(40, "#2E8B57")
    t.write(" [D]", align="center")

    t.goto(0, 0)
    t.showturtle()

    print("\n--- STAGE {0} START ---".format(current_stage))

    if current_stage == 1:
        print("눈을 떴을 때, 가장 먼저 느껴진 건 차가운 바닥의 감촉이었다.")
        print("나는 한 손으로 머리를 감싸 쥔 채 천천히 몸을 일으켰다.")
        print("머릿속은 물에 젖은 종이처럼 흐릿했고, 목 안쪽에는 오래된 먼지 맛이 남아 있었다.")
        print("주위를 둘러보니 낯선 방 안이었다.")
        print("낡은 문, 책상, 침대, 옷장, 그리고 서랍 하나.")
        print("이곳에 들어온 기억도, 나가야 하는 이유도 떠오르지 않았다.")
        print("그런데 이상하게도, 이 방의 공기는 나를 알고 있는 것 같았다.")
        print("\n[Door] 문 / [A] 책상 / [B] 침대 / [C] 옷장 / [D] 서랍")

    elif current_stage == 2:
        print("문을 열고 나갔다고 생각했다.")
        print("하지만 잠깐의 암전 후 눈앞에 나타난 것은, 조금 전과 같은 방이었다.")
        print("완전히 같은 방은 아니었다.")
        print("책상 위에는 카드와 칩이 흩어져 있었고, 바닥에는 오래된 담배 냄새와 축축한 먼지가 뒤섞여 있었다.")
        print("공기 속에는 낡은 도박장의 냄새가 아직 빠져나가지 못한 채 가라앉아 있었다.")
        print("그 냄새를 맡는 순간, 이유를 알 수 없는 불안이 천천히 목을 조여 왔다.")
        print("나는 이 방을 처음 보는 것이 아닐지도 모른다.")
        print("아니, 외려 누군가를 찾기 위해 이런 곳을 오래 헤맨 적이 있는 것 같았다.")
        print("\n[Door] 문 / [A] 책상 / [B] 침대 / [C] 서랍 / [D] 방 구석")

    elif current_stage == 3:
        print("이번에는 눈을 뜨자마자 알 수 있었다.")
        print("이 방은 더 이상 평범한 방이 아니었다.")
        print("축축한 흙냄새가 났고, 벽과 문에는 긁힌 자국이 남아 있었다.")
        print("낡은 나무판 사이로 찬 공기가 새어 들어왔다.")
        print("어딘가의 산속 폐가.")
        print("그 단어가 떠오르는 순간, 등 뒤로 이유를 알 수 없는 불쾌감이 번졌다.")
        print("나는 이곳에 온 적이 있다.")
        print("그리고 아마, 혼자가 아니었다.")
        print("\n[Door] 문 / [A] 책상 / [B] 바닥 구석 / [C] 낡은 선반 / [D] 벽")

    elif current_stage == 4:
        print("마지막 방은 폐가와 감옥이 뒤섞인 모습이었다.")
        print("벽에는 산속의 습기가 배어 있었고, 바닥에는 차가운 콘크리트 냄새가 깔려 있었다.")
        print("나는 이곳이 단순한 방이 아니라는 것을 이제는 알고 있었다.")
        print("내가 끝까지 밀어낸 무언가가, 이 방의 형태를 하고 날 기다리고 있었다.")
        print("문 앞에는 낡은 카드 테이블이 놓여 있었다.")
        print("그 위에 놓인 카드들은 마치 나를 기다리고 있었던 것처럼 조용히 펼쳐져 있었다.")
        print("이번 판이 끝나면, 더는 모른 척할 수 없을 것 같았다.")
        print("\n[Door] 문 / [Table] 카드 테이블 / [A] 책상 위 파일 / [B] 흙 묻은 바닥 / [C] 구석의 천더미 / [D] 바닥 구석")

    is_loading = False


def disable_keys():
    screen.onkey(None, "w")
    screen.onkey(None, "s")
    screen.onkey(None, "a")
    screen.onkey(None, "d")


def enable_keys():
    screen.onkey(up, "w")
    screen.onkey(down, "s")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    screen.listen()


def show_final_memory():
    print("\n마지막 기억이 열리기 시작했다.")
    print("\n나는 그 남자를 사기꾼이라고 믿었다.")
    print("당첨 복권을 빼앗고, 모든 것을 망가뜨린 사람이라고.")
    print("\n그는 도박장 주변을 맴돌고 있었다.")
    print("누군가와 신호를 주고받는 것처럼 보였고,")
    print("나는 그것을 조직과 연결된 증거라고 믿었다.")
    print("\n그를 산속 폐가로 데려갈 이유는 그것으로 충분했다.")
    print("나는 감히 확신했다.")
    print("그를 묶고, 가두고, 그가 아니라고 말하는 목소리를 끝까지 듣지 않을 정도로.")
    print("\n그러나 짜증이 날 정도로 그 남자는, 도무지 내가 옳다는 것을 순순히 인정해주지 않았다.")
    print("그는 처음부터 계속해서 말했다.")
    print("나는 사기꾼이 아니라고.")
    print("\n' 경찰 ' 이라고.\n")
    print("누군가를 잡기 위해 그곳에 있었다고.")
    print("\n하지만 그때의 나는, 그 말이 변명으로밖에 들리지 않았다.")
    print("그가 사실을 말할수록, 나는 더 세게 묶었다.")
    print("그가 부정할수록, 나는 그를 더 확실한 범인으로 만들었다.")
    print("\n내가 생필품을 구하러 폐가를 비운 사이, 그는 탈출을 시도했다.")
    print("돌아온 나는 그를 막으려 했고, 우리는 몸싸움을 벌였다.")
    print("\n몸싸움이라고 부르기에도 우스울 정도로 짧은 순간이었지만.")
    print("그가 내 아래에서 버티려 할수록 나는 더 세게 밀어붙였던 것이 기억난다.")
    print("\n더 세게,")
    print("더 세게,")
    print("더.")
    print("더.")
    print("더!")
    print("\n그리고 이후에 일어난 일은....")
    print("... ....")
    print("...")
    print("\n...고민 끝에 나는 아무것도 신고하지 않았다.")
    print("처음에는 죽일 생각은 없었지만, 일이 이렇게 된 이상 어쩔 수 없었다.")
    print("나는 삽으로 땅을 파서, 흰 천에 감싼 시신을 묻었다.")
    print("\n흙으로 덮으면 모든 것이 끝날 거라고 생각했다.")
    print("이만하면 호화로운 장례를 치뤄주는 거라고 여기면서....")
    print("\n하지만 이 얼마나 우스운 착각이었던가.")
    print("얼마 지나지 않아 폭우가 산을 무너뜨리면서, 곧 숨겨둔 것이 표면 위로 드러났다.")
    print("\n내가 아주 긴 시간을 외면했던 진실과 함께.")
    print("\n그래.")
    print("그는 사기꾼이 아니었다.")
    print("\n...")
    print("실종된 잠복 경찰이었다.")
    print("\n피해자 신분: 잠복 경찰")


def show_ending_choice():
    global current_stage

    print("\n문 아래에 빈칸이 있는 문장이 떠올랐다.")
    print("그는 사기꾼이 아니라 ____이었다.")

    answer = input("정답: ").replace(" ", "")

    if answer == "잠복경찰" or answer == "경찰":
        print("\n그는 사기꾼이 아니라 잠복 경찰이었다.")
        print("\n가려져 있던 기록들이 하나씩 맞춰지기 시작했다.")
        print("내가 사기꾼이라 믿었던 남자는, 처음부터 내가 찾던 범인이 아니었다.")
        print("나는 복수를 하고 있다고 믿었다.")
        print("동생의 죽음도, 가족에게 남은 빚도, 무너진 모든 시간도 누군가에게 갚게 해야 한다고 믿었다.")
        print("하지만 내가 한 일은 진실을 확인하는 과정이 아니라,")
        print("한 사람을 끝까지 몰아붙인 분풀이일 뿐이었다.")
        print("\n문이 열렸다.")
        print("\n이번에는 바깥으로 나가는 문이 아니라, 내가 외면해 온 현실로 돌아가는 문이었다.")

        print("\n1. 진실을 받아들인다.")
        print("2. 기억을 지우고 처음으로 돌아간다.")
        print("3. 끝까지 그를 사기꾼이라고 주장한다.")

        choice = input("선택: ")

        if choice == "1":
            print("\n[엔딩: 진실 수용]")
            print("나는 한동안 아무 말도 하지 못했다.")
            print("흩어져 있던 기억들이 천천히 하나의 사건으로 이어졌다.")
            print("복권, 빚, 동생의 죽음, 의심, 납치, 감금, 몸싸움, 그리고 죽음.")
            print("그 모든 것은 누군가가 꾸며낸 거짓이 아니라, 내가 외면해 온 현실이었다.")
            print("\n나는 복수를 원한다고 믿었다.")
            print("빼앗긴 것을 되찾기 위한 일이라고 믿었다.")
            print("무너진 가족을 대신해, 죽은 사람을 대신해, 누군가에게 벌을 주는 일이라고 믿었다.")
            print("하지만 그 믿음은 진실을 확인하기 위한 것이 아니었다.")
            print("내가 무너지지 않기 위해 붙잡은 핑계에 가까웠다.")
            print("\n그 결과 한 사람은 돌아올 수 없는 곳으로 밀려났다.")
            print("그리고 나는 그 사실을, 이제야 내 이름으로 받아들였다.")
            print("\n[시스템: 피험자가 사건의 주요 기억을 인식했습니다.]")
            print("[시스템: 책임 인식 반응을 확인했습니다.]")
            print("[시스템: 현실 복귀 절차를 시작합니다.]")
            print("\n차가운 감옥의 공기가 폐 안으로 들어왔다.")
            print("나는 천천히 눈을 떴다.")
            print("희미한 형광등 불빛, 회색 벽, 손목에 남은 구속구의 자국.")
            print("더 이상 방은 바뀌지 않았다.")
            print("더 이상 문도 숨겨져 있지 않았다.")
            print("\n나는 고개를 숙였다.")
            print("도망칠 곳은 없었다.")
            print("하지만 적어도 이제는, 무엇으로부터 도망치고 있었는지 알고 있었다.")

        elif choice == "2":
            print("\n[엔딩: 반복]")
            print("나는 고개를 저었다.")
            print("눈앞에 놓인 진실은 받아들이기엔 너무 무거웠다.")
            print("그가 잠복 경찰이었다는 사실도,")
            print("그를 죽게 만든 사람이 나였다는 사실도,")
            print("내 손으로 땅을 팠다는 기억도.")
            print("\n차라리 모르는 편이 나았다.")
            print("차라리 처음부터 아무것도 기억하지 못하는 편이 나았다.")
            print("복권도, 동생의 마지막 말도,")
            print("내가 사기꾼이라고 불렀던 얼굴도,")
            print("전부 모르는 편이 나았다.")
            print("\n나는 마지막 문장을 읽지 않은 사람처럼 눈을 감았다.")
            print("\n[시스템: 피험자가 현실 인식을 보류했습니다.]")
            print("[시스템: 기억 초기화를 시작합니다.]")
            print("\n시야가 하얗게 번지고, 방 안의 소리들이 멀어졌다.")
            print("카드가 섞이는 소리, 삽이 흙을 파는 소리, 누군가 살려 달라고 말하던 목소리.")
            print("모든 것이 멀어졌다.")
            print("\n잠시 후, 나는 다시 차가운 바닥 위에서 눈을 떴다.")
            print("낯선 방이었다.")
            print("나는 내가 왜 이곳에 있는지 기억하지 못했다.")

            reset_game()

        elif choice == "3":
            print("\n[엔딩: 부정]")
            print("나는 끝까지 고개를 저었다.")
            print("기록도, 목소리도, 되살아난 기억도 받아들이지 않았다.")
            print("그는 여전히 사기꾼이어야 했다.")
            print("그래야 내가 한 일에도 이유가 생겼다.")
            print("그래야 내가 무너뜨린 것이 사람이 아니라, 벌을 받아 마땅한 무언가였다고 믿을 수 있었다.")
            print("\n나는 같은 말을 몇 번이고 되풀이했다.")
            print("그는 사기꾼이었다.")
            print("나는 속았을 뿐이다.")
            print("나는 되찾으려 했을 뿐이다.")
            print("내 동생이 죽었고, 우리 가족이 무너졌고, 누군가는 대가를 치러야 했다.")
            print("그러니 그는 사기꾼이어야 했다.")
            print("\n[시스템: 피험자가 현실 인식을 거부했습니다.]")
            print("[시스템: 방어 반응이 지속됩니다.]")
            print("[시스템: 교화 단계를 강화합니다.]")
            print("\n방 안의 불빛이 하나둘 꺼졌다.")
            print("어둠 속에서 카드 테이블만이 희미하게 반짝였다.")
            print("다시 판이 시작될 것이다.")
            print("이번에는 더 깊은 곳에서.")
            print("내가 끝내 인정하지 않은 기억들이, 더 어두운 형태로 나를 기다리고 있었다.")

        else:
            print("잘못된 선택이다.")
            print("나는 아직 어떤 결말도 고르지 못하고 있다.")

    else:
        print("아직 진실을 제대로 마주하지 못했다.")


def check_interaction():
    global is_interacting, current_stage, has_blackjack_ch4
    global has_desk_ch1, has_bed_ch1, has_closet_ch1, has_drawer_ch1
    global has_bed_ch2, has_desk_ch2, has_drawer_ch2, has_game_ch2
    global has_desk_ch3, has_rope_ch3, has_recorder_ch3, has_paper_ch3
    global has_file_ch4, has_shovel_ch4, has_cloth_ch4, has_id_ch4

    if is_loading or is_interacting:
        return

    is_interacting = True

    try:
        if t.distance(COORD_DOOR) < 40:
            t.backward(40)
            disable_keys()

            if current_stage == 4:
                print("\n문 아래에 빈칸이 있는 문장이 떠 있었다.")
                print("그는 사기꾼이 아니라 ____이었다.")

                if has_blackjack_ch4:
                    show_ending_choice()
                else:
                    print("\n하지만 아직 빈칸을 채울 수 없었다.")
                    print("방 안 어딘가에 마지막 기억을 여는 장치가 남아 있는 것 같다.")

            else:
                target_pwd = None

                if current_stage == 1:
                    print("\n문에는 네 자리 비밀번호 장치가 달려 있었다.")
                    print("장치 옆에는 작은 글씨가 새겨져 있었다.")
                    print("\n'기억은 순서대로 돌아온다.'")
                    print("'처음 본 숫자부터 마지막에 얻은 숫자까지.'\n")

                    if has_desk_ch1 and has_bed_ch1 and has_closet_ch1 and has_drawer_ch1:
                        target_pwd = "7294"

                elif current_stage == 2:
                    print("\n문에는 세 개의 단어를 입력하는 장치가 붙어 있었다.")
                    print("입력창 위에는 흐릿한 문장이 떠 있었다.")
                    print("\n'그날 빼앗긴 순서대로 빈틈없이 입력하라.'\n")

                    if has_desk_ch2 and has_bed_ch2 and has_drawer_ch2 and has_game_ch2:
                        target_pwd = "복권담보사기꾼"

                elif current_stage == 3:
                    print("\n문에는 빈칸이 있는 문장이 떠 있었다.")
                    print("나는 그를 ____했다.")
                    print("문 옆에는 작은 글씨가 적혀 있었다.")
                    print("\n'네가 한 행동의 이름을 입력하라.'\n")

                    if has_desk_ch3 and has_rope_ch3 and has_recorder_ch3 and has_paper_ch3:
                        target_pwd = "납치"

                if target_pwd:
                    pwd = input("Password: ")
                    clean_pwd = pwd.replace(" ", "").replace(",", "").replace("/", "")

                    if clean_pwd == target_pwd:
                        if current_stage == 1:
                            print("\n자물쇠 안쪽에서 둔탁한 소리가 났다.")
                            print("문은 열렸지만, 이상하게도 안도감은 들지 않았다.")
                            print("복권, 빚, 그리고 누군가의 사과.")
                            print("그 조각들은 아직 사건이 아니라 감정에 가까웠다.")
                            print("나는 숨을 삼키고, 어둠 너머로 한 걸음을 내디뎠다.")
                            print("\n[시스템: 1단계 반응 확인.]")
                            print("[시스템: 상실 관련 기억 조각이 활성화되었습니다.]")

                        elif current_stage == 2:
                            print("\n문 너머에서 카드가 섞이는 듯한 소리가 들렸다.")
                            print("\n복권, 담보, 사기꾼.")
                            print("세 단어가 하나로 이어지는 순간, 가슴 안쪽이 불쾌하게 내려앉았다.")
                            print("\n불현듯 잊고 있던 과거가 하나둘씩 머릿속에 떠올랐다.")
                            print("\n빚더미에 내려앉은 집, 매주 사 모으던 복권, 서로에게 상처만 남기던 가족들.")
                            print("\n그래, 그 복권.")
                            print("\n어떻게 지금까지 잊고 있었을까.")
                            print("내 인생을 망쳤던 바로 그 사건을.")
                            print("\n그 복권은 단순한 종이 한 장이 아니었다.")
                            print("빚을 갚고, 무너진 우리 집을 다시 세울 수 있을지도 모른다는 마지막 기대였다.")
                            print("\n그러나 어느 날, 그 기대를 들고 도박장에 간 사람에 의해 내 꿈은 산산이 부서졌다.")
                            print("\n형, 미안해.")
                            print("그 문장이 뒤늦게 귓속에서 되살아났다.")
                            print("\n메모 뒷면의 날짜가 다시 떠올랐다.")
                            print("그날 이후로 내 동생은 더 이상 변명도, 사과도 하지 못하고 영원한 침묵 속으로 빠져들었다.")
                            print("\n혼자 남은 내게 막대한 빚만을 떠넘긴 채로.")
                            print("\n[시스템: 기억 복구 2단계.]")
                            print("[시스템: 빼앗긴 마지막 기회를 확인했습니다.]")

                        elif current_stage == 3:
                            print("\n납치.")
                            print("그 단어를 떠올리자 문 너머에서 낮은 바람 소리가 들렸다.")
                            print("나는 사기꾼을 쫓고 있었다고 믿었다.")
                            print("하지만 이 방에 남은 흔적들은, 내가 누군가를 쫓은 것이 아니라 이곳으로 데려왔다는 사실만을 가리키고 있었다.")
                            print("\n그는 도박장 주변을 맴돌고 있었다.")
                            print("누군가와 신호를 주고받는 것처럼 보였고, 나는 그것을 증거라고 믿었다.")
                            print("지금 생각하면, 그 장면에는 다른 해석도 있었을지 모른다.")
                            print("하지만 그때의 나는 내가 보고 싶은 방식으로만 그를 보았다.")
                            print("\n나는 문고리를 잡았다.")
                            print("손바닥 안쪽에 밧줄의 거친 감촉이 되살아났다.")
                            print("\n[시스템: 기억 복구 3단계.]")
                            print("[시스템: 납치 및 감금 사실을 확인했습니다.]")

                        input("\npress any key to next stage")
                        current_stage += 1
                        draw_map()
                    else:
                        if current_stage == 1:
                            print("아니다.")
                            print("숫자는 맞는 것 같은데, 순서가 어딘가 어긋나 있다.")
                        elif current_stage == 2:
                            print("아니다.")
                            print("그날의 순서는 아직 제대로 맞춰지지 않았다.")
                        elif current_stage == 3:
                            print("아니다.")
                            print("입 밖으로 꺼내기에는 아직 너무 이른 단어인 것 같다.")
                else:
                    if current_stage == 1:
                        print("문고리를 잡았지만, 손끝에 아무런 확신도 걸리지 않았다.")
                        print("아직 이 방이 내게 보여주려는 것을 다 보지 못했다.")
                    elif current_stage == 2:
                        print("문 앞에 섰지만, 머릿속의 순서가 아직 이어지지 않았다.")
                        print("그날의 판이 어떻게 시작됐는지 더 확인해야 한다.")
                    elif current_stage == 3:
                        print("문은 열리지 않았다.")
                        print("이 방에는 아직 내가 외면하고 있는 단어가 남아 있다.")

            enable_keys()

        elif current_stage == 4 and t.distance(COORD_TABLE) < 40:
            t.backward(40)
            disable_keys()

            if has_blackjack_ch4:
                print("\n카드 테이블 위에는 이미 끝난 판의 흔적만 남아 있었다.")
                print("이제 문 아래의 빈칸을 채워야 할 것 같다.")
            else:
                print("\n문 앞의 카드 테이블을 조사했다.")
                print("낡은 카드들이 테이블 위에 가지런히 놓여 있었다.")
                print("마지막 판을 시작하라는 듯, 카드 한 장이 내 쪽으로 밀려 나왔다.")
                print("이번에는 돈을 따기 위한 판이 아니었다.")
                print("나는 본능적으로 그 사실을 눈치챌 수 있었다.")
                print("\n누가, 도대체 무슨 이유로 내게 이런 악질적인 게임을 시키는 걸까.")
                print("\n손끝에 남은 떨림을 숨기지 못한 채, 나는 천천히 카드를 집어 들었다.")

                result = blackJack.play()

                if result == "승리":
                    has_blackjack_ch4 = True
                    show_final_memory()
                else:
                    print("카드는 내 손 안에서 무겁게 식어 갔다.")
                    print("아직 마지막 기억을 확인할 수 없다.")
                    print("다시 시도해야 할 것 같다.")

            enable_keys()

        elif current_stage == 1:
            if t.distance(COORD_A) < 40 and not has_desk_ch1:
                t.backward(40)
                has_desk_ch1 = True
                print("\n책상 위에 구겨진 빚 독촉장이 놓여 있었다.")
                print("종이는 여러 번 접혔다 펴진 듯 주름져 있었고, 붉은 글씨만 유난히 선명했다.")
                print("\n'7일 안에 갚을 것.'\n")
                print("그 아래에는 알아보기 힘들 만큼 번진 이름들과 금액이 빼곡하게 적혀 있었다.")
                print("왜인지 보기만 해도 가슴 안쪽이 조이는 듯한 기분이 들었다.")

            elif t.distance(COORD_B) < 40 and not has_bed_ch1:
                t.backward(40)
                has_bed_ch1 = True
                print("\n침대 밑에서 낡은 메모를 발견했다.")
                print("먼지를 털어내자 떨리는 글씨가 드러났다.")
                print("\n'형, 미안해.'")
                print("'이번 판만 이기면 다 돌려놓을 수 있을 줄 알았어.'\n")
                print("메모 아래에는 '2번째 기회'라는 말이 작게 남아 있었다.")
                print("나는 그 문장을 읽고도 한동안 메모에서 손을 떼지 못했다.")

            elif t.distance(COORD_C) < 40 and not has_closet_ch1:
                t.backward(40)
                has_closet_ch1 = True
                print("\n옷장 안쪽에서 찢어진 복권 조각을 발견했다.")
                print("복권의 대부분이 찢겨 나갔지만, 첫 숫자 하나는 겨우 읽어낼 수 있었다.")
                print("9.")
                print("그 숫자 9가 이상하게도 시야에서 떨어지질 않았다.")

            elif t.distance(COORD_D) < 40 and not has_drawer_ch1:
                t.backward(40)
                disable_keys()

                print("\n서랍 손잡이 옆에는 오래된 숫자 입력 장치가 붙어 있었다.")
                print("낡은 화면에는 세 칸의 빈 숫자가 떠 있었고, 아래에는 짧은 문장이 깜빡이고 있었다.")
                print("\n'맞는 숫자는 반응한다.'\n")
                print("평범한 자물쇠라기보다는, 오래된 숫자 맞추기 게임처럼 보였다.")
                print("나는 마른 입술을 한번 깨물고, 천천히 숫자를 입력했다.")
                print("\n숫자 세 개를 맞혀야 한다.")
                print("숫자가 맞으면 장치가 반응하고,")
                print("자리까지 맞으면 더 선명한 신호가 돌아오는 것 같다.")
                print("\n서랍을 열려면 이 게임을 끝내야 한다.")

                result = numBaseball.play()

                if result == "승리" or result is True or result is None:
                    has_drawer_ch1 = True
                    print("\n마지막 숫자를 입력하는 순간, 세 칸의 불빛이 동시에 켜졌다.")
                    print("장치 안쪽에서 짧은 기계음이 울렸다.")
                    print("곧이어 서랍 속 걸쇠가 풀리는 소리가 났다.")
                    print("\n안에는 접힌 종이 한 장이 들어 있었다.")
                    print("펼쳐 보니 복권 번호의 일부가 적혀 있었다.")
                    print("마지막 숫자는 4로 보였다.")
                    print("이제 흩어진 숫자들이 하나의 순서로 맞물리기 시작했다.")
                else:
                    print("\n숫자를 입력하자 장치가 짧게 떨렸다.")
                    print("몇 개의 불빛이 희미하게 들어왔다가 사라졌다.")
                    print("완전히 틀린 것은 아닌 것 같다.")
                    print("하지만 아직 서랍은 열리지 않았다.")

                enable_keys()

        elif current_stage == 2:
            if t.distance(COORD_A) < 40 and not has_desk_ch2:
                t.backward(40)
                has_desk_ch2 = True
                print("\n책상 위에는 낡은 카드와 칩이 흩어져 있었다.")
                print("칩 몇 개는 바닥에 떨어져 있었고, 그 아래에는 '담보'라고 적힌 빈 종이봉투가 끼워져 있었다.")
                print("봉투에는 집 주소처럼 보이는 글자와, 낯익은 이름의 일부가 적혀 있었다.")
                print("어째서인지 불쑥 불쾌감이 솟았다가 가라앉았다.")
                print("하지만 그 감정이 어디서 온 것인지는 아직 잡히지 않았다.")

            elif t.distance(COORD_B) < 40 and not has_bed_ch2:
                t.backward(40)
                has_bed_ch2 = True
                print("\n침대 밑에서 또 다른 복권 조각을 발견했다.")
                print("조각 뒷면에는 '처음 빼앗긴 것'이라는 글씨가 적혀 있었다.")
                print("복권.")
                print("그 얇은 종이 한 장을 보는 순간, 이상하게 숨이 막혔다.")
                print("왜 그토록 중요한 물건이었는지는 아직 떠오르지 않았다.")

            elif t.distance(COORD_C) < 40 and not has_drawer_ch2:
                t.backward(40)
                has_drawer_ch2 = True
                print("\n서랍 안에서 누군가의 메모를 발견했다.")
                print("\n'그 사람이 다 가져갔어.'")
                print("'처음부터 이길 수 없는 판이었어.'")
                print("'미안해. 용서해 달라는 말도 못 하겠다.'\n")
                print("메모의 뒷면에는 구겨진 병원 영수증 같은 종이가 붙어 있었다.")
                print("이름은 번져 알아볼 수 없었지만, 날짜만은 선명했다.")
                print("그 날짜를 보는 순간, 머릿속 어딘가가 짧게 흔들렸다.")
                print("하지만 더는 떠오르지 않았다.")
                print("\n짧은 문장들이었지만, 읽을수록 머릿속이 뜨거워졌다.")
                print("사기꾼.")
                print("그 단어 하나가 오래전부터 내 안에 박혀 있었던 것처럼 떠올랐다.")

            elif t.distance(COORD_D) < 40 and not has_game_ch2:
                t.backward(40)
                disable_keys()

                print("\n방 구석에 낡은 게임기가 놓여 있었다.")
                print("먼지가 두껍게 내려앉아 있었지만, 화면만은 희미하게 켜져 있었다.")
                print("\n'이기면 그날의 판을 보여주겠다.'\n")
                print("화면은 낡았고, 버튼은 끈적하게 닳아 있었다.")
                print("나는 망설이다가 손끝에 힘을 주고 버튼을 눌렀다.")

                result = rsp.play()

                if result == "승리" or result is True:
                    print("\n게임기 화면이 잠시 깜빡이더니, 흐린 글자들이 순서대로 떠올랐다.")
                    print("\n복권 > 담보 > 사기꾼")
                    print("\n순간, 내 머릿속에 연쇄적으로 짧은 이미지들이 연상됐다.")
                    print("\n부엌 테이블 위에서 사라지는 얇은 종이 한 장.")
                    print("검고 둥근 원탁 위로 우수수 쏟아지는 온갖 잡동사니들.")
                    print("그것을 보며 히죽 웃는 양의 탈을 쓴 누군가....")
                    print("\n하지만 전부 상상을 덧입힌 피상적인 이미지에 불과할 뿐.")
                    print("\n그나마 첫번째 이미지가 무언가 익숙하게 느껴졌으나, 아무리 노력해도 더 생각나는 것은 없었다.")
                    print("화면 속 단어들이 오래된 얼룩처럼 남아 조용히 날 기다려주었다.")
                    has_game_ch2 = True
                else:
                    print("화면은 다시 어둡게 가라앉았다.")
                    print("아직 그날의 순서를 확인할 수 없다.")

                enable_keys()

        elif current_stage == 3:
            if t.distance(COORD_A) < 40 and not has_desk_ch3:
                t.backward(40)
                has_desk_ch3 = True
                print("\n책상 위에서 내가 쓴 것으로 보이는 메모를 발견했다.")
                print("\n'그놈이 복권을 가져갔다.'")
                print("'그놈만 잡으면 전부 되돌릴 수 있다.'")
                print("'네가 죽었는데, 나는 아직도 아무것도 되찾지 못했다.'\n")
                print("글씨는 거칠었고, 문장마다 눌러쓴 자국이 깊게 남아 있었다.")
                print("나는 이 문장을 쓰는 동안 분노하고 있었던 것 같다.")
                print("아니, 분노하고 싶어 했던 것 같다.")
                print("무너진 것을 붙잡을 방법이 그것밖에 없다고 믿고 싶었던 것 같다.")

            elif t.distance(COORD_B) < 40 and not has_rope_ch3:
                t.backward(40)
                has_rope_ch3 = True
                print("\n바닥 구석에 낡은 밧줄이 떨어져 있었다.")
                print("밧줄 군데군데에는 긁힌 자국과 말라붙은 흙이 남아 있었다.")
                print("누군가를 묶었던 흔적처럼 보였다.")
                print("손끝이 차갑게 굳었다.")
                print("나는 이 밧줄의 감촉을 알고 있었다.")
                print("손가락의 마디마디를 거칠게 쓸고 지나갔던 그 감각을.")

            elif t.distance(COORD_C) < 40 and not has_recorder_ch3:
                t.backward(40)
                has_recorder_ch3 = True
                print("\n낡은 선반 위에 녹음기 하나가 놓여 있었다.")
                print("먼지를 뒤집어쓴 채였지만, 재생 버튼만은 유난히 닳아 있었다.")
                print("나는 잠시 망설이다가 버튼을 눌렀다.")
                print("\n녹음기에서 끊어진 목소리가 흘러나왔다.")
                print('\n"나는 사기꾼이 아니야."')
                print('"네가 찾는 사람은 내가 아니야."')
                print('"나는…… 찰…… 제발 풀어줘."\n')
                print("잡음이 심해 정확히 무슨 말인지는 알 수 없었다.")
                print("하지만 그 목소리는 쉽게 끊어지지 않았다.")
                print("테이프가 멈춘 뒤에도, 그 말은 계속 내 귀 안쪽에 남아 있었다.")
                print("그는 무언가를 설명하려 했고, 나는 그것을 듣지 않았던 것 같다.")

            elif t.distance(COORD_D) < 40 and not has_paper_ch3:
                t.backward(40)
                disable_keys()

                print("\n벽 한쪽에 누렇게 바랜 종이가 붙어 있었다.")
                print("가까이 다가가자, 종이 위의 문제가 또렷하게 보였다.")
                print("\nQ. 내가 되찾으려 했던 것은?")
                print("1. 복권")
                print("2. 반지")
                print("3. 사진")

                answer = input("정답: ")

                if answer == "1" or answer == "복권":
                    print("\n정답이었다.")
                    print("종이 뒤편에서 접혀 있던 또 다른 종이가 떨어졌다.")
                    print("그곳에는 빈칸이 여러 개 그어진 단어 퍼즐이 적혀 있었다.")
                    print("나는 그것을 보는 순간, 숨이 조금 막혔다.")

                    result = hangman.play("kidnap")

                    if result == "승리" or result is True:
                        print("\n단어가 완성되는 순간, 손끝이 저렸다.")
                        print("납치.")
                        print("나는 그 단어를 새로 읽은 것이 아니라, 이미 알고 있던 것을 떠올린 것 같았다.")
                        print("그제야 이 방의 공기가 왜 이렇게 무거웠는지 알 것 같았다.")
                        has_paper_ch3 = True
                    else:
                        print("단어는 아직 완성되지 않았다.")
                        print("하지만 빈칸 사이로 불길한 윤곽이 조금씩 드러나고 있었다.")
                else:
                    print("아니다.")
                    print("내가 붙잡고 있던 건 그런 것이 아니었다.")
                    print("나는 처음부터 그 종이 한 장에 매달려 있었다.")

                enable_keys()

        elif current_stage == 4:
            if t.distance(COORD_A) < 40 and not has_file_ch4:
                t.backward(40)
                has_file_ch4 = True
                print("\n책상 위에 오래된 기록 파일이 놓여 있었다.")
                print("표지는 오래되어 빛이 바랬지만, 안쪽의 문장들은 지나치게 또렷했다.")
                print("\n피해자 신분: □□□□")
                print("사건 장소: 산속 폐가")
                print("사건 내용: 납치, 감금, 사망, 시신 은폐")
                print("\n기록은 차갑고 건조했다.")
                print("그런데 이상하게도, 그 안의 내용은 낯설지 않았다.")
                print("마치 내가 이미 알고 있는 일을 남의 문장으로 다시 읽는 것 같았다.")

            elif t.distance(COORD_B) < 40 and not has_shovel_ch4:
                t.backward(40)
                has_shovel_ch4 = True
                print("\n흙이 말라붙은 바닥 위에 삽 하나가 놓여 있었다.")
                print("삽 끝에는 굳은 흙이 붙어 있었다.")
                print("손잡이 부분은 오래 쥔 흔적처럼 매끈하게 닳아 있었다.")
                print("나는 이것으로 땅을 팠던 것 같다.")
                print("그 생각이 떠오르자 속이 천천히 가라앉았다.")
                print("흙을 덮으면 끝날 거라고 믿었던 손의 무게가, 아직 손바닥 안쪽에 남아 있는 것 같았다.")

            elif t.distance(COORD_C) < 40 and not has_cloth_ch4:
                t.backward(40)
                has_cloth_ch4 = True
                print("\n구석에 아무렇게나 뭉쳐진 천더미가 있었다.")
                print("펼쳐 보니 천에는 흙과 마른 얼룩이 눌어붙어 있었다.")
                print("무언가를 감싸기 위해 급하게 사용한 것처럼 보였다.")
                print("나는 그것이 무엇이었는지 떠올리고 싶지 않았다.")
                print("하지만 기억은 이미 천천히 되돌아오고 있었다.")

            elif t.distance(COORD_D) < 40 and not has_id_ch4:
                t.backward(40)
                has_id_ch4 = True
                print("\n바닥 구석에서 찢어진 신분증 조각을 발견했다.")
                print("글자는 대부분 지워져 있었지만, '경...'이라는 글자와 일부 번호만 보였다.")
                print("녹음기에서 끊겨 들렸던 말이 다시 떠올랐다.")
                print('\n"나는…… 찰…… 제발 풀어줘."\n')
                print("나는 그가 끝까지 말하려 했던 것을 듣지 않았다.")
                print("아니, 들을 생각이 없었던 것 같다.")
                print("그 생각이 들자 신분증 조각이 손 안에서 유난히 차갑게 느껴졌다.")

    finally:
        is_interacting = False


def up():
    t.sety(t.ycor() + 20)
    check_interaction()


def down():
    t.sety(t.ycor() - 20)
    check_interaction()


def left():
    t.setx(t.xcor() - 20)
    check_interaction()


def right():
    t.setx(t.xcor() + 20)
    check_interaction()


show_title()

screen = t.Screen()
t.shape("turtle")
t.penup()
t.speed(0)

screen.listen()
enable_keys()
draw_map()
t.mainloop()
