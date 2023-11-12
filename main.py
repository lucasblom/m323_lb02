from flask import Flask, request
from student import Student
from A.factorial_pure import factorial
from A.immutable_function import immutable
from A.loesungs_moeglichkeiten import *
from B.functional import *


app = Flask(__name__)


def check_if_student_id_is_valid(student_id):
    if isinstance(student_id, str):
        raise ValueError('Please enter a number!')
    if student_id > len(students):
        raise ValueError('Student not found!')


def check_if_list_of_students_is_valid(student_ids):
    for student_id in student_ids:
        try:
            check_if_student_id_is_valid(int(student_id))
        except ValueError as error:
            raise ValueError(str(error))
    if len(student_ids) > len(students):
        raise ValueError('Too many students entered!')


def check_if_list_is_greater_than_2(lst):
    if len(lst) > 2:
        raise ValueError('Please enter only two numbers!')
    for id in lst:
        try:
            check_if_student_id_is_valid(int(id))
        except ValueError as error:
            raise ValueError(str(error))


@app.route('/a1g')
def pure_function():
    try:
        student_id = int(request.args.get('student_id', default=0))
        check_if_student_id_is_valid(student_id)
        return f'Factorial of {students[student_id].name}`s score is: {factorial(int(students[student_id].scores))}'
    except ValueError as error:
        return str(error)


@app.route('/a1f')
def immutable_function():
    first_name = request.args.get('first_name', default='Alice')
    last_name = request.args.get('last_name', default='Wonderland')
    return f'{immutable(str(first_name), str(last_name))}'


@app.route('/a1e')
def functional_solution():
    try:
        student_id = int(request.args.get('student_id', default=0))
        check_if_student_id_is_valid(student_id)
        return (f'Score of {students[student_id].name} squared with different solutions: '
                f'<br>Functional solution: {quadrat_summe_funktional(students[student_id].scores)} '
                f'<br>Procedural solution: {quadrat_summe_prozedural(students[student_id].scores)} '
                f'<br>Object-oriented solution: {QuadratSummeObjektorientiert(students[student_id].scores).berechne_quadrat_summe()}')
    except ValueError as error:
        return str(error)


@app.route('/b1g')
def algorithm():
    try:
        student_id = int(request.args.get('student_id', default=0))
        check_if_student_id_is_valid(student_id)
        return f'Squared sum of {students[student_id].name} score is: {quadrat_summe(students[student_id].scores)}'
    except ValueError as error:
        return str(error)


@app.route('/b1f')
def sub_functions():
    try:
        a = int(request.args.get('a', default=3))
        b = int(request.args.get('b', default=4))
        check_if_student_id_is_valid(a)
        check_if_student_id_is_valid(b)
        return (f'Basic mathematical calculations with the scores of {students[a].name} and {students[b].name} <br>'
                f'{calculations(students[a].scores, students[b].scores)}')
    except ValueError as error:
        return str(error)


@app.route('/b1e')
def sub_algoritmen():
    try:
        lst = (request.args.get('list', default='0,1,2,3,4')).split(',')
        check_if_list_of_students_is_valid(lst)
        return f'{calculate_algoritmen(list(map(lambda x: students[int(x)].scores, lst)))}'
    except ValueError as error:
        return str(error)


@app.route('/b2g')
def function_as_object():
    try:
        student_ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_is_greater_than_2(student_ids)
        function = add
        return f'{cal(function, students[int(student_ids[0])].scores, students[int(student_ids[1])].scores)}'
    except ValueError as error:
        return str(error)


@app.route('/b2f')
def hochwertige_funktion():
    try:
        student_ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_is_greater_than_2(student_ids)
        return f'{cal(add, students[int(student_ids[0])].scores,students[int(student_ids[1])].scores)}'
    except ValueError as error:
        return str(error)


@app.route('/b2e')
def function_als_objekt():
    factor = int(request.args.get('factor', default=1))
    multiplied = students[int(request.args.get('multiplied', default=1))].scores
    multiplier_by_n = multiplier(factor)
    return f'{multiplier_by_n(multiplied)}'


@app.route('/b3g')
def names():
    try:
        ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_of_students_is_valid(ids)
        names = list(map(lambda x: students[int(x)].name, ids))
        return f'{to_upper(names)}'
    except ValueError as error:
        return str(error)


@app.route('/b3f')
def lambda_multiple_arguments():
    try:
        student_ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_is_greater_than_2(student_ids)
        return f'{add_numbers(int(students[int(student_ids[0])].scores), int(students[int(student_ids[1])].scores))}'
    except ValueError as error:
        return str(error)


@app.route('/b3e')
def sort_with_user():
    userList = [
        {'name': 'Leo', 'age': 18},
        {'name': 'Noah', 'age': 16},
        {'name': 'Gilles', 'age': 20},
        {'name': 'Peter', 'age': 21}
    ]
    criteria = request.args.get('criteria', default='name')
    if criteria not in userList[0].keys():
        return f'Criteria not found!'
    return f'{sort_by_user(userList, criteria)}'


@app.route('/b4g')
def maped_filtered_reduced():
    try:
        ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_of_students_is_valid(ids)
        numbers = list(map(lambda x: students[int(x)].scores, ids))
        return f'{map_filter_reduce(numbers)}'
    except ValueError as error:
        return str(error)


@app.route('/b4f')
def reduce_list():
    try:
        ids = request.args.get('student_ids', default='0,1').split(',')
        check_if_list_of_students_is_valid(ids)
        student_scores = list(map(lambda x: students[int(x)].scores, ids))
        return f'{map_filter_reduce_combined(student_scores)}'
    except ValueError as error:
        return str(error)


@app.route('/b4e')
def reduce_complex():
    gender = request.args.get('gender', default='male')
    if gender not in map(lambda x: students[x].gender, range(len(students))):
        return f'Gender {gender} not found!'
    return f'{filter_through_students(gender, students)}'


@app.route('/c1g')
def comprehend():
    list_comp = list_comprehension(students)
    gen = generator(students)
    return f'{list_comp}{gen}'


if __name__ == '__main__':
    students = [
        Student('Alice', 'male', 85),
        Student('Bob', 'male', 92),
        Student('Charlie', 'male', 78),
        Student('Diana', 'female', 95),
        Student('Eva', 'female', 88),
        Student('Norah', 'female', 90),
        Student('Phrederico', 'male', 88),
        Student('Bobin', 'male', 70),
        Student('Java', 'female', 77)
    ]

    print('Students have been created.')
    print('Running Flask app...')
    app.run(debug=True)
