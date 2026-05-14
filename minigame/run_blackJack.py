from blackJack import play

wins = losses = draws = 0

while True:
    result = play()

    if result == "승리":
        wins += 1
    elif result == "패배":
        losses += 1
    elif result == "무승부":
        draws += 1

    print(f"[전적] 승: {wins}  패: {losses}  무: {draws}")

    again = input("\n다시 하시겠습니까? (y/n): ").strip().lower()
    if again != "y":
        print("게임 종료!")
        break
