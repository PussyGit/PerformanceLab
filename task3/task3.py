# Обновление значений в json по id

import json

def update_values(tests, values):
    for test in tests:
        test['value'] = next((value['value'] for value in values if value['id'] == test['id']), '')

        if 'values' in test:
            update_values(test['values'], values)


def main():
    with open('values.json') as values_file:
        values_data = json.load(values_file)
    with open('tests.json') as tests_file:
        tests_data = json.load(tests_file)

    values = values_data['values']
    update_values(tests_data['tests'], values)

    with open('report.json', 'w') as report_file:
        json.dump(tests_data, report_file, indent=2)


if __name__ == '__main__':
    main()
