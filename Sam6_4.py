def extract_employee_log(log, employee_id):
    try:
        start_index = log.index(employee_id)
        end_index = log.index(employee_id, start_index + 1)
        return tuple(log[start_index:end_index + 1])
    except ValueError:
        return tuple()


employee_log = (1, 2, 3, 4, 2, 5, 6, 2, 7, 8)
employee_id_to_check = 2
result = extract_employee_log(employee_log, employee_id_to_check)
print(result)