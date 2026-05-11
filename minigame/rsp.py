import random
import time

#컴퓨터 선택
def get_computer_choice():
    return random.choice(["가위", "바위", "보"])

#판단
def judge(player, computer):
    if player == computer:
        return "무승부"
    wins = {"가위" : "보", "바위" : "가위", "보" : "바위"}
    if wins[player] == computer:
        return "승리"
    return "패배"

#가위 바위 보
def play():
    print("\n=== 가위 바위 보 ===")
    mapping = {"1": "가위", "2": "바위", "3": "보"}

    while True:
        print("\n1: 가위 2: 바위 3: 보")
        choice = input("선택: ")

        if choice not in mapping:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        player_choice = mapping[choice]
        computer_choice = get_computer_choice()
        result = judge(player_choice, computer_choice)

        print(f"플레이어: {player_choice}")
        print(f"컴퓨터: {computer_choice}")
        print(f"결과: {result}")
        time.sleep(3)

        if result == "승리":
            return result