""" The main file where our program runs"""
import csv
# from typing import Any
import pickle
from week import Week

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
                    break
            if found_user:
                schedule = pickle.load(open(f'{user}.pickle', "rb"))
                print(f'Welcome {user} \n type print(schedule) to view your schedule \n schedule. '
                      f'to see the operations you can do')
            else:
                print('user/pass combination not found')

    else:
        print("Welcome! Please create your account")
        user = input("Username: ")
        password = input("Password: ")
        schedule = Week()
        with open('user_pass.csv', 'a+', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([user, password])
            file = open(f'{user}.pickle', 'wb')
            pickle.dump(schedule, file)
            file.close()
        print('Please rerun the program and log in')

    # os.chdir("../src/reddit")
    # os.system("scrapy crawl all")
