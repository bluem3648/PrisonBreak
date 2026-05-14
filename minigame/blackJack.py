import random

def create_deck():
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck = ranks * 4
    random.shuffle(deck)
    return deck

def card_value(card):
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        return 11
    return int(card)

def hand_total(hand):
    total = sum(card_value(c) for c in hand)
    aces = hand.count("A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def show_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}: [?] {' '.join(hand[1:])}") #join : 리스트 원소들을 공백으로 이어붙임
    else:
        print(f"{name}: {' '.join(hand)} (합계: {hand_total(hand)})")

def play():
    print("\n=== 블랙잭 ===")
    deck = create_deck()

    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    show_hand("딜러", dealer, hide_first=True)
    show_hand("플레이어", player)

    while hand_total(player) < 21:
        action = input("\n1: Hit  2: Stand > ")
        if action == "1":
            player.append(deck.pop())
            show_hand("플레이어", player)
        elif action == "2":
            break

    player_total = hand_total(player)
    if player_total > 21:
        print("버스트! 패배")
        return "패배"

    print("\n--- 딜러 턴 ---")
    show_hand("딜러", dealer)
    while hand_total(dealer) <= 16:
        dealer.append(deck.pop())
        show_hand("딜러", dealer)

    dealer_total = hand_total(dealer)

    if dealer_total > 21 or player_total > dealer_total:
        print("승리!")
        return "승리"
    elif player_total == dealer_total:
        print("무승부")
        return "무승부"
    else:
        print("패배")
        return "패배"
