from collections import deque


def check_left_side_is_smaller(left_sublist, right_sublist):
    left_avg = sum(left_sublist) / len(left_sublist)
    right_avg = sum(right_sublist) / len(right_sublist)
    return left_avg < right_avg


def check_right_side_is_smaller(central_value, right_sublist):
    right_avg = sum(right_sublist) / len(right_sublist)
    return right_avg < central_value


def find_strongest_eggs(*args):
    initial_deque = deque(args[0])
    sl_count = args[1]
    dict_results = dict()
    # Create dict keys
    for i in range(sl_count):
        dict_results[i] = []
    # Fill up the sublist
    while len(initial_deque) > 0:
        for j in range(sl_count):
            if len(initial_deque) == 0:
                break
            dict_results[j].append(initial_deque.popleft())
    winners = []
    # Validate sub lists
    for k in range(sl_count):
        current_sl = dict_results[k]
        mid_index = int(len(current_sl) / 2)
        left_sublist, right_sublist = current_sl[:mid_index], current_sl[mid_index + 1:]
        left_side_is_smaller_than_right_side = check_left_side_is_smaller(left_sublist, right_sublist)
        right_side_is_smaller_than_center_value = check_right_side_is_smaller(current_sl[mid_index], right_sublist)
        if left_side_is_smaller_than_right_side and right_side_is_smaller_than_center_value:
            winners.append(current_sl[mid_index])
    return winners


test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
