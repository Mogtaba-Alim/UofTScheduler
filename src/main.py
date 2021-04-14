""" The main file where our program runs"""
import csv
from typing import Any
import pickle
from week import Week


def pickle_loader(pkl_file) -> Any:
    """load pickle files"""
    try:
        while True:
            yield pickle.load(pkl_file)
    except EOFError:
        pass


if __name__ == '__main__':
    acc_creation = input('Create Account? (y/n)')
    users_to_pickle = {}

    if acc_creation == 'n':
        print("Welcome! Please enter your login")
        user = input("Username: ")
        password = input("Password: ")
        found_user = False

        with open('user_pass.csv') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if user == row[0] and password == row[1]:
                    found_user = True
                    # Generate their schedule
                    break
            if found_user:
                print(f'Welcome {user}')
            else:
                print('user/pass combination not found')

    else:
        print("Welcome! Please create your account")
        user = input("Username: ")
        password = input("Password: ")
        schedule = Week()
        with open('user_pass.csv', 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([user, password])
            file = open('my_trees.pickle', 'wb')
            pickle.dump(schedule, file)

        with open('my_trees.pickle') as f:
            csv_reader = csv.reader('user_pass.csv')
            next(csv_reader)
            for event in pickle_loader(f):
                users_to_pickle[user] = event
                next(csv_reader)







