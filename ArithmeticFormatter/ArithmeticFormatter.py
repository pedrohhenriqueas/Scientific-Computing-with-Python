def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    arranged_problems = ''
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'

        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(width) + '    '
        line2 += operator + operand2.rjust(width - 1) + '    '
        line3 += '-' * width + '    '


        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2)).rjust(width)
            else:
                answer = str(int(operand1) - int(operand2)).rjust(width)
            line4 += answer + '    '

    arranged_problems += line1.rstrip() + '\n'
    arranged_problems += line2.rstrip() + '\n'
    arranged_problems += line3.rstrip() + '\n'
    if show_answers:
        arranged_problems += line4.rstrip() + '\n'

    return arranged_problems.rstrip()


print(arithmetic_arranger(["1 + 2", "1 - 9380", "2 + 199"], True))

