""" This is where the week class is implemented"""
import day
from typing import List
import pickle
from ics import Calendar, Event
import datetime


class Week:
    """ This class representes a single week in the schedule
    This class uses recursive tree data structures to store information
    """
    _week: List[day.Day]

    def __init__(self) -> None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._week = []
        for i in range(7):
            self._week.append(day.Day(days[i], []))

    def add_event_date(self, event_name: str, target_day: str, start_time: str, end_time: str,
                       importance: int, user: str) -> str:
        """ Adds an event to the specified time and date of the week. If the event slot is already
            filled the importance level of the current event and the new event are compared, if the
            importance level of the new event is higher than the current event the new event will
            replace the current event and the current event will be moved to the next available
            time-slot. Otherwise the new event is placed in the next available time-slot.
            - event_name: The name of the new event
            - target_day: A string corresponding to the day of the week of the new event
            - start_time: The time ofC the day corresponding to the start time of the new event.- Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - end_time: The time of the day corresponding to the end time of the new event. Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - importance: a parameter that measures the measures the importance of the event being
            inserted and is an integer between 0 and 3
        Preconditions
            - 0 <= importance <= 3
            - int(start_time[:-3]) + int(start_time[-2:]) / 100 < \
            - int(end_time[:-3]) + int(end_time[-2:]) / 100
            - target_day in {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday'}
        """
        days_to_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4,
                         'Saturday': 5, 'Sunday': 6}

        remaining_events = []
        for days in self._week:
            if days.identify_day() == target_day:
                # Replaces events that meet the importance criteria and returns un-added or
                # displaced events
                remaining_events.extend(days.replace_event(event_name, importance, start_time,
                                                           end_time))
        # new_start = "0:00"
        # new_end = "0:30"        if remaining_events == []:
        # new_end = "0:30"        if remaining_events == []:
        #             return "Event successfully added"

        # iterate through the remaining events
        for event in remaining_events:
            # check for the next available slot in each day
            for new_days in self._week[days_to_index[target_day]:]:
                # inserts into next available slot
                if new_days.insert_event(event[1], event[2]):
                    break
                else:
                    continue
        if remaining_events == []:
            print("Event successfully added")
            file = open(f'{user}.pickle', 'wb')
            pickle.dump(self, file)
        else:
            return "Current week full"

    def remove_event_date(self, event_name: str, target_day: str, start_time: str, end_time: str,
                          user: str):
        """
        Removes an event from the specified time of the week on the specific day.
            - event_name: The name of the event to be removed
            - target_day: A string corresponding to the day of the week of the removed event
            - start_time: The time of the day corresponding to the start time of the removed event.
              Its format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - end_time: The time of the day corresponding to the end time of the removed event. Its
              format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
        Preconditions
            - int(start_time[:-3]) + int(start_time[-2:]) / 100 < \
            - int(end_time[:-3]) + int(end_time[-2:]) / 100
            - target_day in {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday'}
        """
        for days in self._week:
            if days.identify_day() == target_day:
                days.remove_event(event_name, start_time, end_time)
                print("Event successfully removed")
                file = open(f'{user}.pickle', 'wb')
                pickle.dump(self, file)

    def __str__(self) -> str:
        """ Prints the current schedule"""
        s = ""
        for days in self._week:
            s += days.day_str_indented(0)
        return s

    def get_days(self) -> list:
        """Returns the list of day classes in the week """
        days = []
        for day in self._week:
            days.append(day
                        )
        return days

    def read_tree_and_conv(self, day: str, time: str, ics_name: str):
        """this """
        c = Calendar()
        e = Event()
        
        # line 117 - 121: https://stackoverflow.com/questions/17277002/how-to-get-all-datetime-instances-of-the-current-week-given-a-day
        today = datetime.datetime.today()
        day_of_week = today.isocalendar()[2] - 1
        start_date = today - datetime.timedelta(days=day_of_week)
        dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
        days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4,
                'Saturday': 5, 'Sunday': 6}
        curr_day = days[day]

        for days in self._week:
            for subtree in days.get_subtree():
                if subtree.return_root()[1] != 'Empty':
                    time = subtree.return_root()[0]
                    name = subtree.return_root()[1]
                    e.name = name
                    month = str(dates[curr_day].month)
                    day = str(dates[curr_day].day)

                    if len(month) == 1:
                        month = '0' + month
                    if len(day) == 1:
                        day = '0' + day

                    date = str(dates[curr_day].year) + '-' + month + '-' + day
                    if len(time) == 5:
                        time = time + ':00'
                    else:
                        time = "0" + time + ":00"

                    e.begin = date + ' ' + time
                    time2 = time
                    if time2[-6:-3] == ':00':
                        time2 = time[0:-6] + ':30:00'
                    else:
                        time2 = str(int(time[0:2]) + 1) + ":" + '00:00'

                    if len(time2) == 7:
                        time2 = '0' + time2

                    e.end = date + ' ' + time2
                    c.events.add(e)

                    with open(ics_name, 'w') as my_file:
                        my_file.writelines(c)
