""" The main file where our program runs"""
import csv
import pickle
from week import Week
import uoft_event_finder
import visualization
import pprint

functions = ["schedule.add_event_date(self, event_name: str, target_day: str, start_time: str, "
             "end_time: str, importance: int, user: str)", "schedule.remove_event_date(self, "
                                                           "event_name: str, target_day: str, "
                                                           "start_time: str, end_time: str, "
                                                           "user: str)", "find_uoft_events()",
             "read_tree_and_conv_to_ics(self, day: str, time: str, ics_file_name: str)"]


def main() -> any:
    """ Calls all our files"""
    acc_creation = input('Create Account?(Y/N) \n'
                         ' Type Y if you are a new user or N if you already have an account')

    if acc_creation == 'N':
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
                print(f'Welcome {user} \n')
                print("#####################################")
                add_events = input("Do you want to see upcoming U of T events(Y/N): ")
                if add_events == "Y":
                    uoft_event_finder.find_uoft_events()
                global schedule
                schedule = pickle.load(open(f'{user}.pickle', "rb"))
                print("#####################################")
                vis = input("Do you wish to visualize your schedule?(Y/N) ")
                if vis == "Y":
                    visualization.visualize(schedule)
                print('Here are all the possible operations to your schedule \n')
                pprint.pprint(functions)

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

        print("Account Created \n Please rerun main.py file to login")


if __name__ == '__main__':
    main()
