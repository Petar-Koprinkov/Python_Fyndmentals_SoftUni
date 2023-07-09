def check_ticket(current_ticket):
    if len(current_ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    first_half = current_ticket[0:10]
    second_half = current_ticket[10:]

    for symbols in winning_symbols:
        for matching_symbols in range(10, 5, -1):
            repetition = symbols * matching_symbols
            if repetition in first_half and repetition in second_half:
                if len(repetition) == 10:
                    return f'ticket "{current_ticket}" - {matching_symbols}{symbols} Jackpot!'
                return f'ticket "{current_ticket}" - {matching_symbols}{symbols}'
    return f'ticket "{current_ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    print(check_ticket(ticket))



