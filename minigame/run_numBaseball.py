import numBaseball

games = 0
total_attempts = 0

while True:
    numBaseball.play()
    games += 1

    again = input("\n다시 하시겠습니까? (y/n): ").strip().lower()
    if again != "y":
        print(f"\n총 {games}판 플레이했습니다. 수고하셨습니다!")
        break
