def process_query(query_string):
    if query_string == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif query_string == "asteroids":
        return "Unknown"
    elif "name" in query_string:
        return "Vadim_Mariia_Kevin_"
    elif "largest" in query_string:
        return process_max_number(query_string)
    elif "smallest" in query_string:
        return process_min_number(query_string)
    elif "multiplied" in query_string:
        return process_multiply(query_string)
    elif "plus" in query_string:
        return process_plus(query_string)
    elif "minus" in query_string:
        return process_minus(query_string)
    elif "both a square and a cube" in query_string:
        return process_cube_square(query_string)
    elif "prime" in query_string:
        return process_prime(query_string)
    else:
        return "Invalid query"


def process_max_number(query_string):
    numbers = query_string.split(" ")[-3:]
    return str(max([int(number[:-1]) for number in numbers]))


def process_min_number(query_string):
    numbers = query_string.split(" ")[-3:]
    return str(min([int(number[:-1]) for number in numbers]))


def process_multiply(query_string):
    number_1 = int(query_string.split(" ")[-4])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 * number_2)


def process_plus(query_string):
    number_1 = int(query_string.split(" ")[-3])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 + number_2)


def process_minus(query_string):
    number_1 = int(query_string.split(" ")[-3])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 - number_2)


def process_cube_square(query_string):
    numbers_string = query_string.split(":")
    numbers_list = numbers_string[-1].split(" ")
    numbers_list = [number[:-1] for number in numbers_list][1:]
    numbers_list = [int(numb) for numb in numbers_list]

    if 1 in numbers_list:
        return "1"

    answer_cubed = []

    for num in numbers_list:
        for i in range(num):
            if i * i * i == num:
                answer_cubed.append(num)

    answer_final = []
    for num in answer_cubed:
        for i in range(num):
            if i * i == num:
                answer_final.append(num)

    return str(answer_final)[1:-1]


def process_prime(query_string):
    numbers_string = query_string.split(":")
    numbers_list = numbers_string[-1].split(" ")
    numbers_list = [number[:-1] for number in numbers_list][1:]
    numbers_list = [int(numb) for numb in numbers_list]

    answer_list = []
    non_prime = []

    for num in numbers_list:
        for i in range(2, num):
            if num % i == 0:
                non_prime.append(num)
                break

    answer_list = [n for n in numbers_list if n not in non_prime and n != 1]

    return str(answer_list)[1:-1]
