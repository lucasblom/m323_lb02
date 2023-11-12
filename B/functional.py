from functools import reduce


def quadrat_summe(n):
    #B1G
    return sum(map(lambda x: x ** 2, range(1, n + 1)))


def calculations(a, b):
    #B1F
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    added = add(a, b)
    subtracted = subtract(a, b)
    multiplied = multiply(a, b)
    divided = divide(a, b)

    return f'Added: {added},<br> Subtracted: {subtracted},<br> Multiplied: {multiplied},<br> Divided: {divided}'


def calculate_algoritmen(lst):
    #B1E
    def add_one(lst):
        return list(map(lambda x: x + 1, lst))

    def subtract_one(lst):
        return list(map(lambda x: x - 1, lst))

    def multiply_by_two(lst):
        return list(map(lambda x: x * 2, lst))

    def divide_by_two(lst):
        return list(map(lambda x: x / 2, lst))

    added = add_one(lst)
    subtracted = subtract_one(lst)
    multiplied = multiply_by_two(lst)
    divided = divide_by_two(lst)
    return f'Added: {added},<br> Subtracted: {subtracted},<br> Multiplied: {multiplied},<br> Divided: {divided}'


def add(a, b):
    #B2G & B2F
    return a + b


def cal(function, a, b):
    #B2G & B2F
    return function(int(a), int(b))


def multiplier(factor):
    #B2E
    def multiply(number):
        return number * factor
    return multiply


def to_upper(names):
    #B3G
    return list(map(lambda x: x.upper(), names))


#B3F
add_numbers = lambda x, y: x + y


def sort_by_user(lst, criteria):
    #B3E
    return sorted(lst, key=lambda x: x[criteria])


def map_filter_reduce(lst):
    #B4G
    mapped = map(lambda x: x ** 2, lst)
    filtered = filter(lambda x: x > 10, mapped)
    reduced = reduce(lambda x, y: x + y, filtered)
    return reduced


def map_filter_reduce_combined(lst):
    #B4F
    return reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst)))


def filter_through_students(gender, students):
    #B4E
    target_students = list(filter(lambda student: student.gender == gender, students))
    scores_of_target_students = list(map(lambda student: student.scores, target_students))
    print(scores_of_target_students)
    avg_scores_of_target_students = reduce(lambda x, y: x + y, scores_of_target_students) / len(
        scores_of_target_students) if len(scores_of_target_students) > 0 else 0
    return avg_scores_of_target_students


def list_comprehension(lst):
    # C1F
    names = [student.name for student in lst]
    print(names)
    return names


def generator(lst):
    # C1F
    names = list(student.name for student in lst)
    print(names)
    return names