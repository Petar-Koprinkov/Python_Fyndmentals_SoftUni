deck_of_cards = input().split()
count_of_shuffle = int(input())

for shuffle in range(count_of_shuffle):
    final_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]

    for cards in range(len(left_part)):
        final_deck.append(left_part[cards])
        final_deck.append(right_part[cards])

    deck_of_cards = final_deck

print(final_deck)
