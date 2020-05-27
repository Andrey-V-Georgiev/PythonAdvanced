def concatenate(*args):
    args_list = list(args)
    concatenated_args = ''.join(args_list)
    return concatenated_args


print(concatenate("Soft", "Uni", "Is", "Great", "!"))