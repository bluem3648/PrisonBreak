import hangman

while True:
    result = hangman.play()
    print(f"결과: {result}")

    again = input("\n다시 하시겠습니까? (y/n): ").strip().lower()
    if again != "y":
        print("게임 종료!")
        break
