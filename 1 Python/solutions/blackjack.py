def handle_card(ordinal: str, hands: list) -> list:
    card = input(f'What is your {ordinal} card? ').lower()
    if card in ['j', 'q', 'k']:
        hands = list(map(lambda c: c + 10, hands))
    elif card == 'a':
        for i in range(len(hands)):
            val = hands[i]
            hands[i] += 1
            hands.append(val+11)
    else:
        try:
            if int(card) >= 2 and int(card) <= 10:
                hands = list(map(lambda c: c + int(card), hands))
            else:
                print('That is not a valid card, please try again')
                handle_card(ordinal, hands)
        except ValueError:
            print('That is not a valid card, please try again')
            handle_card(ordinal, hands)
    return hands


def advise(hands: list) -> tuple:
    if 21 in hands:
        return 'BLACKJACK!', 21
    elif min(hands) > 21:
        return 'BUSTED', min(hands)

    max_val = max(filter(lambda c: c < 21, hands))
    if max_val >= 17:
        return 'stay', max_val
    else:
        return 'hit', max_val


if __name__ == '__main__':
    first = handle_card('first', [0])
    second = handle_card('second', first)
    third = handle_card('third', second)
    advice = advise(third)
    print(f'With {advice[1]} points, {advice[0]}')
