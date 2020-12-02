def get_input():
    input_data = []
    with open('../_input/2.txt') as file:
        for line in file:
            line_parts = line.strip().split()
            password = line_parts[-1]
            policy_letter = line_parts[1][:1]
            policy_min_max = (int(line_parts[0].split('-')[0]), int(line_parts[0].split('-')[1]))
            input_data.append((password, policy_letter, policy_min_max))
    return input_data


def is_valid_password_old_policy(password, policy_letter, policy_min_max):
    amount_of_policy_letter = len(password.split(policy_letter)) - 1
    return policy_min_max[0] <= amount_of_policy_letter <= policy_min_max[1]


def is_valid_password(password, policy_letter, policy_min_max):
    location1 = password[policy_min_max[0] - 1] == policy_letter
    location2 = password[policy_min_max[1] - 1] == policy_letter
    return (location1 or location2) and not (location1 and location2)


def main():
    input_data = get_input()

    amount_valid = len([None for password, policy_letter, policy_min_max in input_data
                    if is_valid_password_old_policy(password, policy_letter, policy_min_max)])
    print(f'Amount of valid passwords following old policy: {amount_valid}')

    print()

    amount_valid = len([None for password, policy_letter, policy_min_max in input_data
                        if is_valid_password(password, policy_letter, policy_min_max)])
    print(f'Amount of valid passwords following new policy: {amount_valid}')


if __name__ == '__main__':
    main()
