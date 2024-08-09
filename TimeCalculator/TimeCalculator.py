def add_time(start, duration, start_day=None):
    # Convertendo o horário de início para minutos
    start_hour, start_minute = map(int, start[:-3].split(':'))
    if start[-2:] == 'PM':
        start_hour += 12
    start_minutes = start_hour * 60 + start_minute

    # Convertendo o tempo de duração para minutos
    duration_hour, duration_minute = map(int, duration.split(':'))
    duration_minutes = duration_hour * 60 + duration_minute

    # Calculando o tempo total em minutos
    total_minutes = start_minutes + duration_minutes

    # Calculando o novo horário e dia
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    days_passed = total_minutes // (24 * 60)

    # Determinando se é AM ou PM
    new_period = 'AM' if new_hour < 12 else 'PM'
    if new_hour >= 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12

    # Determinando o dia da semana, se fornecido
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if start_day:
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + days_passed) % 7
        new_day = ', ' + days_of_week[new_day_index]
    else:
        new_day = ''

    # Determinando a parte da mensagem sobre dias passados
    days_passed_message = ''
    if days_passed == 1:
        days_passed_message = ' (next day)'
    elif days_passed > 1:
        days_passed_message = f' ({days_passed} days later)'

    # Formatando o novo horário e dia
    new_time = f'{new_hour}:{new_minute:02d} {new_period}{new_day}{days_passed_message}'

    return new_time


# Testando a função com o exemplo fornecido
print(add_time('3:30 PM', '2:12'))  # Retorna: 5:42 PM