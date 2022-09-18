#!/usr/local/bin/python3

import sys

def get_subjects_data() -> list:

    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
                    'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov',
                    'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    return set(clients), set(participants), set(recipients)


def call_center_request(clients: set, recipients: set) -> list:

    return list(clients - recipients)


def potential_clients_request(clients: set, participants: set) -> list:

    return list(participants - clients)


def loyalty_program_request(clients: set, participants: set) -> list:

    return list(clients - participants)


def interactive_request_handler(task: str) -> None:

    clients, participants, recipients = get_subjects_data()

    if task == 'call_center':
        print(call_center_request(clients, recipients))
    elif task == 'potential_clients':
        print(potential_clients_request(clients, participants))
    elif task == 'loyalty_program':
        print(loyalty_program_request(clients, participants))
    else:
        raise ValueError('Invalid argument: argument must be one of: ' +
                            '["call_center", "potential_clients", "loyalty_program"]')



def main():

    if len(sys.argv) == 2:
        interactive_request_handler(sys.argv[1])


if __name__ == '__main__':
    main()