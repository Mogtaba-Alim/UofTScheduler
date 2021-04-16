# """This file's purpose is to convert given inputs into an ics format"""
# from ics import Calendar, Event
# import tree
# import datetime
# from week import Week
#
#
# def add_event(c: Calendar, e_name: str, start_date_time: str, end_date_time: str) -> None:
#     """This mutates calendar to add an event."""
#     # transform the event into an event class
#     e = Event()
#     e.name = e_name
#     e.begin = start_date_time
#     e.end = end_date_time
#
#     # add the event
#     c.events.add(e)
#
#
# def create_calendar(t: tree.Tree) -> Calendar:
#     """This takes in a tree data class and converts it into a calendar."""
#
#     # initialize the calendar
#     c = Calendar()
#
#     if t.is_empty():
#         return c
#
#     # go through each subtree
#     for subtree in t._subtrees:
#         if subtree.is_empty():
#             return c
#         else:
#             # create the event
#             add_event(c, t._root[0], t._root[1], t._root[2])
#             create_calendar(subtree)
#
#
# def to_ics(c: Calendar, file_name: str) -> None:
#     """This takes in a calendar, and writes its contents into an ics file"""
#     with open(file_name, 'w') as my_file:
#         my_file.writelines(c)
#
#
# def to_csv(t: tree.Tree, file_name: str) -> None:
#     """This takes in a tree and writes it's contents into a csv file."""
#     with open(file_name, 'w') as my_file:
#         if t.is_empty(): return
#
#         for subtree in t._subtrees:
#             my_file.write(subtree._root[0], subtree._root[1], subtree._root[2])
#             to_csv(subtree)
#
#
# def read_tree_and_conv(t: Week, day: str, time: str, ics_name:str) -> None:
#     """this """
#     c = Calendar()
#     e = Event()
#
#     today = datetime.datetime.today()
#     day_of_week = today.isocalendar()[2] - 1
#     start_date = today - datetime.timedelta(days=day_of_week)
#     dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
#     days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4,
#             'Saturday': 5, 'Sunday': 6}
#     curr_day = days[day]
#
#     for days in t._week:
#         for subtree in days._subtrees:
#             if subtree.return_root()[1] != 'Empty':
#                 time = subtree.return_root()[0]
#                 name = subtree.return_root()[1]
#                 e.name = name
#                 month = str(dates[curr_day].month)
#                 day = str(dates[curr_day].day)
#
#                 if len(month) == 1:
#                     month = '0' + month
#                 if len(day) == 1:
#                     day = '0' + day
#
#                 date = str(dates[curr_day].year) + '-' + month + '-' + day
#                 if len(time) == 5:
#                     time = time + ':00'
#                 else:
#                     time = "0" + time + ":00"
#
#                 e.begin = date + ' ' + time
#                 time2 = time
#                 if time2[-6:-3] == ':00':
#                     time2 = time[0:-6] + ':30:00'
#                 else:
#                     time2 = str(int(time[0:2])+1) + ":" + '00:00'
#
#                 if len(time2) == 7:
#                     time2 = '0' + time2
#
#                 e.end = date + ' ' + time2
#                 c.events.add(e)
#
#                 with open(ics_name, 'w') as my_file:
#                     my_file.writelines(c)
#
#
# if __name__ == '__main__':
#     """test suite"""
#     print("please enter your ics file name in this format: my.ics")
#     ics_name = input()
#     c = Calendar()
#     e = Event()
#
#     # e2 = Event()
#     # e2.name = "My cooler event"
#     # e2.begin = '2021-03-28 02:00:00'
#     # e2.end = '2021-03-28 03:00:00'
#     # c.events.add(e2)
#     #
#     with open(ics_name, 'w') as my_file:
#         my_file.writelines(c)
