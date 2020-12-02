def get_input():
    with open('../_input/1.txt') as file:
        return [int(line.strip()) for line in file]


def get_2_entries_summing_to(n, entries):
    for entry1 in entries:
        for entry2 in entries:
            if entry1 + entry2 == n:
                return entry1, entry2


def get_3_entries_summing_to(n, entries):
    for entry1 in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry1 + entry2 + entry3 == n:
                    return entry1, entry2, entry3


def main():
    n = 2020
    input_data = get_input()

    expense1, expense2 = get_2_entries_summing_to(n, input_data)
    print(f'Found 2 entries summing to {n}:\n\t{expense1}, {expense2}\nTheir product is {expense1 * expense2}')

    print()

    expense1, expense2, expense3 = get_3_entries_summing_to(n, input_data)
    print(f'Found 3 entries summing to {n}:\n\t{expense1}, {expense2}, {expense3}\n'
          f'Their product is {expense1 * expense2 * expense3}')


if __name__ == '__main__':
    main()
