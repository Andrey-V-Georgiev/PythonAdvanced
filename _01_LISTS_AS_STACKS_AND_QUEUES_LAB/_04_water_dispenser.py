from collections import deque

water_reserve = int(input())
names = deque()
while True:
    name = input()
    if name == "Start":
        while True:
            input_row = input()
            if input_row.startswith("refill"):
                # add litters to water_reserve
                water_reserve += int(input_row.split(" ")[1])
            elif input_row == "End":
                break
            else:
                asked_liters = int(input_row)
                # check for availability
                if asked_liters <= water_reserve:
                    water_reserve -= asked_liters
                    print(f"{names.popleft()} got water")
                else:
                    print(f"{names.popleft()} must wait")
        # print how much liters of water left
        print(f"{water_reserve} liters left")
        break
    else:
        names.append(name)


