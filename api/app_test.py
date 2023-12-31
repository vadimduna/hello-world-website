from app import process_query


def test_knows_about_dinosaurs():
    string = "Dinosaurs ruled the Earth 200 million years ago"
    assert process_query("dinosaurs") == string


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_does_know_about_names():
    assert process_query("What is your name?") == "Vadim_Mariia_Kevin_"


def test_returns_largest_number():
    string = "Which of the following numbers is the largest: 25, 89, 26?"
    assert process_query(string) == "89"


def multiple():
    string = "What is 30 multiplied by 76?"
    assert process_query(string) == "2280"


def test_sum():
    string = "What is 37 plus 66?"
    assert process_query(string) == "103"


def test_minus():
    string = "What is 80 minus 90?"
    assert process_query(string) == "-10"


def test_returns_smallest_number():
    string = "Which of the following numbers is the smallest: 25, 9, 26?"
    assert process_query(string) == "9"


def test_cube_square():
    string_1 = "Which of the following numbers is both a square and a cube: "
    string_2 = "1934, 3115, 3915, 64, 2725, 2601, 4096?"
    string = string_1 + string_2
    assert process_query(string) == "64, 4096"


def test_cube_square_one():
    string_1 = "Which of the following numbers is both a square and a cube: "
    string_2 = "1331, 1370, 1770, 2852, 2601, 1, 1273?"
    string = string_1 + string_2
    assert process_query(string) == "1"


def test_prime():
    string_1 = "Which of the following numbers are primes: "
    string_2 = "7, 13, 26, 84, 43?"
    string = string_1 + string_2
    assert process_query(string) == "7, 13, 43"


def test_prime2():
    string_1 = "Which of the following numbers are primes: "
    string_2 = "13, 26, 84, 1?"
    string = string_1 + string_2
    assert process_query(string) == "13"
