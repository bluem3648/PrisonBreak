HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

ANSWER = "sangmyung"

def play(word=None):
    print("\n=== 행맨 ===")
    answer = word if word else ANSWER
    guessed = set()
    lives = 6

    while True:
        print(HANGMAN[6 - lives])
        display = " ".join(c if c in guessed else "_" for c in answer)
        print(f"단어: {display}")
        print(f"남은 목숨: {lives}  |  맞춘 글자: {', '.join(sorted(guessed)) or '없음'}")

        if all(c in guessed for c in answer):
            print(f"\n정답입니다! 정답은 '{answer}' 였습니다!")
            return "승리"

        guess = input("\n글자를 입력하세요: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 입력하세요.")
            continue

        if guess in guessed:
            print(f"'{guess}'는 이미 입력했습니다.")
            continue

        guessed.add(guess)

        if guess in answer:
            print(f"'{guess}' 정답!")
        else:
            lives -= 1
            print(f"'{guess}' 틀렸습니다!")
            if lives == 0:
                print(HANGMAN[6])
                print(f"\n게임 오버! 정답은 '{answer}' 였습니다.")
                return "패배"
