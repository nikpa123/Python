def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(f'{operation(i, j): ^5}', end = '')
        print()
operation = lambda x, y: x * y
print_operation_table(operation, num_rows=6, num_columns=6)