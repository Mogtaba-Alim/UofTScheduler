"""This file's purpose is to convert given inputs into an ics format"""
from ics import Calendar, Event
import tree


def add_event(c: Calendar, e_name: str, start_date_time: str, end_date_time: str) -> None:
    """This mutates calendar to add an event."""
    # transform the event into an event class
    e = Event()
    e.name = e_name
    e.begin = start_date_time
    e.end = end_date_time

    # add the event
    c.events.add(e)


def create_calendar(t: tree.Tree) -> Calendar:
    """This takes in a tree data class and converts it into a calendar."""

    # initialize the calendar
    c = Calendar()

    if t.is_empty():
        return c

    # go through each subtree
    for subtree in t._subtrees:
        if subtree.is_empty():
            return c
        else:
            # create the event
            add_event(c, t._root[0], t._root[1], t._root[2])
            create_calendar(subtree)


def to_ics(c: Calendar, file_name: str) -> None:
    """This takes in a calendar, and writes its contents into an ics file"""
    with open(file_name, 'w') as my_file:
        my_file.writelines(c)


def to_csv(t: tree.Tree, file_name: str) -> None:
    """This takes in a tree and writes it's contents into a csv file."""
    with open(file_name, 'w') as my_file:
        if t.is_empty(): return

        for subtree in t._subtrees:
            my_file.write(subtree._root[0], subtree._root[1], subtree._root[2])
            to_csv(subtree)


if __name__ == '__main__':
    """test suite"""
    # print("please enter your ics file name in this format: my.ics")
    # ics_name = input()
    #
    # c = Calendar()
    # e = Event()
    # e.name = "My cool event"
    # e.begin = '2021-03-28 00:00:00'
    # e.end = '2021-03-28 01:00:00'
    # c.events.add(e)
    #
    # e2 = Event()
    # e2.name = "My cooler event"
    # e2.begin = '2021-03-28 02:00:00'
    # e2.end = '2021-03-28 03:00:00'
    # c.events.add(e2)
    #
    # with open(ics_name, 'w') as my_file:
    #     my_file.writelines(c)
