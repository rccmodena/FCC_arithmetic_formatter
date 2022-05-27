#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

class TooManyProblems(Exception):
    """Raise for too many problems"""


class OperatorError(Exception):
    """Raise for not allowed operator"""


class OperandNotNumber(Exception):
    """Raise for not a number operand"""


class OperandGreaterLimit(Exception):
    """Raise for operando too big"""


def verify_problem(problems):
    '''
    Verify if the problem is valid.
    '''

    # Max number of problems is 5
    limit_problem_size = 5
    if len(problems) > limit_problem_size:
        raise TooManyProblems()

    for problem in problems:
        result_str = problem.split()
        if result_str[1]  not in "+-":
            raise OperatorError()
        
        elif not (result_str[0].isdigit() and result_str[2].isdigit()):
            raise OperandNotNumber()

        elif (len(result_str[0]) > 4) or (len(result_str[2]) > 4):
            raise OperandGreaterLimit()


def create_list_str_problems(answer):
    list_str_problems = [""] * 3
    if answer:
        list_str_problems.append("")
    return list_str_problems


def format_problem(problem, answer):
    formated_problem = problem.split()

    # Calculate the number of columns of the problem
    size_problem = max(len(formated_problem[0]), len(formated_problem[2]))

    dict_str_problem = dict()
    dict_str_problem['line_one'] = formated_problem[0].rjust(size_problem + 2)
    dict_str_problem['line_two'] = formated_problem[1] + " " + formated_problem[2].rjust(size_problem)
    dict_str_problem['line_three'] = '-' * (size_problem + 2)

    if answer:
        if formated_problem[1] == '+':
            total = int(formated_problem[0]) + int(formated_problem[2])
        else:
            total = int(formated_problem[0]) - int(formated_problem[2])

        dict_str_problem['line_four'] = str(total).rjust(size_problem + 2)

    return dict_str_problem


def arithmetic_arranger(problems, answer=False):

    try:
        verify_problem(problems)

    except TooManyProblems:
        return "Error: Too many problems."

    except OperatorError:
        return "Error: Operator must be '+' or '-'."

    except OperandNotNumber:
        return "Error: Numbers must only contain digits."

    except OperandGreaterLimit:
        return "Error: Numbers cannot be more than four digits."

    # Create list with the lines of the arranged problems
    list_str_problems = create_list_str_problems(answer)

    n_problems = len(problems)
    for n_problem, problem in enumerate(problems):

        dict_str_problem = format_problem(problem, answer)
        list_str_problems[0] += dict_str_problem['line_one']
        list_str_problems[1] += dict_str_problem['line_two']
        list_str_problems[2] += dict_str_problem['line_three']
        if answer:
            list_str_problems[3] += dict_str_problem['line_four']

        if n_problem != (n_problems - 1):
            if answer:
                n_lines = 4
            else:
                n_lines = 3
            for i in range(n_lines):
                list_str_problems[i] += ' ' * 4

    return "\n".join(list_str_problems)