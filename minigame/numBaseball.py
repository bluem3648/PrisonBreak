import random

#정답 생성
def get_answer():
    digits = list(range(1, 10))
    random.shuffle(digits)
    return digits[:3]

#판단
def judge(answer, guess):
    strikes = sum(a==g for a, g in zip(answer, guess))
    balls = sum(g in answer for g in guess) - strikes
    return strikes, balls

#숫자 야구
def play():
    print("\n=== 숫자 야구 ===")
    answer = get_answer()
    attempts = 0

    while True:
        guess_input = input("세 자리 숫자를 입력하세요 (1-9, 중복 없음): ")
        if len(guess_input) != 3 or not guess_input.isdigit():
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue
        
        guess = [int(d) for d in guess_input]
        #중복 검사 및 범위 검사
        if len(set(guess)) != 3 or any(d < 1 or d > 9 for d in guess):
            print("숫자는 1-9 사이의 중복 없는 세 자리여야 합니다. 다시 시도하세요.")
            continue
        
        attempts += 1
        strikes, balls = judge(answer, guess)
        
        print(f"{strikes} 스트라이크, {balls} 볼")
        
        if strikes == 3:
            print(f"축하합니다! {attempts}번 만에 맞추셨습니다!")
            break