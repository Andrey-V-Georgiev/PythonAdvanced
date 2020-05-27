def get_info(**kwargs):
    kwargs_dict = dict(kwargs)
    name = kwargs_dict['name']
    town = kwargs_dict['town']
    age = int(kwargs_dict['age'])
    output_str = f'This is {name} from {town} and he is {age} years old'
    return output_str


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
