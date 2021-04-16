""" The main file where our program runs"""
import csv
import pickle
from week import Week
import uoft_event_finder


def main() -> any:
    """ Calls all our files"""
    acc_creation = input('Create Account? (y/n)')

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
                global schedule
                schedule = pickle.load(open(f'{user}.pickle', "rb"))
                print(f'Welcome {user} \n  \
                    Please type print(schedule) to view your schedule \n \
                    schedule.f to see the operations you can do')
            else:
                print('username/password combination you entered can not found')
                print('user/pass combination not found')
                print("#####################################")
                print("Retrying")
                print("#####################################")
                main()

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

        print("Account Created \n Please restart to login")



if __name__ == '__main__':
    main()
