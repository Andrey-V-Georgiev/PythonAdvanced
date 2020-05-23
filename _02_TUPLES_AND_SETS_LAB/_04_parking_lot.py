first_row = input()
is_digit = first_row.isdigit()
if is_digit:
    rows_count = int(first_row)
    registrations = set()
    for _ in range(rows_count):
        row = input()
        command, reg = row.split(', ')
        if command == 'IN':
            registrations.add(reg)
        elif command == 'OUT':
            registrations.discard(reg)

    print('Parking Lot is Empty') if len(registrations) == 0 else [print(r) for r in registrations]
else:
    registrations = set()
    if first_row == "END":
        print('Parking Lot is Empty') if len(registrations) == 0 else [print(r) for r in registrations]
    else:
        command, reg = first_row.split(', ')
        if command == 'IN':
            registrations.add(reg)
        elif command == 'OUT':
            registrations.discard(reg)
        while True:
            row = input()
            if row == "END":
                print('Parking Lot is Empty') if len(registrations) == 0 else [print(r) for r in registrations]
                break
            else:
                command, reg = row.split(', ')
                if command == 'IN':
                    registrations.add(reg)
                elif command == 'OUT':
                    registrations.discard(reg)
