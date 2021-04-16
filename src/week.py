""" This is where the week class is implemented"""
import tree
import day
from typing import Optional, List, Any
import pickle


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
