vip_guests = set()
regular_guests = set()

guests_count = int(input())
for _ in range(guests_count):
    guest = input()
    is_digit = guest[0].isdigit()
    if is_digit:
        vip_guests.add(guest)
    else:
        regular_guests.add(guest)
while True:
    reservation = input()

    if reservation == 'END':
        unchecked_guests_count = len(vip_guests) + len(regular_guests)
        print(unchecked_guests_count)
        [print(g) for g in sorted(vip_guests)]
        [print(g) for g in sorted(regular_guests)]
        break
    else:
        is_digit = reservation[0].isdigit()
        if is_digit:
            vip_guests.discard(reservation)
        else:
            regular_guests.discard(reservation)
